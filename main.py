import requests
from pyngrok import ngrok
import socket
import colorama
import os

ngrok_token = input('Ngrok token: ')
username = input('NoIP Username: ')
password = input('NoIP Password: ')
host = input('NoIP Host: ')

colorama.init(autoreset=True)

localip = socket.gethostbyname(socket.gethostname())
os.system('cls' if os.name=='nt' else 'clear')
print('Local IP:')
print(colorama.Fore.RED+localip)

ngrok.set_auth_token(ngrok_token)
ip = ngrok.connect().public_url[7:]

os.system('cls' if os.name=='nt' else 'clear')
print('Ngrok IP:')
print(colorama.Fore.YELLOW+ip)

DDNS = noip_api.noip(host)
DDNS.login(username=username, password=password)
DDNS.setDNS(ip=ip)

os.system('cls' if os.name=='nt' else 'clear')
print('Public IP:')
print(colorama.Fore.GREEN+host)

while True:
    pass
