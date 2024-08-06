# Redragon Keyboard Profile Switcher

O código presente neste repositório apresenta um seletor de perfis para teclados da Redragon. Este seletor é apresentado na forma de um ícone na bandeja do sistema em Windows.


## Instalação

Para instalar, siga os passos abaixo:

1. Realize o clone do repositório no diretório desejado:

    ```sh
    git clone https://github.com/gabrielmrp/redragon-keyboard-profile-switcher.git
    ```

2. Execute o arquivo que constrói o ambiente e instala os pacotes necessários para a execução da aplicação:

    ```sh
    create_venv.bat
    ```

3. Acesse o arquivo `ref.env` e altere as informações pertinentes:
    - **Título da janela:** Verifique na pasta Arquivos de Programas (x86) qual nome de pasta faz referência ao teclado e copie esse valor.
    - **Caminho aplicação:** Insira o caminho da pasta previamente citada.
    - **Caminho base:** Insira o caminho da aplicação clonada.

4. Salve esse arquivo como ".env"

## Uso

1. Execute o arquivo `call_pos.bat` e siga as instruções do terminal para capturar as posições dos botões do aplicativo Redragon: Perfil 1, Perfil 2, Perfil 3 e Aplicar.

2. Execute o arquivo `seletor_perfis_teclado_redragon_debug.bat` e verifique se um ícone contendo dois retângulos centralizados apareceu na bandeja. Se tudo estiver certo você poderá passar a executar o arquivo `seletor_perfis_teclado_redragon.bat` que mantém o terminal aberto.

3. Clique com o botão esquerdo no ícone e selecione o perfil que deseja aplicar.

4. Clique em “Sair” no ícone para sair da aplicação.

## Especificações

- **Teclado:** Redragon Ashe
- **Sistema Operacional:** Windows 11
- **Python:** 3.9.13

## Importante
Não movimentar o mouse enquanto o aplicativo estiver alternando o perfil para evitar situações indesejadas 

---

### English Version

## Redragon Keyboard Profile Switcher

The code in this repository presents a profile selector for Redragon keyboards. This selector is displayed as an icon in the Windows system tray.


## Installation

To install, follow these steps:

1. Clone the repository to the desired directory:

    ```sh
    git clone https://github.com/gabrielmrp/redragon-keyboard-profile-switcher.git
    ```

2. Run the script that sets up the environment and installs the necessary packages for the application:

    ```sh
    create_venv.bat
    ```

3. Access the `ref.env` file and update the relevant information:
    - **Window Title:** Check in the Program Files (x86) folder for the folder name that references the keyboard and copy that value.
    - **Application Path:** Enter the path to the previously mentioned folder.
    - **Base Path:** Enter the path to the cloned application.

## Usage

4. Run the `call_pos.bat` script and follow the terminal instructions to capture the positions of the Redragon app buttons: Profile 1, Profile 2, Profile 3, and Apply.

2. Run the `seletor_perfis_teclado_redragon_debug.bat` script and check if an icon with two centered rectangles appeared in the tray. If it works you can execute the  `seletor_perfis_teclado_redragon.bat` file that imediatly closes the terminal.

3. Left-click on the icon and select the profile you want to apply.

4. Click "Exit" on the icon to exit the application.

## Specifications

- **Keyboard:** Redragon Ashe
- **Operating System:** Windows 11
- **Python:** 3.9.13

## Importante
Do not move the mouse when the app is in the profile switch process in order to avoid unwanted behaviours.
