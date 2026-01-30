omni-clipper/
│
├── README.md               # 📘 Documentation: How to run dev servers, API docs.
├── .gitignore              # 🛡️ Safety: Ignores node_modules, venv, .env, and large video files.
│
├── /apps                   # 🚀 THE APPLICATIONS
│   │
│   ├── /api                # 🐍 BACKEND (The Heavy Lifter)
│   │   │                   # Responsibility: Video processing, Database access, API endpoints.
│   │   ├── .env            # 🔑 SECURE: API Keys (OPENAI_KEY, TIKTOK_CLIENT_SECRET).
│   │   ├── main.py         # 🚦 Entry Point: Sets up FastAPI, CORS, and Routes.
│   │   ├── requirements.txt# 📦 Python Deps: fastapi, uvicorn, yt-dlp, moviepy.
│   │   │
│   │   ├── /core           # 🧠 THE BRAIN (Platform Agnostic Logic)
│   │   │   ├── downloader.py   # Uses yt-dlp to fetch raw video from URL.
│   │   │   ├── editor.py       # Uses MoviePy to crop (16:9 -> 9:16), resize, and burn subs.
│   │   │   └── utils.py        # Helpers: File cleanup, time formatters.
│   │   │
│   │   ├── /platforms      # 🔌 THE PLUGINS (Social Media Logic)
│   │   │   ├── base.py         # Abstract Class: Enforces `auth()` and `upload()` methods.
│   │   │   ├── tiktok.py       # TikTok-specific OAuth flow and API calls.
│   │   │   └── youtube.py      # Google API Client logic for Shorts.
│   │   │
│   │   ├── /database       # 💾 MEMORY
│   │   │   ├── db.py           # SQLite connection setup.
│   │   │   └── models.py       # SQL Tables: UserTokens, VideoHistory.
│   │   │
│   │   └── /temp           # 🗑️ WORKSPACE (Gitignored)
│   │       ├── raw/            # Downloads land here first.
│   │       └── processed/      # Edited vertical clips wait here for upload.
│   │
│   └── /web                # ⚛️ FRONTEND (The Control Center)
│       │                   # Responsibility: User UI, Auth flow handling, Progress bars.
│       ├── package.json    # 📦 JS Deps: React, Vite, Axios, TailwindCSS.
│       ├── .env            # 🌍 Public Config: VITE_API_URL="http://localhost:8000"
│       ├── vite.config.js  # ⚡ Bundler: Hot module reloading config.
│       │
│       └── /src            # 🎨 UI CODE
│           ├── main.jsx        # React Entry point.
│           ├── App.jsx         # Main Layout (Sidebar, Dashboard).
│           ├── /components     # Widgets: <UrlInput />, <PlatformToggle />, <VideoPreview />.
│           └── /hooks          # Logic: useUploadStatus(), useAuth().
│
└── /packages               # 📦 SHARED (Optional / Future Proofing)
    └── /types              # 📐 Definitions: If you use TypeScript, put shared interfaces here
                            # (e.g., VideoStatusEnum) so both Frontend and Backend agree on data.