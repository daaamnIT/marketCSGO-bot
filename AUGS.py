import telebot
from telebot import types
from workTOKEN import workTOKEN

botTOKEN = workTOKEN

bot = telebot.TeleBot(botTOKEN)

name = ''


def augs(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('AUG | Акихабара', callback_data='AUG | Akihabara Accept')
    item2 = types.InlineKeyboardButton('AUG | Хот-род', callback_data='AUG | Hot Rod')
    item3 = types.InlineKeyboardButton('AUG | Пламенный Ёрмунганд', callback_data='AUG | Flame Jormungandr')
    item4 = types.InlineKeyboardButton('AUG | Полуночная лилия', callback_data='AUG | Midnight Lily')
    item5 = types.InlineKeyboardButton('AUG | Медянка', callback_data='AUG | Copperhead')
    item6 = types.InlineKeyboardButton('AUG | Песчаная буря', callback_data='AUG | Sand Storm')
    item7 = types.InlineKeyboardButton('AUG | Бенгальский тигр', callback_data='AUG | Bengal Tiger')
    item8 = types.InlineKeyboardButton('AUG | Динамика', callback_data='AUG | Momentum')
    item9 = types.InlineKeyboardButton('AUG | Анодированная синева', callback_data='AUG | Anodized Navy')
    item10 = types.InlineKeyboardButton('AUG | Крылья', callback_data='AUG | Wings')
    item11 = types.InlineKeyboardButton('AUG | Смертоносные пёсики', callback_data='AUG | Death by Puppy')
    item12 = types.InlineKeyboardButton('AUG | Скорая стая', callback_data='AUG | Fleet Flock')
    item13 = types.InlineKeyboardButton('AUG | Сид Мид', callback_data='AUG | Syd Mead')
    item14 = types.InlineKeyboardButton('AUG | Колония', callback_data='AUG | Colony')
    item15 = types.InlineKeyboardButton('AUG | Стимфалийская птица', callback_data='AUG | Stymphalian')
    item16 = types.InlineKeyboardButton('AUG | Закрученный', callback_data='AUG | Torque')
    item17 = types.InlineKeyboardButton('AUG | Резной нефрит', callback_data='AUG | Carved Jade')
    item18 = types.InlineKeyboardButton('AUG | Арктический волк', callback_data='AUG | Arctic Wolf')
    item19 = types.InlineKeyboardButton('AUG | Хамелеон', callback_data='AUG | Chameleon')
    item20 = types.InlineKeyboardButton('AUG | Оперативная память', callback_data='AUG | Random Access')
    item21 = types.InlineKeyboardButton('AUG | Дедал', callback_data='AUG | Daedalus')
    item22 = types.InlineKeyboardButton('AUG | Синее Мурано', callback_data='AUG | Navy Murano')
    item23 = types.InlineKeyboardButton('AUG | Аристократ', callback_data='AUG | Aristocrat')
    item24 = types.InlineKeyboardButton('AUG | Радиационная опасность', callback_data='AUG | Radiation Hazard')
    item25 = types.InlineKeyboardButton('AUG | Осужденный', callback_data='AUG | Condemned')
    item26 = types.InlineKeyboardButton('AUG | Рикошет', callback_data='AUG | Ricochet')
    item27 = types.InlineKeyboardButton('AUG | Чума', callback_data='AUG | Plague')
    item28 = types.InlineKeyboardButton('AUG | Янтарный градиент', callback_data='AUG | Amber Fade')
    item29 = types.InlineKeyboardButton('AUG | Застарелое дерево', callback_data='AUG | Spalted Wood')
    item30 = types.InlineKeyboardButton('AUG | Янтарный шквал', callback_data='AUG | Amber Slipstream')
    item31 = types.InlineKeyboardButton('AUG | Квадрант', callback_data='AUG | Triqua')
    item32 = types.InlineKeyboardButton('AUG | Кот-истребитель', callback_data='AUG | Tom Cat')
    item33 = types.InlineKeyboardButton('AUG | Гроза', callback_data='AAUG | Storm')
    item34 = types.InlineKeyboardButton('AUG | Наемник', callback_data='AUG | Contractor')
    item35 = types.InlineKeyboardButton('AUG | Слежка', callback_data='AUG | Surveillance')
    item36 = types.InlineKeyboardButton('AUG | Дворник', callback_data='AUG | Sweeper')

    markup.add(item1, item2, item3, item4, item5,
               item6, item7, item8, item9, item10,
               item11, item12, item13, item14, item15,
               item16, item17, item18, item19, item20,
               item21, item22, item23, item24, item25,
               item26, item27, item28, item29, item30,
               item31, item32, item33, item34, item35,
               item36, )

    bot.send_message(message.chat.id, 'Выберите скин', reply_markup=markup)
