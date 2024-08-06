@echo off
REM Check if virtualenv is installed
python -m pip show virtualenv >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    REM Install virtualenv if it's not installed
    echo Installing virtualenv...
    python -m pip install virtualenv
)

REM Create a virtual environment named 'red'
echo Creating virtual environment...
python -m virtualenv red

REM Activate the virtual environment
echo Activating virtual environment...
call red\Scripts\activate

REM Install dependencies from requirements.txt
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Inform the user that the virtual environment has been created and dependencies installed
echo Virtual environment 'red' has been created and dependencies have been installed.
pause