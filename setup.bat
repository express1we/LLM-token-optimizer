@echo off
REM Project environment setup — finds Python and runs setup.py
REM Compatible with venv, system Python, and common install locations

setlocal enabledelayedexpansion

set "PYTHON="

where python >nul 2>&1 && set "PYTHON=python" && goto :found
where python3 >nul 2>&1 && set "PYTHON=python3" && goto :found

if exist ".venv\Scripts\python.exe" set "PYTHON=.venv\Scripts\python.exe" && goto :found

for %%V in (313 312 311 310 39) do (
    if exist "%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe" (
        set "PYTHON=%LOCALAPPDATA%\Programs\Python\Python%%V\python.exe"
        goto :found
    )
)

for %%V in (313 312 311 310 39) do (
    if exist "%ProgramFiles%\Python%%V\python.exe" (
        set "PYTHON=%ProgramFiles%\Python%%V\python.exe"
        goto :found
    )
)

where py >nul 2>&1 && set "PYTHON=py" && goto :found

echo Error: Python not found. Please install Python 3.9+ and try again.
exit /b 1

:found
echo Using Python: %PYTHON%
"%PYTHON%" setup.py
