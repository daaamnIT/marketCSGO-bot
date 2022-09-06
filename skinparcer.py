from listofcsgoskins import allskins
from itertools import groupby

#Винтовки
ak = []
aug = []
famas = []
galil = []
m4a4 = []
m4a1s = []
sg = []

#снайперские винтовки
awp = []
ssg = []
scar = []
g3s = []

#пп
bizon = []
mac = []
mp5 = []
mp7 = []
mp9 = []
p90 = []
ump = []

#Пистолеты
rev = []
deagle = []
cz = []
berets = []
f7 = []
glock = []
usp = []
tec = []
p2000 = []
p250 = []

#ДРОБОВИКИ
mag = []
nove = []
xm = []
sawoff = []

#ПУЛЕМЕТЫ
m249 = []
negev = []


def parcer():
    # global ak, m4a4, m4a1s, aug, sg, famas, galil
    list = []
    for i in range(len(allskins)):
        list.append(str(allskins[i]['weapon']) + ' | ' + str(allskins[i]['name']))

    skinslist = [el for el, _ in groupby(list)]
    print(skinslist)

    for i in range(len(skinslist)):
        if skinslist[i].split()[0] == 'AK-47':
            ak.append(skinslist[i])
        if skinslist[i].split()[0] == 'AUG':
            aug.append(skinslist[i])
        if skinslist[i].split()[0] == 'FAMAS':
            famas.append(skinslist[i])
        if skinslist[i].split()[0] == 'M4A4':
            m4a4.append(skinslist[i])
        if skinslist[i].split()[0] == 'M4A1-S':
            m4a1s.append(skinslist[i])
        if skinslist[i].split()[0] == 'SG':
            sg.append(skinslist[i])
        if skinslist[i].split()[0] == 'Galil':
            galil.append(skinslist[i])
        if skinslist[i].split()[0] == 'AK-47':
            ak.append(skinslist[i])

    print(ak)
    print(m4a1s)
    print(m4a4)
    print(famas)
    print(galil)
    print(sg)
    print(aug)
    ak_2 = set(ak)
    m4a1s_2 = set(m4a1s)
    m4a4_2 = set(m4a4)
    famas_2 = set(famas)
    galil_2 = set(galil)
    sg_2 = set(sg)
    aug_2 = set(aug)
    print(len(aug_2))


if __name__ == "__main__":
    parcer()