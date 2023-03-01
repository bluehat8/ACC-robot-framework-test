import socket
import getpass
import platform
import webbrowser



def get_system_info():
    # Obtener el nombre del host del PC
    hostname = socket.gethostname()

    # Obtener el nombre de usuario
    username = getpass.getuser()

    # Obtener la dirección IP del host
    ip_address = socket.gethostbyname(hostname)

    # Obtener el navegador y su versión
    browser = webbrowser.get()
    browser_name = browser.name
   # browser_version = browser.version

    # Obtener el sistema operativo y su versión
    operating_system = platform.system()
    operating_system_version = platform.release()

    # Devolver un diccionario con la información obtenida
    system_info = {
        "Hostname": hostname,
        "Username": username,
        "IP Address": ip_address,
        "Browser Name": browser_name,
        #"Browser Version": browser_version,
        "Operating System": operating_system,
        "Operating System Version": operating_system_version
    }
    return system_info


print(get_system_info())
