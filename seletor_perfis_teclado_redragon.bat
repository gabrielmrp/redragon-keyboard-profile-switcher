@echo off
REM Ativa o ambiente virtual chamado "red"
call red\Scripts\activate.bat

REM Executa o script tray.py em segundo plano e fecha a janela do CMD
start "" "start_tray.vbs"
exit