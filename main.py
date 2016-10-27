#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json, os
from time import sleep
import sys
import re
import urllib
import methods as bot
reload(sys)
sys.setdefaultencoding("utf-8")
"""
handler message              _____'_____
start & copy right negative / super team\ MIT
                           |______'______|
"""
def run ():
    last_update = 0
    while True:
        get_updates = bot.getUpdates()
        for update in get_updates['result']:
            if last_update < update['update_id']:
                last_update = update['update_id']
                if 'message' in update or 'text' in update:
                    try:
                        chat_id = update['message']['chat']['id']
                        text = update['message']['text']
                        message = update['message']
                        command = text
                        if(command == '/start' or command == '/help'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            key = json.dumps(
                            {'inline_keyboard':[[
                            {'text':'Developer 👓','url':'https://telegram.me/DevToP'},
                            {'text':'team 🔌','url':'https://telegram.me/devtop'}
                            ],
                            [
                            {'text':'Your Info 🕶','url':'https://telegram.me/Pythoneinfobot'}
                            ],
                            [
                            {'text':'my dev','url':'https://telegram.me/ahmedjabbar1'}
                            ]
                            ]
                            })
                            bot.send_msg(chat_id,'<b>help sudo Development</b>\ncommands : \n/about\n/info',reply_markup=key)
                        if(command == '/frends' or command == '/team'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            key = json.dumps(
                            {'inline_keyboard':[[
                            {'text':'bot Dev','url':'https://telegram.me/Ahmedjabbar1'},
                            {'text':'Ch dev',url':'https://telegram.me/p444p'}
                            ],
                            [
                            {'text':'channel','url':'https://telegram.me/DevToP'}
                            ],
                            [
                            {'text':'Dev','url':'https://telegram.me/ahmedjabbar1}
                            ]
                            ]
                            })
                            bot.send_msg(chat_id,'<b>this is my frends</b>',reply_markup=key)
                        if(command == '/time'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            time = urllib.urlopen('http://api.gpmod.ir/time/').read()
                            data = json.loads(time)
                            en = data['ENtime']
                            msgg = '<b>Time iraq :</b> {}'.format(en)
                            bot.send_msg(chat_id,msgg,reply_to_message_id=update['message']['message_id'])
                        if(command == '/about'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'upload_photo')
                            markup = json.dumps({
                            'inline_keyboard':[
                            [
                            {'text':'👇 DeVToP 👇','callback_data':'1'}
                            ],
                            [
                            {'text':'Developer 🕶','url':'https://telegram.me/ahmedjabbar1'},
                            {'text':'Channel','url':'https://telegram.me/DevToP'}
                            ]
                            ]
                            })
                            bot.send_photo(chat_id,open('photo_2016-10-14_17-31-55.jpg'),caption='ch @DevToP',reply_markup=markup)
                        if(command == '/info' or command == '/start info'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            user_id = update['message']['from']['id']
                            username = update['message']['from']['username']
                            s = bot.getUserProfilePhotos(update['message']['from']['id'])
                            markup = json.dumps(
                            {
                            'inline_keyboard':[
                            [
                            {'text':'{}'.format(username),'url':'https://telegram.me/{}'.format(username)}
                            ]
                            ]
                            }
                            )
                            bot.send_photo_file_id(chat_id,photo=s['result']['photos'][0][2]['file_id'],caption='🔺- ID : {}\n🔺- Username : @{}\n🔺- ch :  @DevToP'.format(user_id,username),reply_markup=markup)
                        if(command == '/type'):
                            if(update['message']['reply_to_message']['entities'][0]['type']):
                                msg = update['message']['reply_to_message']['entities'][0]['type']
                                bot.send_msg(chat_id,'<b>{}</b>'.format(msg))
                    except KeyError:
                        print 'error'

run()

