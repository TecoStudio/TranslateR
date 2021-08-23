import requests
from mcdreforged.api.all import *

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'


def help_message(source: CommandSource, context: dict):
    source.reply('You can type "!!t" to translated text')


def translate(source: CommandSource, context: dict):
    data = {
        'i': context['text'],
        'doctype': 'json',
    }
    response = requests.post(url, data=data)
    res_data = response.json()
    source.get_server().say(res_data['translateResult'][0][0]['tgt'])


def on_load(server: PluginServerInterface, old):
    server.register_help_message('!!t', 'You can type "!!t" to translated text')
    server.register_command(
        Literal('!!t').runs(help_message).on_error(UnknownArgument, help_message).
            then(GreedyText('text').runs(translate))
    )

