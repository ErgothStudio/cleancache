import os
import platform
import shutil
import datetime
import ctypes  # Import necessário para verificar permissões de administrador no Windows

def is_admin():
    """
    Verifica se o script está sendo executado com permissões de administrador.
    Funciona no Windows usando ctypes e ignora para outros sistemas.
    """
    if platform.system() == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    else:
        # No Linux/macOS, é comum verificar se o UID é zero
        try:
            return os.getuid() == 0
        except AttributeError:
            return False

def clear_browser_cache():
    """
    Limpa o cache dos navegadores conhecidos.
    """
    user_home = os.path.expanduser("~")
    cache_paths = {
        'chrome': os.path.join(user_home, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Cache'),
        'firefox': os.path.join(user_home, 'AppData', 'Local', 'Mozilla', 'Firefox', 'Profiles'),
        'edge': os.path.join(user_home, 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data', 'Default', 'Cache'),
        'opera': os.path.join(user_home, 'AppData', 'Local', 'Opera Software', 'Opera Stable', 'Cache'),
        'brave': os.path.join(user_home, 'AppData', 'Local', 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default', 'Cache')
    }

    for browser, path in cache_paths.items():
        if os.path.exists(path):
            try:
                for root, dirs, files in os.walk(path):
                    for f in files:
                        try:
                            os.remove(os.path.join(root, f))
                        except Exception as e:
                            print(f"Erro ao remover arquivo {f} no {browser}: {e}")
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d), ignore_errors=True)
                        except Exception as e:
                            print(f"Erro ao remover diretório {d} no {browser}: {e}")
                print(f"Cache do {browser.capitalize()} limpo com sucesso.")
            except PermissionError:
                print(f"Permissão negada para limpar o cache do {browser.capitalize()}.")
            except Exception as e:
                print(f"Erro ao limpar o cache do {browser.capitalize()}: {e}")
        else:
            print(f"Caminho de cache do {browser.capitalize()} não encontrado.")

def clear_temp_files(days_old=7):
    """
    Limpa arquivos e pastas temporárias do sistema com mais de 'days_old' dias.
    """
    system_platform = platform.system()
    user_home = os.path.expanduser("~")
    
    if system_platform == "Windows":
        temp_path = os.path.join(user_home, 'AppData', 'Local', 'Temp')
    elif system_platform == "Linux":
        temp_path = "/tmp"
    elif system_platform == "Darwin":  # macOS
        temp_path = "/private/tmp"
    else:
        print("Sistema operacional não suportado.")
        return

    now = datetime.datetime.now()
    for root, dirs, files in os.walk(temp_path):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                if os.path.isfile(file_path) and (now - datetime.datetime.fromtimestamp(os.path.getmtime(file_path))).days >= days_old:
                    os.remove(file_path)
                    print(f"Arquivo temporário removido: {file_path}")
            except PermissionError:
                print(f"Permissão negada para remover o arquivo: {file_path}")
            except Exception as e:
                print(f"Erro ao remover arquivo temporário {file_path}: {e}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                if (now - datetime.datetime.fromtimestamp(os.path.getmtime(dir_path))).days >= days_old:
                    shutil.rmtree(dir_path, ignore_errors=True)
                    print(f"Pasta temporária removida: {dir_path}")
            except Exception as e:
                print(f"Erro ao remover pasta temporária {dir_path}: {e}")

def reset_network_settings():
    """
    Reseta as configurações de rede, incluindo cache DNS e reinicia o adaptador de rede.
    """
    system_platform = platform.system()
    
    try:
        if system_platform == "Windows":
            os.system("ipconfig /flushdns")
            os.system("ipconfig /release")
            os.system("ipconfig /renew")
            print("Configurações de rede do Windows foram redefinidas.")
        
        elif system_platform == "Linux":
            os.system("sudo systemctl restart NetworkManager")
            os.system("sudo systemd-resolve --flush-caches")
            print("Configurações de rede do Linux foram redefinidas.")
        
        elif system_platform == "Darwin":  # macOS
            os.system("sudo dscacheutil -flushcache")
            os.system("sudo killall -HUP mDNSResponder")
            print("Configurações de rede do macOS foram redefinidas.")
        else:
            print("Sistema operacional não suportado.")
    except Exception as e:
        print(f"Erro ao redefinir configurações de rede: {e}")

if __name__ == "__main__":
    # Exibe ASCII Art antes de iniciar o processo
    print("""
██████╗ ███╗   ███╗ █████╗ ██████╗ ██╗ ██████╗ 
██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║██╔═══██╗
██║  ██║██╔████╔██║███████║██████╔╝██║██║   ██║
██║  ██║██║╚██╔╝██║██╔══██║██╔══██╗██║██║   ██║
██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║██║╚██████╔╝
╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
                                               
    """)

    # Descrição do que o script fará
    print("O script realizará as seguintes ações de limpeza e redefinição:")
    print("1. Limpeza do cache dos navegadores Chrome, Firefox, Edge, Opera e Brave.")
    print("2. Limpeza de arquivos temporários do sistema com mais de 7 dias.")
    print("3. Redefinição das configurações de rede (flush DNS e renovação do adaptador de rede).")
    
    # Confirmação do usuário
    confirm = input("\nVocê tem certeza que deseja iniciar o processo de limpeza? (Y/N): ").strip().lower()
    if confirm != 'y':
        print("Processo de limpeza cancelado.")
        exit()

    if not is_admin():
        print("O script requer permissões de administrador para ser executado corretamente.")
        exit()

    print("Iniciando limpeza de cache do navegador, arquivos temporários e redefinição de rede.")
    clear_browser_cache()
    clear_temp_files(days_old=7)
    reset_network_settings()
    print("Processo concluído.")
