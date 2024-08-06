@echo off
REM Ativa o ambiente virtual chamado "red"
call red\Scripts\activate.bat

REM Executa o script run.py com o argumento 1
python run.py 1

REM Desativa o ambiente virtual após a execução
deactivate