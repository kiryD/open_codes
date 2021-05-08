x=0
y=0
ss = 0
sps = 0
costCl = 10
costS = 100


def setup():
    size(800,600)

def draw():
    global x, y, ss, costCl, costS,frame,sps
    
    a = loadImage("2.png")

    rect(x,y,20,20)
    if keyPressed:
        if key=="w":
            y-=5
        if key=="s":
            y+=5
        if key=="d":
            x+=5
        if key=="a":
            x-=5
    for step in range(0,1):
       
        image (a, random(0,800),random(0,600),30,30)
        
