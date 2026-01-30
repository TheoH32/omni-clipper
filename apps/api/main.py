from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from core import downloader
from platforms.youtube import YouTube
from platforms.tiktok import TikTok

app = FastAPI(title="Omni-Clipper API")

# Enable CORS for the Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    # TODO: Get auth URL from youtube class
    youtube = YouTube()
    auth_url = youtube.auth() # This will be the auth url
    return RedirectResponse(auth_url)

@app.get("/auth/youtube/callback")
def auth_youtube_callback(request: Request):
    # TODO: Handle callback, exchange code for token, create JWT
    return {"status": "success"}

@app.get("/auth/tiktok")
def auth_tiktok():
    # TODO: Get auth URL from tiktok class
    tiktok = TikTok()
    auth_url = tiktok.auth() # This will be the auth url
    return RedirectResponse(auth_url)

@app.get("/auth/tiktok/callback")
def auth_tiktok_callback(request: Request):
    # TODO: Handle callback, exchange code for token, create JWT
    return {"status": "success"}
