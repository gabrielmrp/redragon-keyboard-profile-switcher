import os
import subprocess
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item
from dotenv import load_dotenv
import concurrent.futures

def create_image(width, height, top_color, bottom_color, background_color):
    """Cria uma imagem com um grande retângulo vermelho no topo e um pequeno retângulo na parte inferior."""
    image = Image.new('RGBA', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Desenha o retângulo grande no topo
    top_rect_height = height // 3
    top_rect_width = width 
    top_rect_y = height // 4
    draw.rectangle([0, top_rect_y, top_rect_width, top_rect_y + top_rect_height], fill=top_color)
    
    # Desenha o retângulo pequeno na parte inferior
    bottom_rect_width = width // 2
    bottom_rect_height = height // 4
    bottom_rect_x = (width - bottom_rect_width) // 2
    bottom_rect_y = height - bottom_rect_height - 10
    draw.rectangle([bottom_rect_x, bottom_rect_y, bottom_rect_x + bottom_rect_width, bottom_rect_y + bottom_rect_height], fill=bottom_color)
    
    return image

def run_profile_script(profile_number):
    """Executa o script associado ao perfil selecionado."""
    load_dotenv()  # Carrega variáveis de ambiente, se necessário
    
    # Formata o caminho do arquivo .bat
    bat_file = f"activate_profile_{profile_number}.bat"
    path = os.path.join(os.getenv('CAMINHO_BASE', ''), bat_file)
    
    if not os.path.isfile(path):
        print(f"O arquivo {path} não foi encontrado.")
        return
    
    command = [path]
    
    try:
        # Executa o comando e aguarda a conclusão
        print(f"Executando: {' '.join(command)}")
        subprocess.run(command, shell=True, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
    except MemoryError:
        print("Erro de memória ao executar o comando.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def on_clicked(icon, item):
    """Manipula cliques no ícone da bandeja."""
    if item.text.startswith("Perfil"):
        profile_number = item.text.split()[-1]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(run_profile_script, profile_number)
    elif item.text == "Sair":
        icon.stop()

def main():
    """Configura e executa o ícone da bandeja do sistema."""

    width, height = 300, 150
    top_color = 'red'
    bottom_color = 'red'
     # Transparente
    background_color = (0, 0, 0, 0) 

    # Cria e salva a imagem
    image = create_image(width, height, top_color, bottom_color, background_color)
    image.save('tray_icon.png')

    # Define o menu da bandeja
    menu = (item('Perfil 1', on_clicked),
            item('Perfil 2', on_clicked),
            item('Perfil 3', on_clicked),
            item('Sair', on_clicked))

    # Cria o ícone da bandeja
    icon = pystray.Icon("perfil_seletor", image, "Seletor de Perfil REDRAGON", menu)

    # Executa o ícone da bandeja
    icon.run()

if __name__ == "__main__":
    main()
