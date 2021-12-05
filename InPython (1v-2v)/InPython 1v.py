import random
cardpacks=1
ingame=1
cards=0
cardsquirel=0
cardbee=0
while ingame==1:
menu=input("You have 3 cardpack, to use print :use cardpack:. To see cards print :see cards:")
    if menu=="use cardpack":
        if cardpacks!=0:
            cardwe=random.randint(0,1)
            cardhp=random.randint(1,1)
            print(cardhp)
            print(cardwe)
            if cardhp==1 and cardwe==0:
                cardbelka=1
                if cardbelka==1:
                    cards+=1
    if menu=="see cards":
        print("card : ",cards)
        if cardbelka ==1 and cards:
            print("cards: belka(0,1)")
        if cardpchela==1:
                print("pchela(1,1)
    if menu=="use":
    	print("print :use cardpack:")    
