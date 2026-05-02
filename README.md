# KeyGermany - German Typing Trainer

> A modern, interactive German typing practice application with real-time validation, speech synthesis, and progress tracking.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 3000
```

Open **http://127.0.0.1:3000**

## Features

- Real-time typing validation with accuracy tracking
- Multi-language support (German, English, Arabic)
- Audio pronunciation via speech synthesis
- Difficulty levels (A1-C1) and category filtering
- Statistics and achievements system
- Interactive QWERTZ/QWERTY/AZERTY keyboard
- Theme selection (Light/Dark/Soft)
- Offline mode with fallback sentences

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/sentences` | List sentences (query: `level`, `category`, `limit`) |
| GET | `/api/sentences/random` | Random sentence (query: `level`, `category`) |
| POST | `/api/sentences` | Create a new sentence |
| GET | `/api/categories` | List all categories |
| GET | `/api/levels` | List all difficulty levels |

API docs: **http://127.0.0.1:3000/docs**

## Project Structure

```
keyde/
├── main.py                 # FastAPI app (serves frontend + API)
├── requirements.txt        # Python dependencies
├── static/                 # Frontend files
│   ├── index.html
│   ├── style.css
│   └── script.js
├── app/                    # Backend logic
│   ├── core/database.py    # SQLite setup + migrations
│   ├── models/models.py    # SQLAlchemy models
│   ├── routes/             # API route handlers
│   └── schemas/schemas.py  # Pydantic schemas
├── database/
│   └── schema.sql          # Reference schema
└── README.md
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | Optional. Set to use PostgreSQL. Defaults to SQLite (`keygermany.db`). |
