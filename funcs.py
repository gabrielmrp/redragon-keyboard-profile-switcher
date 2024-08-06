import os
import time
import subprocess
from dotenv import load_dotenv
import pygetwindow as gw
import pywinauto
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
# Função para obter a posição e tamanho da janela pelo título
def get_window_by_title(titulo):
    window = gw.getWindowsWithTitle(titulo)
    if window:
        window = window[0]
        return window
    print("Janela não encontrada.")
    return None

# Função para listar todas as janelas abertas
def list_windows():
    result = ''
    for window in gw.getAllWindows():
        if(window.title!='' and window.title[0:len('Redragon')]=='Redragon'):
            result = window.title

    return result

def put_window_on_lefttop_position(window):

    # Usando pywinauto para mover a janela
    app = pywinauto.Application().connect(title=window.title)
    current_window = app.window(title=window.title)

    # Mover a janela para (0, 0) sem afetar o mouse
    current_window.move_window(x=0, y=0, width=window.width, height=window.height)

    # Espera um pouco para garantir que a janela foi movida
    time.sleep(0.2)

    # Verifica a nova posição da janela
    rect = current_window.rectangle()
    new_x, new_y = rect.left, rect.top
    print(f"\n\nNova posição da janela: x={new_x}, y={new_y}")

    return new_x,new_y


def open_redragon_app(path,title):
    """Abre o aplicativo e conecta à janela especificada."""
    
    subprocess.Popen(path)
    
    try:
        app = Application(backend="win32").connect(title=title, timeout=5)
        window = app.window(title=title)
        window.restore()  # Restaura a janela se ela estiver minimizada
        window.maximize()  # Maximiza a janela para garantir que ela esteja em primeiro plano
        print(f"Janela '{title}' conectada com sucesso.")
        return window
    except ElementNotFoundError:
        print(f"Janela com o título '{title}' não encontrada.")
        # Você pode adicionar código aqui para abrir o aplicativo, se necessário
        return None

    time.sleep(0.2)  # Aguarda um breve momento para garantir que a janela esteja totalmente carregada
