@echo off
REM KeyGermany - Run Full Project

echo.
echo =================================================
echo         KeyGermany Typing Trainer
echo =================================================
echo.
echo Starting Backend (Port 8000)...
set PYTHONDONTWRITEBYTECODE=1
start cmd /k "cd /d %~dp0 && set PYTHONDONTWRITEBYTECODE=1 && python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000"

timeout /t 2

echo Starting Frontend (Port 3000)...
start cmd /k "cd /d %~dp0frontend && set PYTHONDONTWRITEBYTECODE=1 && python -m http.server 3000"

echo.
echo =================================================
echo         Project Started!
echo =================================================
echo.
echo Frontend:  http://127.0.0.1:3000
echo API Docs:  http://127.0.0.1:8000/docs
echo Health:    http://127.0.0.1:8000/api/health
echo.
echo Close either terminal to stop the server.
echo Press CTRL+C in the terminal to stop.
echo.
pause
