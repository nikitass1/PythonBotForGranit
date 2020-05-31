import telebot
import schedule
import time
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('TOKEN')



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, меня зовут Бот Результатор и я буду говорить пришли результаты олимпиады Гранит науки или нет	 =)")
	message1 = "Чтобы узнать пришли ли резы:\nпо информатике -- отправь /result_gr_inf\nпо естественных наукам -- " \
               "отправь /result_gr_ns\nпо химии -- отправь /result_gr_ch"
	bot.send_message(message.chat.id, message1)

@bot.message_handler(commands=['result_gr_ns'])
def echo_all(message):
    #2020
    url = "http://ogn.spmi.ru/metodicheskie-ukazaniya-2"
    # 2019 url = "http://ogn.spmi.ru/metodicheskie-ukazaniya"
    flag = False
    page = requests.get(url).text

    soup = BeautifulSoup(page, features="html.parser")
    h4s = soup.find_all('h4')
    for h4 in h4s:
        try:
            h4_titile = h4.find('a').text
        except AttributeError:
            h4_titile = ""
        text1 = "Ответы на билеты "
        if text1 in h4_titile:
            flag = True

    if flag:
        text11 = "Результаты пришли!!!"
    else:
        text11 = "Результатов пока нет!!!"

    bot.reply_to(message, text11)

@bot.message_handler(commands=['result_gr_inf'])
def echo_all(message):
    #2020
    url = "http://ogn.spmi.ru/rezultaty-1"
    #2019 url = "http://ogn.spmi.ru/metodicheskie-ukazaniya-0"
    flag = False
    page = requests.get(url).text

    soup = BeautifulSoup(page, features="html.parser")
    strongs = soup.find_all('strong')
    for strong in strongs:
        strong_title = strong.find('strong').text
        print(strong_title)
        text1 = "РЕЗУЛЬТАТЫ ОЛИМПИАДЫ"
        if text1 in strong_title:
            flag = True

    if flag:
        text11 = "Результаты пришли!!!"
    else:
        text11 = "Результатов пока нет!!!"

    bot.reply_to(message, text11)

@bot.message_handler(commands=['result_gr_ch'])
def echo_all(message):
    #2020
    url = "http://ogn.spmi.ru/metodicheskie-ukazaniya-3"
    #2019
    #url = "http://ogn.spmi.ru/metodicheskie-ukazaniya-1"
    flag = False
    page = requests.get(url).text

    soup = BeautifulSoup(page, features="html.parser")
    h4s = soup.find_all('h4')
    for h4 in h4s:
        try:
            h4_titile = h4.find('a').text
        except AttributeError:
            h4_titile = ""
        text1 = "Ответы на билеты "
        if text1 in h4_titile:
            flag = True

    if flag:
        text11 = "Результаты пришли!!!"
    else:
        text11 = "Результатов пока нет!!!"

    bot.reply_to(message, text11)


@bot.message_handler(commands=['gde'])
def res(message):
    textt = "ГДЕ РЕЗЫ БЛЯТЬ"
    bot.send_message(message.chat.id, textt)
bot.polling()

