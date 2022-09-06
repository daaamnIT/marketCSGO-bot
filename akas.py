import telebot
from telebot import types
from workTOKEN import workTOKEN

botTOKEN = workTOKEN

bot = telebot.TeleBot(botTOKEN)

name = ''


def aks(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('AK-47 | Дикий лотос', callback_data='AK-47 | Wild Lotus')
    item2 = types.InlineKeyboardButton('AK-47 | Огненный змей', callback_data='AK-47 | Fire Serpent')
    item3 = types.InlineKeyboardButton('AK-47 | Рентген', callback_data='AK-47 | X-Ray')
    item4 = types.InlineKeyboardButton('AK-47 | Золотая арабеска', callback_data='AK-47 | Gold Arabesque')
    item5 = types.InlineKeyboardButton('AK-47 | Гидропоника', callback_data='AK-47 | Hydroponic')
    item6 = types.InlineKeyboardButton('AK-47 | Вулкан', callback_data='AK-47 | Vulcan')
    item7 = types.InlineKeyboardButton('AK-47 | Путешественник', callback_data='AK-47 | Jet Set')
    item8 = types.InlineKeyboardButton('AK-47 | Panthera onca', callback_data='AK-47 | Panthera onca')
    item9 = types.InlineKeyboardButton('AK-47 | Красный глянец', callback_data='AK-47 | Red Laminate')
    item10 = types.InlineKeyboardButton('AK-47 | Топливный инжектор', callback_data='AK-47 | Fuel Injector')
    item11 = types.InlineKeyboardButton('AK-47 | Поверхностная закалка', callback_data='AK-47 | Case Hardened')
    item12 = types.InlineKeyboardButton('AK-47 | Пожелание на ночь', callback_data='AK-47 | Nightwish')
    item13 = types.InlineKeyboardButton('AK-47 | Азимов', callback_data='AK-47 | Asiimov')
    item14 = types.InlineKeyboardButton('AK-47 | Пустынный повстанец', callback_data='AK-47 | Wasteland Rebel')
    item15 = types.InlineKeyboardButton('AK-47 | Ice Coaled', callback_data='AK-47 | Ice Coaled')
    item16 = types.InlineKeyboardButton('AK-47 | Черный глянец', callback_data='AK-47 | Black Laminate')
    item17 = types.InlineKeyboardButton('AK-47 | Неоновый гонщик', callback_data='AK-47 | Neon Rider')
    item18 = types.InlineKeyboardButton('AK-47 | Императрица', callback_data='AK-47 | The Empress')
    item19 = types.InlineKeyboardButton('AK-47 | Ягуар', callback_data='AK-47 | Jaguar')
    item20 = types.InlineKeyboardButton('AK-47 | Кровавый спорт', callback_data='AK-47 | Bloodsport')
    item21 = types.InlineKeyboardButton('AK-47 | Аквамариновая месть', callback_data='AK-47 | Aquamarine Revenge')
    item22 = types.InlineKeyboardButton('AK-47 | Первый класс', callback_data='AK-47 | First Class')
    item23 = types.InlineKeyboardButton('AK-47 | Красная линия', callback_data='AK-47 | Redline')
    item24 = types.InlineKeyboardButton('AK-47 | Цвет джунглей', callback_data='AK-47 | Jungle Spray')
    item25 = types.InlineKeyboardButton('AK-47 | Снежный вихрь', callback_data='AK-47 | Frontside Misty')
    item26 = types.InlineKeyboardButton('AK-47 | Неоновая революция', callback_data='AK-47 | Neon Revolution')
    item27 = types.InlineKeyboardButton('AK-47 | Музей элиты', callback_data='AK-47 | Leet Museo')
    item28 = types.InlineKeyboardButton('AK-47 | Хищник', callback_data='AK-47 | Predator')
    item29 = types.InlineKeyboardButton('AK-47 | Буйство красок', callback_data='AK-47 | Point Disarray')
    item30 = types.InlineKeyboardButton('AK-47 | Легион Анубиса', callback_data='AK-47 | Legion of Anubis')
    item31 = types.InlineKeyboardButton('AK-47 | Орбита, вер. 01', callback_data='AK-47 | Orbit Mk01')
    item32 = types.InlineKeyboardButton('AK-47 | Изумрудные завитки', callback_data='AK-47 | Emerald Pinstripe')
    item33 = types.InlineKeyboardButton('AK-47 | Картель', callback_data='AK-47 | Cartel')
    item34 = types.InlineKeyboardButton('AK-47 | Сланец', callback_data='AK-47 | Slate')
    item35 = types.InlineKeyboardButton('AK-47 | Зелёный глянец', callback_data='AK-47 | Green Laminate')
    item36 = types.InlineKeyboardButton('AK-47 | Фантомный вредитель', callback_data='AK-47 | Phantom Disruptor')
    item37 = types.InlineKeyboardButton('AK-47 | Фиолетовое барокко', callback_data='AK-47 | Baroque Purple')
    item38 = types.InlineKeyboardButton('AK-47 | Защитная сетка', callback_data='AK-47 | Safety Net')
    item39 = types.InlineKeyboardButton('AK-47 | Синий глянец', callback_data='AK-47 | Blue Laminate')
    item40 = types.InlineKeyboardButton('AK-47 | Колымага', callback_data='AK-47 | Rat Rod')
    item41 = types.InlineKeyboardButton('AK-47 | Элитное снаряжение', callback_data='AK-47 | Elite Build')
    item42 = types.InlineKeyboardButton('AK-47 | Африканская сетка', callback_data='AK-47 | Safari Mesh')
    item43 = types.InlineKeyboardButton('AK-47 | Затерянная земля', callback_data='AK-47 | Uncharted')

    markup.add(item1, item2, item3, item4, item5,
               item6, item7, item8, item9, item10,
               item11, item12, item13, item14, item15,
               item16, item17, item18, item19, item20,
               item21, item22, item23, item24, item25,
               item26, item27, item28, item29, item30,
               item31, item32, item33, item34, item35,
               item36, item37, item38, item39, item40,
               item41, item42, item43, )

    bot.send_message(message.chat.id, 'Выберите скин', reply_markup=markup)
