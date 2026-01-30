from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

from core import downloader
from core.security import get_password_hash, verify_password
from platforms.youtube import YouTube
from platforms.tiktok import TikTok
from database.db import get_db, User, UserToken

# TODO: Move to environment variable
JWT_SECRET = "a_very_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ACCESS_CODE = "1024"

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    access_code: str

class UserLogin(BaseModel):
    email: str
    password: str

app = FastAPI(title="Omni-Clipper API")

# Enable CORS for the Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    print(f"Signup request received: {user.dict()}")
    if user.access_code != ACCESS_CODE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid access code",
        )
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, name=user.name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(db_user.id), "exp": datetime.utcnow() + access_token_expires}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer", "user": {"id": db_user.id, "email": db_user.email, "name": db_user.name}}

@app.get("/")
def health_check():
    return {"status": "Backend is Online 🟢"}

@app.post("/process-video")
def process_video(url: str):
    # Stub for future logic
    print(f"Processing {url}...")
    return {"status": "started", "message": "Download queued"}

# --- Authentication ---
@app.get("/auth/youtube")
def auth_youtube():
    youtube = YouTube()
    auth_url = youtube.auth()
    return RedirectResponse(auth_url)

@app.get("/auth/youtube/callback")
def auth_youtube_callback(request: Request, db: Session = Depends(get_db)):
    youtube = YouTube()
    code = request.query_params.get('code')
    youtube.flow.fetch_token(code=code)
    credentials = youtube.flow.credentials

    # Get user info from id_token
    id_token = credentials.id_token
    claims = jwt.get_unverified_claims(id_token)
    user_email = claims.get("email")

    # Create or update user
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        user = User(email=user_email)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Store tokens
    token = db.query(UserToken).filter(UserToken.user_id == user.id, UserToken.platform == 'youtube').first()
    if not token:
        token = UserToken(user_id=user.id, platform='youtube')
    
    token.access_token = credentials.token
    token.refresh_token = credentials.refresh_token
    db.add(token)
    db.commit()

    # Create JWT
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(user.id), "exp": datetime.utcnow() + access_token_expires}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

    response = RedirectResponse(url="http://localhost:3000/")
    response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
    return response

@app.get("/auth/tiktok")
def auth_tiktok():
    return RedirectResponse("/auth/tiktok/mock_callback")

@app.get("/auth/tiktok/mock_callback")
def auth_tiktok_mock_callback(db: Session = Depends(get_db)):
    # This is a mock implementation of the TikTok authentication callback.
    user_email = "tiktok-user@example.com"

    # Create or update user
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        user = User(email=user_email)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Store dummy tokens
    token = db.query(UserToken).filter(UserToken.user_id == user.id, UserToken.platform == 'tiktok').first()
    if not token:
        token = UserToken(user_id=user.id, platform='tiktok')
    
    token.access_token = "mock_access_token"
    token.refresh_token = "mock_refresh_token"
    db.add(token)
    db.commit()

    # Create JWT
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(user.id), "exp": datetime.utcnow() + access_token_expires}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

    response = RedirectResponse(url="http://localhost:3000/")
    response.set_cookie(key="access_token", value=encoded_jwt, httponly=True)
    return response

@app.get("/auth/tiktok/callback")
def auth_tiktok_callback(request: Request):
    # TODO: Handle callback, exchange code for token, create JWT
    return {"status": "success"}
