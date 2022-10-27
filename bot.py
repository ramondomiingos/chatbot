# -*- coding: utf-8 -*-
from typing import Dict
import  telepot
import string
bot = telepot.Bot("YOUR KEY")
import time
from telepot.loop import MessageLoop
response = bot.getUpdates()

def handle(msg: Dict):
    if(msg['chat']['type']=='supergroup'):
        chat_id= msg['chat']['id']
        command = msg['text']

    else:
        chat_id = msg['chat']['id']
        command = msg['text']
        nome = msg['chat']['first_name']
    command = string.replace(command, '@digiinforbot', '',1)
    print(command)
    if command == '/start':
           bot.sendMessage(chat_id, "Olá, agora as coisas vao iniciar!")
    elif command == '/test':
           bot.sendMessage(chat_id, "Apenas teste!!!!")
    elif command == 'ola' or command ==  '/ola':
           bot.sendMessage(chat_id, "Ola ,"+nome)
    elif command =='/help':
          bot.sendMessage(chat_id, "chame ramon e pergunte. /start /tijolada /test /help")
    elif command == '/tijolada':
          bot.sendMessage(chat_id, "Tijolinho, peninha e gotinha!")
    elif command == '/juciano':
          bot.sendMessage(chat_id, "Eeeeeee. Bits e Bytes!")
    elif command == '/crianzap':
          bot.sendMessage(chat_id, "Chupa meu pinto então...Seu VAGABUNDO.")
    elif command == '/ain':
          bot.sendMessage(chat_id, "Ain pai para...")
    elif command == '/joaozin':
          bot.sendMessage(chat_id, "oh heloisa...bom...show...uber...comprar")
    elif command == 'vou trabalhar!' or command == '/git':
          bot.sendMessage(chat_id, "https://i.imgur.com/HLQOYgm.gif")
    elif command == 'rosinha' or command == '/rosinha':
          bot.sendMessage(chat_id, "https://i.imgur.com/cIa6kcH.jpg")
    elif command == 'rosinho' or command == '/rosinho':
          bot.sendMessage(chat_id, "https://i.pinimg.com/originals/c6/0b/37/c60b372f6981564d693be3f99da534c2.jpg")
    elif command == 'cafe' or command == '/cafe':
          bot.sendMessage(chat_id, "EU QUERO CAFÉ")
    elif command == 'dadinho' or command == '/dadinho':
          bot.sendMessage(chat_id, "dadinho o caralho..meu nome agora e zé pequeno")
    elif command == 'taca' or command == '/taca':
          bot.sendMessage(chat_id, "vo tacar o piruuuuuuuuuuuu")
    elif command == 'yoda' or command == '/porra' or command == '/caralho' or command == '/bct':
        bot.sendMessage(chat_id, "ÉOQ?! Fale palavrão aqui nao!")
    elif command == 'endpoint' or command == '/endpoint':
        import random
        a = ['@ramondomiingos', '@hugo_dsilva', '@Tawan_SF']
        bot.sendMessage(chat_id, random.choice (a))
    elif command == 'ney' or command == '/ney':
          bot.sendMessage(chat_id, "http://conteudo.imguol.com.br/c/esporte/2013/06/17/17junho2013---neymar-faz-careta-em-treino-da-selecao-1371495702546_956x500.jpg")
    elif command == 'manual' or command == '/manual':
          bot.sendMessage(
                  chat_id,
                  """Comandos: 
                  /start
                  /test
                  /ola
                  /help
                  /tijolada
                  /juciano
                  /crianzap
                  /ain
                  /joaozin
                  /git
                  /rosinha
                  /rosinho
                  /cafe
                  /dadinho
                  /taca
                  /endpoint
                  """
          )
    else:
            bot.sendMessage(chat_id, "Send command '/help'")
MessageLoop(bot, handle).run_as_thread()
while 1:
      time.sleep(10)
