@echo off
REM KeyGermany - Complete Setup and Run Script
REM This script installs dependencies and runs the entire project

echo.
echo =================================================
echo     KeyGermany - Complete Setup & Run
echo =================================================
echo.

cd /d %~dp0
set PYTHONDONTWRITEBYTECODE=1

echo [1/4] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [2/4] Installing dependencies...
python -m pip install -r backend/requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Dependency installation failed!
    echo Try running this manually:
    echo   python -m pip install -r backend/requirements.txt
    pause
    exit /b 1
)

echo.
echo [3/4] Starting Backend (Port 8000)...
start cmd /k "cd /d %~dp0 && set PYTHONDONTWRITEBYTECODE=1 && python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000"

timeout /t 3

echo [4/4] Starting Frontend (Port 3000)...
start cmd /k "cd /d %~dp0frontend && set PYTHONDONTWRITEBYTECODE=1 && python -m http.server 3000"

echo.
echo =================================================
echo         Setup Complete! Project Started
echo =================================================
echo.
echo Frontend:  http://127.0.0.1:3000
echo API Docs:  http://127.0.0.1:8000/docs
echo Health:    http://127.0.0.1:8000/api/health
echo.
echo Press any key to close this window...
pause
