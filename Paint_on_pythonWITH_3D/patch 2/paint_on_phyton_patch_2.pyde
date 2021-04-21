#Рандом
r = random(50,100)
#Размер окна и цвет фона
def setup():
    background(0)
    size(1200,600)
#Само рисование
def draw():
    #Что бы не говорил что не правильно
    global r
    #Заливается текст
    fill(255)
    #Сам текст
    textSize(20)
    text("e = reset", 10, 60)
    text("r = swap to 3D", 10, 80)
    text("left = grey", 10, 100)
    text("right = blue", 10, 120)
    text("center = red", 10, 140)
    text("w = rectane", 10, 160)
    text("q = ellipse", 10, 180)
    text("a = sky", 10, 200)
    text("ver. 1.1.2(patch 2)", 1000, 580)
    if mousePressed and mouseButton == (LEFT):
        stroke(132)
        strokeWeight(50)
        line(mouseX,mouseY,mouseX,mouseY)
    if mousePressed and mouseButton == (RIGHT):
        stroke(0,0,255)
        strokeWeight(50)
        line(mouseX,mouseY,mouseX,mouseY)
    if mousePressed and mouseButton == (CENTER):
        stroke(255,0,0)
        strokeWeight(50)
        line(mouseX,mouseY,mouseX,mouseY)
    if keyPressed and (key == 'e'):
        background(0)
    if keyPressed and key == "r":
        stroke(255)
        strokeWeight(5)
        fill(255,0,0)
        rect(random(0,600),random(0,300),random(0,600),random(0,300))
    if keyPressed and key == "w":
        rect(mouseX,mouseY,pmouseX,pmouseY)
    if keyPressed and key == "q":
        ellipse(mouseX,mouseY,pmouseX,pmouseY)
    if keyPressed and key == "a":
        point(random(0,1600),random(0,900))
        strokeWeight(10)
        stroke(r)
