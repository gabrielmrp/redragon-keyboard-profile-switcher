import os
import sys
import io
import subprocess
import json
import warnings
import time
import argparse
import pyautogui

from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError

from dotenv import load_dotenv
from funcs import get_window_by_title, list_windows,open_redragon_app
from funcs import  put_window_on_lefttop_position



# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pywinauto')

COORDENADAS_DEFINIDAS = True

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Personalize a mensagem de erro em português
        sys.stderr.write("Erro: O argumento 'perfil' é necessário.\n")

        sys.stderr.write("Use: python run.py 1\n   python run.py 2\n")
        sys.stderr.write("ou python run.py 3")
        sys.exit(1)

# Função para mover a janela para a posição (0, 0) e automatizar ações
def automate_actions(current_window,
        x_perfil_selected_button, y_perfil_selected_button, x_aplicar_button, y_aplicar_button):

    new_x,new_y = put_window_on_lefttop_position(current_window)

    # Coordenadas absolutas
    x_perfil_absoluto = new_x + x_perfil_selected_button
    y_perfil_absoluto = new_y + y_perfil_selected_button
    x_aplicar_absoluto = new_x + x_aplicar_button
    y_aplicar_absoluto = new_y + y_aplicar_button

    # Clica no botão do perfil
    pyautogui.click(x_perfil_absoluto, y_perfil_absoluto)
    time.sleep(0.2)
    # Clica no botão "Aplicar"
    pyautogui.click(x_aplicar_absoluto, y_aplicar_absoluto)
    print("Ações automatizadas concluídas.")
    time.sleep(0.2)


def parse_perfil_argument():
    """Configura e parseia o argumento de perfil da linha de comando."""
    parser = CustomArgumentParser(description='Automatize ações para perfis.')

    parser.add_argument(
        'perfil',
        type=int,
        choices=[1, 2, 3],
        help='Número do perfil (1, 2 ou 3)'
    )

    # Redireciona stderr para uma variável para capturar qualquer saída de erro
    stderr = sys.stderr
    sys.stderr = io.StringIO()

    try:
        args = parser.parse_args()
        perfil = args.perfil
        print(f'Perfil selecionado: {perfil}')
        return perfil

    except SystemExit:
        # Captura e mostra a mensagem personalizada em português
        error_message = sys.stderr.getvalue()
        print(error_message.strip())
        sys.exit(1)
    finally:
        # Restaura stderr ori
        sys.stderr = stderr

def load_coordinates():
    """Carrega as coordenadas do arquivo de configuração e retorna as posições definidas."""
    with open('config.json', 'r', encoding='utf-8') as file:
        positions = json.load(file)

    if COORDENADAS_DEFINIDAS:
        def_positions = {
            1: [positions['PERFIL1_X'], positions['PERFIL1_Y']],
            2: [positions['PERFIL2_X'], positions['PERFIL2_Y']],
            3: [positions['PERFIL3_X'], positions['PERFIL3_Y']],
            "Apply": [positions['APLICAR_X'], positions['APLICAR_Y']]
        }
    else:
        def_positions = {
            1: [145, 184],
            2: [145, 220],
            3: [145, 256],
            "Apply": [641, 580]
        }

    x_perfil, y_perfil = def_positions[perfil]  # Coordenadas do perfil selecionado
    x_aplicar, y_aplicar = def_positions["Apply"]  # Coordenadas do botão "Aplicar"

    return x_perfil,y_perfil,x_aplicar,y_aplicar

if __name__ == "__main__":

    load_dotenv()


    perfil = parse_perfil_argument() 

    path = os.getenv("CAMINHO_APLICAÇÃO") + "KeyboardDrv.exe"
    window_title = os.getenv("TÍTULO_JANELA")
    if window_title is None:
        print("\n\nListagem das Janelas da Redragon Abertas:\n\n")
        window_title = listar_janelas()
        print("\n\nFIM\n\n")

    open_redragon_app(path,window_title)

    #verificar_abrir_aplicativo(path)

    # Obter a janela pelo título
    window = get_window_by_title(window_title)

    if window:

        x_perfil,y_perfil,x_aplicar,y_aplicar = load_coordinates()
        # Coordenadas relativas dentro da janela (ajuste conforme necessário)
        

        # Salvar a posição atual do mouse
        mouse_x, mouse_y = pyautogui.position()

        try:
            # Automatizar ações na janela
            automate_actions(window, x_perfil, y_perfil, x_aplicar, y_aplicar)
        finally:
            # Restaurar a posição original do mouse
            pyautogui.moveTo(mouse_x, mouse_y)
            pyautogui.leftClick(mouse_x, mouse_y)
            print("\nPosição do mouse restaurada.")

            window.close()
            print("\nJanela do aplicativo da Redragon fechada")
