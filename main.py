# -- LIBRARIES --
import os
try:
    import requests
    from pyngrok import ngrok
    from noip_api import noip_api
    import socket
    import colorama
except:
    for i in ['pyngrok', 'noip-api-CodeGuy3',
            'colorama', 'socket', 'requests']:
        os.system('python -m pip install '+i)
    os.system('python '+__file__)
# -- LIBRARIES --


# -- SETTINGS --
ngrok_token = input('Ngrok token: ')
proto = input('Ngrok Protocol: ')
username = input('NoIP Username: ')
password = input('NoIP Password: ')
host = input('NoIP Host: ')
# -- SETTINGS --


colorama.init(autoreset=True)
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


# -- LOCAL --
localip = socket.gethostbyname(socket.gethostname())

clear()
print('Local IP:')
print(colorama.Fore.RED+localip)
# -- LOCAL --


# -- NGROK --
ngrok.set_auth_token(ngrok_token)
try:
    ngrok.disconnect(get_tunnels()[0].public_url)
except:
    pass
objip = ngrok.connect(25565, proto, bind_tls=True)
ip = objip.public_url[8:]
ipFromHost = socket.gethostbyname(ip)

clear()
print('Ngrok IP:')
print(colorama.Fore.YELLOW+ipFromHost)
# -- NGROK --


# -- NOIP --
DDNS = noip_api.noip(host)
DDNS.login(username, password)
DDNS.setDNS(ipFromHost)

clear()
print('Public IP:')
print(colorama.Fore.GREEN+host)
# -- NOIP --


while True:
    pass
