import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def abrir_chrome():
    # Caminho para o perfil padrão do Chrome (usuário logado no Windows)
    user_data_dir = os.path.expanduser(r"~\\AppData\\Local\\Google\\Chrome\\User Data")

    # Opções do Chrome
    options = Options()
    options.add_argument("--start-maximized")        # Abrir em tela cheia
    options.add_argument("--disable-blink-features=AutomationControlled")  # Reduz chance de bloqueio
    options.add_argument(f"--user-data-dir={user_data_dir}")         # (opcional) usar perfil real

    # Iniciar driver com interface
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def carregar_csv():
    pass

def lancar_notas():
    pass