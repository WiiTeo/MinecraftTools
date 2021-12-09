import os
import sys
import requests

# By WiiTeo

# MinecraftTools is based in minecraft-api.com

def get_uuid(pseudo):
    # https://minecraft-api.com/api/uuid/{pseudo}
    url = "https://minecraft-api.com/api/uuid/"
    pseudo_du_mec = pseudo
    curl = url + pseudo_du_mec
    r = requests.get(curl, allow_redirects=True)
    print(r.content)

def get_pseudo(uuid):
    # https://minecraft-api.com/api/pseudo/{uuid}
    url = "https://minecraft-api.com/api/pseudo/"
    uuid_du_mec = uuid
    curl = url + uuid_du_mec
    r = requests.get(curl, allow_redirects=True)
    print(r.content)

def get_server_info(ip, port):
    # https://minecraft-api.com/api/ping/{ip}/{port}
    url = "https://minecraft-api.com/api/ping/"
    ip_du_serveur = ip
    port_du_serveur = port
    curl = f"{url}{ip}/{port}"
    r = requests.get(curl, allow_redirects=True)
    print(r.content)

def get_server_status(ip, port):
    # https://minecraft-api.com/api/ping/status/{ip}/{port}
    url = "https://minecraft-api.com/api/ping/status/"
    curl = url + ip + "/" + port
    r = requests.get(curl, allow_redirects=True)
    print(r.content)