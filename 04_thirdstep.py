#!/usr/bin/env python3

import json

with open('prooven_proxies_yt.dat', 'r') as file:
    lines = file.readlines()

colors = [
    "#FFFF00",  # желтый
    "#FF0000",  # красный
    "#008000",  # зеленый
    "#0000FF",  # синий
    "#FFD700",  # золотой
    "#FFA500",  # оранжевый
    '#00FF00',  # классический чистый зеленый
    "#FF00FF"   # магента
]

data = []
for i,line in enumerate(lines):
 if len(line)>0:
    proxy_info = line.strip().split('://')
    hostname, port = proxy_info[1].split(':')
    data.append({
        "active": True,
        "title": line.strip(),
        "type": proxy_info[0],
        "hostname": hostname,
        "port": port,
        "username": "",
        "password": "",
        "cc": "NN",
        "city": "Unknown",
        "color": colors[i%len(colors)],
        "pac": "",
        "pacString": "",
        "proxyDNS": True,
        "include": [],
        "exclude": []
    })

json_data = {
    "mode": "disable",
    "sync": False,
    "autoBackup": False,
    "passthrough": "",
    "theme": "moonlight",
    "container": {
        "incognito": "",
        "container-1": "",
        "container-2": "",
        "container-3": "",
        "container-4": ""
    },
    "commands": {
        "setProxy": "",
        "setTabProxy": "",
        "quickAdd": ""
    },
    "data": data
}

with open('prooven_proxies_yt.json', 'w') as file:
    json.dump(json_data, file, indent=4)



