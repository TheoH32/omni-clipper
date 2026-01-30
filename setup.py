import os

# Define the structure and file contents
monorepo_structure = {
    # --- ROOT CONFIG ---
    ".gitignore": """node_modules/
venv/
__pycache__/
.env
.DS_Store
dist/
apps/api/temp/
apps/api/database/*.db
""",
    "README.md": """# ✂️ Omni-Clipper Monorepo

## Architecture
- **apps/api**: Python/FastAPI backend for video processing.
- **apps/web**: React/Vite frontend for the dashboard.

## Quick Start
1. **Backend:**
   `cd apps/api && pip install -r requirements.txt && uvicorn main:app --reload`
2. **Frontend:**
   `cd apps/web && npm install && npm run dev`
""",

    # --- BACKEND (API) ---
    "apps/api/requirements.txt": """fastapi
uvicorn
python-dotenv
requests
yt-dlp
moviepy
jinja2
python-multipart
sqlalchemy
""",
    "apps/api/.env": """TIKTOK_CLIENT_KEY=your_key
TIKTOK_CLIENT_SECRET=your_secret
""",
    "apps/api/main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import downloader

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
""",
    "apps/api/core/__init__.py": "",
    "apps/api/core/downloader.py": """def download_video(url):
    print(f"Downloading {url}...")
    return "path/to/video.mp4"
""",
    "apps/api/core/editor.py": """def crop_to_vertical(input_path):
    print("Cropping video to 9:16...")
    return "path/to/vertical_video.mp4"
""",
    "apps/api/platforms/__init__.py": "",
    "apps/api/platforms/base.py": """from abc import ABC, abstractmethod

class SocialPlatform(ABC):
    @abstractmethod
    def upload(self, file_path): pass
""",
    "apps/api/database/__init__.py": "",

    # --- FRONTEND (WEB) ---
    "apps/web/package.json": """{
  "name": "omni-clipper-web",
  "private": true,
  "version": "0.0.1",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.0",
    "vite": "^4.4.0"
  }
}
""",
    "apps/web/vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
  }
})
""",
    "apps/web/index.html": """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Omni-Clipper</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",
    "apps/web/src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""",
    "apps/web/src/App.jsx": """import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [status, setStatus] = useState('Idle')

  const handleClip = async () => {
    setStatus('Requesting...')
    try {
        const response = await fetch(`http://localhost:8000/process-video?url=${encodeURIComponent(url)}`, {
            method: 'POST'
        })
        const data = await response.json()
        setStatus(`Server says: ${data.message}`)
    } catch (e) {
        setStatus('Error connecting to backend')
    }
  }

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>✂️ Omni-Clipper Dashboard</h1>
      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input 
            type="text" 
            placeholder="Paste YouTube URL..." 
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            style={{ padding: '10px', width: '300px' }}
        />
        <button onClick={handleClip} style={{ padding: '10px 20px', cursor: 'pointer' }}>
            Generate Clips
        </button>
      </div>
      <div style={{ padding: '20px', background: '#f0f0f0', borderRadius: '8px' }}>
        <strong>Status:</strong> {status}
      </div>
    </div>
  )
}

export default App
""",
    "apps/web/src/index.css": """body { margin: 0; background: #fafafa; }""",
    
    # --- PACKAGES (SHARED) ---
    "packages/types/index.ts": "// Shared Typescript interfaces go here",
}

def create_monorepo():
    print("🏗️  Initializing Omni-Clipper Monorepo...")
    
    for filepath, content in monorepo_structure.items():
        # Ensure directory exists
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        # Write file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  + Created: {filepath}")
    
    # Create empty folders that might be needed
    os.makedirs("apps/api/temp/raw", exist_ok=True)
    os.makedirs("apps/api/temp/processed", exist_ok=True)
    
    print("\n✅ Setup Complete!")
    print("\n--- NEXT STEPS ---")
    print("1. Open two terminal tabs.")
    print("2. Terminal A (Backend):")
    print("   cd apps/api")
    print("   python3 -m venv venv && source venv/bin/activate")
    print("   pip install -r requirements.txt")
    print("   uvicorn main:app --reload")
    print("\n3. Terminal B (Frontend):")
    print("   cd apps/web")
    print("   npm install")
    print("   npm run dev")

if __name__ == "__main__":
    create_monorepo()