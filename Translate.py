# coding: utf-8

import requests
from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'translate',
    'version': '1.0.1',
    'name': 'TranslateR',
    'description': 'You can type "!!t" to translated text',
    'author': [
        'Spanner_Jun'
    ],
    'link': 'https://github.com/Minecraft-TecoCraft-server/TranslateR',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'


def on_user_info(server: ServerInterface, info: Info):
    i = info.content
    if '!!t' in i:
        i = i.replace("!!t ", "", 1)
        data = {
            'i': i,
            'doctype': 'json',
        }
        response = requests.post(url, data=data)
        res_data = response.json()
        server.say(res_data['translateResult'][0][0]['tgt'])
