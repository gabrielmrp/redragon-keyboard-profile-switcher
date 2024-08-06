@echo off
REM Ativa o ambiente virtual chamado "red"
call red\Scripts\activate.bat

REM Executa o script pos.py
python pos.py

REM Desativa o ambiente virtual após a execução
deactivate