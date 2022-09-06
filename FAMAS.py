import telebot
from telebot import types
from workTOKEN import workTOKEN

botTOKEN = workTOKEN

bot = telebot.TeleBot(botTOKEN)

name = ''


def famas(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('FAMAS | Истребитель', callback_data='FAMAS | Spitfire')
    item2 = types.InlineKeyboardButton('FAMAS | Остаточное изображение', callback_data='FAMAS | Afterimage')
    item3 = types.InlineKeyboardButton('FAMAS | Заход солнца', callback_data='FAMAS | Sundown')
    item4 = types.InlineKeyboardButton('FAMAS | Контрастные цвета', callback_data='FAMAS | Contrast Spray')
    item5 = types.InlineKeyboardButton('FAMAS | Теория чисел', callback_data='FAMAS | Prime Conspiracy')
    item6 = types.InlineKeyboardButton('FAMAS | Дань уважения', callback_data='FAMAS | Commemoration')
    item7 = types.InlineKeyboardButton('FAMAS | Защитный каркас', callback_data='FAMAS | Roll Cage')
    item8 = types.InlineKeyboardButton('FAMAS | Авария', callback_data='FAMAS | Meltdown')
    item9 = types.InlineKeyboardButton('FAMAS | Глаз Афины', callback_data='FAMAS | Eye of Athena')
    item10 = types.InlineKeyboardButton('FAMAS | Джинн', callback_data='FAMAS | Djinn')
    item11 = types.InlineKeyboardButton('FAMAS | Механо-пушка', callback_data='FAMAS | Mecha Industries')
    item12 = types.InlineKeyboardButton('FAMAS | Стикс', callback_data='FAMAS | Styx')
    item13 = types.InlineKeyboardButton('FAMAS | Пульс', callback_data='FAMAS | Pulse')
    item14 = types.InlineKeyboardButton('FAMAS | Тёмная вода', callback_data='FAMAS | Dark Water')
    item15 = types.InlineKeyboardButton('FAMAS | ZX Spectron', callback_data='FAMAS | ZX Spectron')
    item16 = types.InlineKeyboardButton('FAMAS | Валентность', callback_data='FAMAS | Valence')
    item17 = types.InlineKeyboardButton('FAMAS | Сержант', callback_data='FAMAS | Sergeant')
    item18 = types.InlineKeyboardButton('FAMAS | Гексан', callback_data='FAMAS | Hexane')
    item19 = types.InlineKeyboardButton('FAMAS | Смертенок', callback_data='FAMAS | Doomkitty')
    item20 = types.InlineKeyboardButton('FAMAS | Ночной Борре', callback_data='FAMAS | Night Borre')
    item21 = types.InlineKeyboardButton('FAMAS | Meow 36', callback_data='FAMAS | Meow 36')
    item22 = types.InlineKeyboardButton('FAMAS | Нейронная сеть', callback_data='FAMAS | Neural Net')
    item23 = types.InlineKeyboardButton('FAMAS | Макабр', callback_data='FAMAS | Macabre')
    item24 = types.InlineKeyboardButton('FAMAS | Голубые брызги', callback_data='FAMAS | Cyanospatter')
    item25 = types.InlineKeyboardButton('FAMAS | Демонтаж', callback_data='FAMAS | Teardown')
    item26 = types.InlineKeyboardButton('FAMAS | Резерв', callback_data='FAMAS | Decommissioned')
    item27 = types.InlineKeyboardButton('FAMAS | Калифорнийский камуфляж', callback_data='FAMAS | CaliCamo')
    item28 = types.InlineKeyboardButton('FAMAS | Защитная окраска', callback_data='FAMAS | Crypsis')
    item29 = types.InlineKeyboardButton('FAMAS | Выживший', callback_data='FAMAS | Survivor Z')
    item30 = types.InlineKeyboardButton('FAMAS | Дефект проводки', callback_data='FAMAS | Faulty Wiring')
    item31 = types.InlineKeyboardButton('FAMAS | Колония', callback_data='FAMAS | Colony')

    markup.add(item1, item2, item3, item4, item5,
               item6, item7, item8, item9, item10,
               item11, item12, item13, item14, item15,
               item16, item17, item18, item19, item20,
               item21, item22, item23, item24, item25,
               item26, item27, item28, item29, item30,
               item31, )

    bot.send_message(message.chat.id, 'Выберите скин', reply_markup=markup)
