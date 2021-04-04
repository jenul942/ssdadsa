import telebot
import requests
import time
from bs4 import BeautifulSoup

api = "1624994495:AAEMBjyt6k7eT5KoSgiB70nexk0OnBA5O_I"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=["start", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello New guy this is the covid-19 stats bot type /details")

@bot.message_handler(commands=["help", "hlp", "feedback"])
def hello(message):
    bot.send_message(message.chat.id, "Any feedback @JenulRanthisa")

@bot.message_handler(commands=['details'])
def details(message):
  page = requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
  after_bs = BeautifulSoup(page.content, 'html.parser')
  find_data = after_bs.find_all(id="maincounter-wrap")
  output = ''
  for x in find_data:
  	  # print(x.text)
  	  output = output + x.text
  
  bot.reply_to(message, output)

while True:
    try:
        bot.polling()
    except:
        time.sleep(5)