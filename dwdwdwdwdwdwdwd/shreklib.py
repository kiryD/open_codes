import random
a=0
b=0
# массив поля, * — пустое поле, # — стена
pole=[["#","#","#","","#","#","#","#","#","#","#","#"],
     ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"],
             ["#","#","#","#","#","#","#","#","#","#","#","#"]]
# то, что будет выводиться на экран
vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]


bomb=[["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"],
      ["@","@","@","@","@","@","@","@","@","@","@","@"]]

stena=[["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"],
      ["*","*","*","*","*","*","*","*","*","*","*","*"]]


def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()

def stepa():
    for i in range(0,11):
        a=random.randint(0,11)
        b=random.randint(0,11)
        pole[a][b] = stena[a][b]

        
def bombes():
    for i in range(0,3):
        a=random.randint(0,11)
        b=random.randint(0,11)
        pole[a][b] = bomb[a][b]


def check1(stroka,stolb):
    john=0
   # если клетка ещё не открыта
    if vidimost_polya[stroka][stolb] == "•":
        # открываем
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        # если оно оказалось пустым
        if pole[stroka][stolb] == "*":
            # проверяем все соседние, только если они существуют
            # а то выйдем за пределы поля, Python ругать будет
            if stroka-1 >= 0:
                john+=1
                check1(stroka-1,stolb)
                if stolb-1 >= 0:
                    check1(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check1(stroka-1,stolb+1)
                    
            if stroka+1 < len(pole):
                john+=1
                check1(stroka+1,stolb)
                if stolb-1 >= 0:
                    check1(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check1(stroka+1,stolb+1)
                    
            if stolb-1 >= 0:
                john+=1
                check1(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check1(stroka,stolb+1)
            
def isOpen():
    # считаем, что поле открыто всё
    opened = True
    #для каждой строки в видимости поля
    for stroka in vidimost_polya:
        # если хотя бы в одной нашлось закрытое поле
        if "•" in stroka:
            # значит неправда, поле ещё не всё открыто
            opened = False
    if opened==True:
        print("ТЫ открыл поле")    
    return opened

def bombchk(stroka,stolb):
    if pole[stroka][stolb]=='@':
        game=False
def randompole():
    for i in range(12):
        for i in range(12):
            pole[stroka][stolb]