import os
import json
import time
import warnings
from dotenv import load_dotenv
import subprocess
import pyautogui
from pynput import mouse

from funcs import get_window_by_title, list_windows,open_redragon_app
from funcs import put_window_on_lefttop_position


# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pywinauto')

click_count = 0
positions = {}


def write_dict_to_env_file( env_dict):
    with open('config.json', 'w', encoding='utf-8') as file:
        file.write( json.dumps(env_dict))


# Função para capturar a posição do mouse quando o botão direito é clicado
def on_click(x, y, button, pressed):
    global click_count

    if click_count < 3:
        print("\nClique com o botão direito na janela do software da Redragon ")
        print(f"correspondente ao perfil {click_count + 1}")
    elif click_count == 3:
        print("\nClique com o botão direito na janela do software da Redragon ")
        print("correspondente a Aplicar")
    elif click_count == 4:
        print("\nClique na tela com o botão direito para finalizar")

    if pressed and button == mouse.Button.right:

        if click_count < 3:
            tipo = f'perfil{click_count + 1}'
            positions[f'PERFIL{click_count + 1}_X']=x
            positions[f'PERFIL{click_count + 1}_Y']=y
        else:
            tipo = 'aplicar'
            positions['APLICAR_X']=x
            positions['APLICAR_Y']=y

        click_count += 1
        if click_count <= 4:
            print(f"Coordenadas capturadas para {tipo}: x={x}, y={y}")

        # Captura a tela na área onde o clique ocorreu
        screenshot = pyautogui.screenshot(region=(x - 50, y - 20, 100, 40))
        # Ajuste o tamanho do retângulo conforme necessário


        screenshot.save(f'imagens/{tipo}.png')
        write_dict_to_env_file(positions)

def main():

    global click_count
    click_count = 0
    # Caminho do executável

    load_dotenv()
    # Caminho do executável
    path = os.getenv("CAMINHO_APLICAÇÃO")+"KeyboardDrv.exe"
    title = os.getenv("TÍTULO_JANELA")

    subprocess.Popen(path)
    
    open_redragon_app(path,title)

    if title is None:
        print("\n\nListagem das Janelas da Redragon Abertas:\n\n")
        title = list_windows()
        print("\n\nFIM\n\n")


    # Obter a janela pelo título
    window = get_window_by_title(title)

    put_window_on_lefttop_position(window)

    if window:
        print("Clique na tela com o botão direito para capturar as coordenadas.")
        print("\nClique com o botão direito na janela do software da Redragon ")
        print(f"correspondente ao Perfil {click_count + 1}")


        with mouse.Listener(on_click=on_click):
            while click_count <=4:
                pass

        print("Posições capturadas, confira a captura na pasta 'imagens'")
        print("Posteriormente, execute o arquivo 'seletor_perfis_teclado_redragon.bat'")

if __name__ == "__main__":
    main()
