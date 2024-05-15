@echo off
:: Activate virtual environment
call venv\Scripts\activate

:: Run Flask
start "" flask run

:: Open browser to localhost:5000
start "" http://localhost:5000
