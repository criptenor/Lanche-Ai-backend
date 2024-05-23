import qrcode
import datetime
import base64
import json
from os.path import exists

def get_name():
    date = str(datetime.datetime.now())
    b64 = base64.b64encode(date.encode()).decode()
    name = ((b64.replace('=', '')) + '.png').lower()
    return name

def get_credentials():
    if exists('./credentials.json'):
        f = open('credentials.json')
        cred = json.load(f)
        return cred

def verify_credentials():
    if not exists('./credentials.json'):
        with open('credentials.json', 'w') as f:
            json.dump({"public_key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9kdHNheHhzaHh6ZGF0YXZ6ZnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE0OTYzNDMsImV4cCI6MjAyNzA3MjM0M30.04XvHLUvjkIdsmu5keJGbUL88DAp97H5bE_a06DdpW4", "access_token": "YOUR_ACCESS_TOKEN_HERE"}, f, indent=2)
            print("Configure suas credenciais no arquivo credentials.json")
            exit()
    if exists('./credentials.json'):
        l = open('./credentials.json')
        data = json.load(l)
        if 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9kdHNheHhzaHh6ZGF0YXZ6ZnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE0OTYzNDMsImV4cCI6MjAyNzA3MjM0M30.04XvHLUvjkIdsmu5keJGbUL88DAp97H5bE_a06DdpW4' in data['public_key'] or 'YOUR_ACCESS_TOKEN_HERE' in data['access_token']:
            print('Configure suas credenciais no arquivo credentials.json')
            exit()