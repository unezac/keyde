# KeyGermany - Run Full Project (PowerShell)
# Usage: .\run.ps1

Write-Host "`n" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green
Write-Host "         KeyGermany Typing Trainer" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green
Write-Host "`n" -ForegroundColor Green

$ProjectPath = $PSScriptRoot
$FrontendPath = Join-Path $ProjectPath "frontend"
$env:PYTHONDONTWRITEBYTECODE = "1"

# Kill any existing processes on ports 8000 and 3000
Write-Host "Checking for existing processes..." -ForegroundColor Yellow
$port8000 = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue
if ($port8000) {
    Write-Host "Stopping process on port 8000..." -ForegroundColor Yellow
    Stop-Process -Id $port8000.OwningProcess -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

$port3000 = Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue
if ($port3000) {
    Write-Host "Stopping process on port 3000..." -ForegroundColor Yellow
    Stop-Process -Id $port3000.OwningProcess -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 1
}

# Start Backend
Write-Host "Starting Backend (Port 8000)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PYTHONDONTWRITEBYTECODE='1'; cd '$ProjectPath'; python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000"

Start-Sleep -Seconds 2

# Start Frontend
Write-Host "Starting Frontend (Port 3000)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PYTHONDONTWRITEBYTECODE='1'; cd '$FrontendPath'; python -m http.server 3000"

Start-Sleep -Seconds 1

Write-Host "`n" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green
Write-Host "         Project Started!" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green
Write-Host "`n" -ForegroundColor Green
Write-Host "Frontend:  " -ForegroundColor Yellow -NoNewLine
Write-Host "http://127.0.0.1:3000" -ForegroundColor Green

Write-Host "API Docs:  " -ForegroundColor Yellow -NoNewLine
Write-Host "http://127.0.0.1:8000/docs" -ForegroundColor Green

Write-Host "Health:    " -ForegroundColor Yellow -NoNewLine
Write-Host "http://127.0.0.1:8000/api/health" -ForegroundColor Green

Write-Host "`n" -ForegroundColor Green
Write-Host "Both terminal windows are now open." -ForegroundColor Yellow
Write-Host "Press CTRL+C in any terminal to stop the server." -ForegroundColor Yellow
Write-Host "`n" -ForegroundColor Green

Read-Host "Press Enter to exit this window"
