import telebot
from telebot import types
from workTOKEN import workTOKEN
import parse
import get_hash_name
import time

botTOKEN = workTOKEN

bot = telebot.TeleBot(botTOKEN)


def quality(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Factory New', callback_data='Factory New')
    item2 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    item3 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    item4 = types.InlineKeyboardButton('Well-Worn', callback_data='Well-Worn')
    item5 = types.InlineKeyboardButton('Battle-Scarred', callback_data='Battle-Scarred')
    markup.add(item1, item2, item3, item4, item5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def redline(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item2 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    item3 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    item4 = types.InlineKeyboardButton('Well-Worn', callback_data='Well-Worn')
    item5 = types.InlineKeyboardButton('Battle-Scarred', callback_data='Battle-Scarred')
    markup.add(item2, item3, item4, item5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def bloodsport(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Factory New', callback_data='Factory New')
    item2 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    item3 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    item4 = types.InlineKeyboardButton('Well-Worn', callback_data='Well-Worn')
    markup.add(item1, item2, item3, item4)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def greenlaminate(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Factory New', callback_data='Factory New')
    item2 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    item3 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    item4 = types.InlineKeyboardButton('Well-Worn', callback_data='Well-Worn')
    markup.add(item1, item2, item3, item4)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def hotrod(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Factory New', callback_data='Factory New')
    item2 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    markup.add(item1, item2)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def copperhead(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    item2 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    item3 = types.InlineKeyboardButton('Well-Worn', callback_data='Well-Worn')
    markup.add(item1, item2, item3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def jade(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Factory New', callback_data='Factory New')
    item2 = types.InlineKeyboardButton('Minimal wear', callback_data='Minimal wear')
    item3 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    markup.add(item1, item2, item3)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)


def darkwater(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Field-Tested', callback_data='Field-Tested')
    item2 = types.InlineKeyboardButton('Well-Worn', callback_data='Well-Worn')
    markup.add(item1, item2)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите качество', reply_markup=markup)