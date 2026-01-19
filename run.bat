@echo off
REM Concert Ticket QR System - Startup Script

echo.
echo ========================================================
echo  Concert Ticket QR System Startup
echo ========================================================
echo.

REM Check if both arguments are provided
if "%1"=="backend" goto start_backend
if "%1"=="frontend" goto start_frontend
if "%1"=="" goto show_help

:show_help
echo Usage: run.bat [command]
echo.
echo Commands:
echo   backend   - Start FastAPI backend server on port 8000
echo   frontend  - Start React frontend on port 3000
echo   both      - Start both (requires two terminal windows)
echo.
echo Example:
echo   run.bat backend
echo   run.bat frontend (in another terminal)
echo.
goto end

:start_backend
echo Starting Backend Server...
cd /d "%~dp0backend"
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
goto end

:start_frontend
echo Starting Frontend Server...
cd /d "%~dp0frontend"
call npm start
goto end

:end
pause
