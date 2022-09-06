import telebot
from telebot import types

from AUGS import augs
from FAMAS import famas
from workTOKEN import workTOKEN
import parse
import get_hash_name
import time
from qual_markups import quality, redline, bloodsport, greenlaminate, hotrod, copperhead, jade, darkwater
from akas import aks

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
        bot.send_message(chat_id=call.message.chat.id,
                         text="Кажется вы выбрали качество, но не выбрали скин. Пожалуйста, выберите скин")
    else:
        if len(data) == 0:
            bot.send_message(chat_id=call.message.chat.id,
                             text="Кажется скин в этом качестве сейчас не продается. Попробуйте другое качество")

        else:
            for i in range(3):
                bot.send_message(chat_id=call.message.chat.id,
                                 text="Price: " + str(data[i]['price'] / 100) + "  |  Float: " + str(
                                     data[i]['extra']['float']))
                bot.send_message(chat_id=call.message.chat.id, text="URL: " + parse.get_url(data[i]))


@bot.callback_query_handler(func=lambda call: True)
def backhandler(call):
    global name
    if call.message:
        if call.data == 'AK-47 | Redline':
            name = basenameformatter(call)
            redline(call)

        if call.data == 'AK-47 | Wild Lotus':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | X-Ray':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Gold Arabesque':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Hydroponic':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Vulcan':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Jet Set':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Panthera onca':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Red Laminate':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Fuel Injector':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Case Hardened':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Nightwish':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Asiimov':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Wasteland Rebel':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Ice Coaled':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Black Laminate':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Neon Rider':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | The Empress':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Jaguar':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Bloodsport':
            name = basenameformatter(call)
            bloodsport(call)

        if call.data == 'AK-47 | Aquamarine Revenge':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | First Class':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Jungle Spray':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Frontside Misty':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Neon Revolution':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Leet Museo':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Predator':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Point Disarray':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Legion of Anubis':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Orbit Mk01':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Emerald Pinstripe':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Cartel':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Slate':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Green Laminate':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'AK-47 | Phantom Disruptor':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Phantom Disruptor':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Fire Serpent':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Baroque Purple':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Safety Net':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Blue Laminate':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'AK-47 | Rat Rod':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Elite Build':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Safari Mesh':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AK-47 | Uncharted':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Akihabara Accept':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Hot Rod':
            name = basenameformatter(call)
            hotrod(call)

        if call.data == 'AUG | Flame Jormungandr':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Midnight Lily':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Copperhead':
            name = basenameformatter(call)
            copperhead(call)

        if call.data == 'AUG | Sand Storm':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Bengal Tiger':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Momentum':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Anodized Navy':
            name = basenameformatter(call)
            hotrod(call)

        if call.data == 'AUG | Wings':
            name = basenameformatter(call)
            hotrod(call)

        if call.data == 'AUG | Death by Puppy':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'AUG | Fleet Flock':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Syd Mead':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Colony':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Stymphalian':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Torque':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Carved Jade':
            name = basenameformatter(call)
            jade(call)

        if call.data == 'AUG | Arctic Wolf':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Chameleon':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Random Access':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Daedalus':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Navy Murano':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Aristocrat':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Radiation Hazard':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Condemned':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Ricochet':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Plague':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Amber Fade':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'AUG | Spalted Wood':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Amber Slipstream':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Triqua':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Tom Cat':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Storm':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Contractor':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Surveillance':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'AUG | Sweeper':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Spitfire':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Afterimage':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'FAMAS | Sundown':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Contrast Spray':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Prime Conspiracy':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Commemoration':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Roll Cage':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Meltdown':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'FAMAS | Eye of Athena':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Djinn':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Mecha Industries':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Styx':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Pulse':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'FAMAS | Dark Water':
            name = basenameformatter(call)
            darkwater(call)

        if call.data == 'FAMAS | ZX Spectron':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Valence':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Sergeant':
            name = basenameformatter(call)
            redline(call)

        if call.data == 'FAMAS | Hexane':
            name = basenameformatter(call)
            greenlaminate(call)

        if call.data == 'FAMAS | Doomkitty':
            name = basenameformatter(call)
            darkwater(call)

        if call.data == 'FAMAS | Night Borre':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Meow 36':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Neural Net':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Macabre':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Cyanospatter':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Teardown':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Decommissioned':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | CaliCamo':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Crypsis':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Survivor Z':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Faulty Wiring':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'FAMAS | Colony':
            name = basenameformatter(call)
            quality(call)

        if call.data == 'Factory New':
            name += ' (Factory New)'
            getinfo(call)
            name = ''

        if call.data == 'Minimal wear':
            name += ' (Minimal wear)'
            getinfo(call)
            name = ''

        if call.data == 'Field-Tested':
            name += ' (Field-Tested)'
            getinfo(call)
            name = ''

        if call.data == 'Well-Worn':
            name += ' (Well-Worn)'
            getinfo(call)
            name = ''

        if call.data == 'Battle-Scarred':
            name += ' (Battle-Scarred)'
            getinfo(call)
            name = ''
