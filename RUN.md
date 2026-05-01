# KeyGermany - How to Run the Project

## Prerequisites
- Python 3.9+ installed
- Virtual environment activated (`.venv`)

## Quick Start (2 terminals)

### Terminal 1: Start Backend API
```powershell
cd D:\CODEcopilot\KeyGermany.de
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Output should show:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

### Terminal 2: Start Frontend
```powershell
cd D:\CODEcopilot\KeyGermany.de\frontend
python -m http.server 3000
```

Output should show:
```
Serving HTTP on :: port 3000 (http://[::]:3000/) ...
```

## Access the App

- **Frontend App**: http://127.0.0.1:3000
- **API Docs**: http://127.0.0.1:8000/docs
- **API Health Check**: http://127.0.0.1:8000/api/health

## Troubleshooting

### Port Already in Use Error
If you get "Port already in use" error:

**For port 8000:**
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**For port 3000:**
```powershell
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### Database Issues
- Delete `keygermany.db` to reset database
- Database auto-creates on startup with sample data

### CORS Issues (frontend can't reach API)
- Backend has CORS enabled for `*` (all origins)
- Check browser console for errors

### Speech Synthesis Not Working
- Requires German voice on system
- Falls back gracefully if unavailable

## Project Structure
```
KeyGermany.de/
├── backend/
│   ├── main.py           # FastAPI app & endpoints
│   ├── database.py       # SQLite setup
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── index.html        # Main page
│   ├── script.js         # App logic
│   ├── style.css         # Styling
├── database/
│   └── schema.sql        # Schema reference
└── keygermany.db        # SQLite database (auto-created)
```

## API Endpoints

- `GET /` - Root info
- `GET /api/health` - Health check
- `GET /api/sentences/random` - Random sentence
- `GET /api/sentences` - All sentences
- `POST /api/sentences` - Add new sentence

## Features
✅ Real-time typing validation
✅ German/English/Arabic translations
✅ Automatic speech synthesis
✅ Keyboard highlighting
✅ Theme switcher
✅ Progress tracking
✅ Works offline with fallback data

## Notes
- Backend auto-initializes database on startup
- Frontend has fallback sentences if API is down
- No external database needed (SQLite built-in)
- Development mode has hot-reload enabled
