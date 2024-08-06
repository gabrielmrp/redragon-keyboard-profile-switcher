@echo off
REM Verifica se o arquivo .dot existe
IF NOT EXIST ".env" (
    echo O arquivo .env nao foi encontrado.
    echo Por favor, renomeie o arquivo ref.env para .env e atualize os dados conforme necessário.
    pause
    exit /b
)

REM Ativa o ambiente virtual chamado "red"
call red\Scripts\activate.bat

REM Executa o script tray.py em segundo plano e fecha a janela do CMD
start python tray.py
exit