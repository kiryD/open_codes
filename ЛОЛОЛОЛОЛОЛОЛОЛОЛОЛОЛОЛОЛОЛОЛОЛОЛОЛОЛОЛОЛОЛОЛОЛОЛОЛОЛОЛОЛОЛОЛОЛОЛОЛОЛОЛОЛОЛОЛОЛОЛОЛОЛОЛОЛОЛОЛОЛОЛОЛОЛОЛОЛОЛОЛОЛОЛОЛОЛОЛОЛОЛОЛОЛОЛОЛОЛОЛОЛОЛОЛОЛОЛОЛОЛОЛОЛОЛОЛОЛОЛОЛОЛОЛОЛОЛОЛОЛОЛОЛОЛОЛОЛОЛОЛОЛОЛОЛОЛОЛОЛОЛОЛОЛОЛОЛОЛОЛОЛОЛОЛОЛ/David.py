import shreklib
shreklib.vyvodPolya(shreklib.vidimost_polya)
shreklib.bombes()
game=True

while game == True:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    if (stolb>1 and stolb<12) or (stroka<1 and stroka>12):
        # передадим не номера строки и столбца, а индексы
        shreklib.check(stroka-1,stolb-1)
        shreklib.vyvodPolya(shreklib.vidimost_polya)
        if shreklib.isOpen():
            game = False
    else:
        game=False
        