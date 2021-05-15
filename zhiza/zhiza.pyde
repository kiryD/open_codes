eda=10
voda=10
dol=5
HP=100
def setup():
    size(1200,600)
    frameRate(5)
def draw():
    background(10)
    global HP,voda,eda,dol
    textSize(20)
    text(u"Еда : "+str(eda),0,100)
    text(u"Вода : "+str(voda),0,150)
    text(u"$ - "+str(dol),0,200)
    push()
    textSize(50)
    text(u"Товарищ! Береги своё Здоровье "+str(HP),0,50)
    pop()
    
    if keyPressed:
        if key == '1':
            eda+=2
            voda+=1
            dol-=5
            HP+=25
        if key == '2':
            eda-=2
            voda-=1
            dol+=5
            HP-=1
        if key == '3':
            eda-=1
            voda+=5
            HP-=12
        if HP <= 0:
            exit()
        if voda<=-1 and key == '2':
            HP-=4
        if eda <= -1 and key == '2':
            HP-=4
        if HP >= 101:
            HP=100
