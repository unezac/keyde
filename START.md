# 🚀 KeyGermany - QUICK START GUIDE

## ⚠️ CRITICAL: Before Running - Install Dependencies

```powershell
# From root directory
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

---

## 🎯 Option 1: Run Using PowerShell Script (RECOMMENDED)

```powershell
# From root directory
.\run.ps1
```

This will:
- ✅ Kill any existing processes on ports 8000 & 3000
- ✅ Start Backend (FastAPI) on http://127.0.0.1:8000
- ✅ Start Frontend (HTTP Server) on http://127.0.0.1:3000
- ✅ Automatically initialize database with sample data

---

## 🎯 Option 2: Run Using Batch Script

```cmd
# From root directory
run.bat
```

---

## 🎯 Option 3: Run Manually (2 Terminals)

### Terminal 1: Start Backend API
```powershell
# From root directory
cd D:\CODEcopilot\KeyGermany.de
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Terminal 2: Start Frontend HTTP Server
```powershell
# From frontend directory
cd D:\CODEcopilot\KeyGermany.de\frontend
python -m http.server 3000
```

Expected output:
```
Serving HTTP on :: port 3000 (http://[::]:3000/)
```

---

## 🌐 Access the Application

| Component | URL |
|-----------|-----|
| **Frontend App** | http://127.0.0.1:3000 |
| **API Docs** | http://127.0.0.1:8000/docs |
| **Health Check** | http://127.0.0.1:8000/api/health |
| **Random Sentence** | http://127.0.0.1:8000/api/sentences/random |

---

## 🔧 Troubleshooting

### ❌ "Port already in use" error?

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

### ❌ Database errors?

Delete the existing database to reset:
```powershell
Remove-Item backend/keygermany.db -Force
```

The database will auto-recreate on startup with sample data.

### ❌ Import errors or ModuleNotFoundError?

Reinstall dependencies:
```powershell
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

### ❌ Frontend not connecting to API?

1. Verify backend is running on port 8000
2. Check browser console (F12) for CORS errors
3. Verify `API_BASE_URL = 'http://127.0.0.1:8000/api'` in `frontend/script.js`

---

## 📋 Features

✅ Real-time typing validation with color feedback  
✅ German/English/Arabic translations  
✅ Automatic speech synthesis  
✅ Dynamic keyboard visualization  
✅ Statistics tracking (WPM, Accuracy)  
✅ Achievement system  
✅ Favorite sentence bookmarking  
✅ Multiple difficulty levels (A1-C1)  
✅ Category filtering  

---

## 📂 Project Structure

```
KeyGermany.de/
├── backend/
│   ├── app/
│   │   ├── main.py              ← FastAPI app
│   │   ├── core/database.py     ← SQLite + migrations
│   │   ├── models/              ← SQLAlchemy models
│   │   ├── routes/              ← API endpoints
│   │   └── schemas/             ← Pydantic models
│   ├── requirements.txt         ← Python dependencies
│   └── keygermany.db           ← SQLite database (auto-created)
├── frontend/
│   ├── index.html              ← Main page
│   ├── script.js               ← App logic
│   └── style.css               ← Styling
└── database/
    └── schema.sql              ← Reference schema
```

---

## 🛠 API Endpoints

- `GET /api/health` - Health check
- `GET /api/sentences/random` - Random sentence
- `GET /api/sentences` - All sentences (filterable)
- `POST /api/sentences` - Add new sentence
- `GET /api/categories` - All categories
- `GET /api/levels` - All difficulty levels

---

## 💡 Tips

1. **Hot Reload**: Backend auto-reloads on code changes
2. **Offline Mode**: Frontend has fallback sentences if API is down
3. **Local Storage**: Settings persist in browser
4. **Statistics**: Stats are saved in browser LocalStorage

---

Generated: 2026-04-30  
Last Updated: After bug fixes
