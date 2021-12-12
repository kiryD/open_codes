import random
import time
cardpacks=3
ingame=1
cards=0
cardbelka=0
cardpchela=0
cardkrisa=0
cardmyaso=0
cardklop=0
while ingame==1:
    menu=input("You have cardpacks! Use command :use cardpack:. See your cardpacks :see cardpacks:. See your cards :see cards:.\n")
    if menu=="use cardpack":
        if cardpacks!=0:
            cardwe=random.randint(0,2)
            cardhp=random.randint(1,2)
            if cardhp=="1" and cardwe=="0":
                cardbelka=1
            if cardhp=="1" and cardwe=="1":
                cardpchela=1
            if cardhp=="1" and cardwe=="2":
                cardklop=1
            if cardhp=="2" and cardwe=="0":
                cardmyaso=1
            if cardhp=="2" and cardwe=="2":
                cardkrisa=1
    if menu=="see cards":
        if cardbelka==1:
            print("cards: squirel(0,1),")
        if cardpchela==1:
            print("pchela(1,1),")
        if cardklop==1:
            print("klop(1,2),")
        if cardmyaso==1:
            print("meat(2,0),")
        if cardkrisa==1:
            print("KRISA(2,2),")
##        if cardpchela==1:
##            print("pchela(1,1),")
    if menu=="cheat":
        print("mining cardpack")
        time.sleep(0.1)
        print("mining cardpack.")
        time.sleep(0.1)
        print("mining cardpack..")
        time.sleep(0.1)
        print("mining cardpack...")
        time.sleep(0.1)
        cardpack+=1
        print("+1 Cardpack")
    if menu=='use':
        print("Use :use cardpacks:")
    if menu=='see':
        print("Use :see inventory: or :see cards: or :see cardpacks:")
