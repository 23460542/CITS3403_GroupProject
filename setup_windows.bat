@echo off
REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate

echo Virtual environment setup is complete.