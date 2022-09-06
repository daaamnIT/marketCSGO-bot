import telebot
from telebot import types

from AUGS import augs
from FAMAS import famas
from backhandler import backhandler
from workTOKEN import workTOKEN
import parse
import get_hash_name
import time
from qual_markups import quality, redline, bloodsport, greenlaminate, hotrod, copperhead, jade, darkwater
from akas import aks
from backhandler import backhandler

botTOKEN = workTOKEN

bot = telebot.TeleBot(botTOKEN)

name = ''


def basenameformatter(call):
	name = ''
	name += call.data
	return name


def getinfo(call):
	print(name)
	hash_name = get_hash_name.get_hash_name(name)
	data = parse.main(hash_name)
	if name == ' (Factory New)' or name == ' (Minimal wear)' or name == ' (Field-Tested)' or name == ' (Well-Worn)' or name == ' (Battle-Scarred)':
		bot.send_message(chat_id=call.message.chat.id, text="Кажется вы выбрали качество, но не выбрали скин. Пожалуйста, выберите скин")
	else:
		if len(data) == 0:
			bot.send_message(chat_id=call.message.chat.id, text="Кажется скин в этом качестве сейчас не продается. Попробуйте другое качество")

		else:
			for i in range(3):
				bot.send_message(chat_id=call.message.chat.id, text="Price: " + str(data[i]['price'] / 100) + "  |  Float: " + str(data[i]['extra']['float']))
				bot.send_message(chat_id=call.message.chat.id, text="URL: " + parse.get_url(data[i]))


def mainMarkup(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Assault Rifles')
	item2 = types.KeyboardButton('Sniper Rifles')
	item3 = types.KeyboardButton('Knives')
	item4 = types.KeyboardButton('Gloves')
	item5 = types.KeyboardButton('Pistols')
	item6 = types.KeyboardButton('SMGs')
	item7 = types.KeyboardButton('Shotguns')
	item8 = types.KeyboardButton('Machine guns')
	item9 = types.KeyboardButton('Keys - in Future')
	item10 = types.KeyboardButton('Other - in Future')
	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, )
	return markup


def mainMenu(message):
	markup = mainMarkup(message)
	bot.send_message(message.chat.id, 'Выберите тип оружия', reply_markup=markup)


def assualt_rifles(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('AK')
	item2 = types.KeyboardButton('AUG')
	item3 = types.KeyboardButton('FAMAS')
	item4 = types.KeyboardButton('Galil AR')
	item5 = types.KeyboardButton('M4A4')
	item6 = types.KeyboardButton('M4A1-S')
	item7 = types.KeyboardButton('SG553')
	item8 = types.KeyboardButton('Back to menu')
	markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
	bot.send_message(message.chat.id, 'Выберите винтовку'.format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
	markup = mainMarkup(message)
	bot.send_message(message.chat.id, 'Привет, {0.first_name}! Этот бот создан для подбора скинов на сайте market.csgo.com'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
	time.sleep(0.5)
	if message.text == "Sniper Rifles":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('AWP')
		item2 = types.KeyboardButton('Back to menu')
		markup.add(item1, item2)
		bot.send_message(message.chat.id, 'Выберите снайперскую винтовку'.format(message.from_user), reply_markup=markup)

	if message.text == "Assault Rifles":
		assualt_rifles(message)

	if message.text == "AK":
		aks(message)

	if message.text == "AUG":
		augs(message)

	if message.text == "FAMAS":
		famas(message)

	elif message.text == 'Back to menu':
		mainMenu(message)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
	global name
	if call.message:
		backhandler(call)


bot.polling(none_stop=True, interval=0)
