#!/usr/bin/env powershell
<#
.SYNOPSIS
Concert Ticket QR System - Startup Script

.DESCRIPTION
Starts either the backend API server or frontend React app

.PARAMETER Server
The server to start: 'backend', 'frontend', or 'both'

.EXAMPLE
.\run.ps1 backend
.\run.ps1 frontend
#>

param(
    [ValidateSet('backend', 'frontend')]
    [string]$Server
)

$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BackendDir = Join-Path $RootDir "backend"
$FrontendDir = Join-Path $RootDir "frontend"
$PythonExe = Join-Path $RootDir ".venv\Scripts\python.exe"

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Concert Ticket QR System Startup" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

if (-not $Server) {
    Write-Host "Usage: .\run.ps1 <backend|frontend>" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Green
    Write-Host "  .\run.ps1 backend     # Start API server on http://127.0.0.1:8000" -ForegroundColor Green
    Write-Host "  .\run.ps1 frontend    # Start React app on http://localhost:3000" -ForegroundColor Green
    Write-Host ""
    exit 0
}

switch ($Server) {
    "backend" {
        Write-Host "Starting Backend API Server..." -ForegroundColor Green
        Write-Host "Database: SQLite (test_concert.db)" -ForegroundColor Gray
        Write-Host "URL: http://127.0.0.1:8000" -ForegroundColor Gray
        Write-Host "Docs: http://127.0.0.1:8000/docs" -ForegroundColor Gray
        Write-Host ""
        
        Set-Location $BackendDir
        
        # Initialize database if not exists
        if (-not (Test-Path "test_concert.db")) {
            Write-Host "Initializing database..." -ForegroundColor Yellow
            & $PythonExe init_db.py
            Write-Host ""
        }
        
        Write-Host "Starting server..." -ForegroundColor Green
        & $PythonExe -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
    }
    
    "frontend" {
        Write-Host "Starting Frontend React App..." -ForegroundColor Green
        Write-Host "URL: http://localhost:3000" -ForegroundColor Gray
        Write-Host ""
        
        Set-Location $FrontendDir
        npm start
    }
}
