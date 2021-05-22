x1=0
y1=700
x2=100
y2=0

def setup():
    size(1300,700)
def draw():
    background(255)
    ve=loadImage("verx.png")
    vn=loadImage("vniz.png")
    global x1,y1,ve,vn,X2,Y2
    image(vn,0,0,100,100)
    image(ve,100,0,100,100)
    image(vn,x1,y1,100,100)
    image(ve,x2,y2,100,100)
    y1-=1
    if keyPressed:
        if x1<=0 and y1<=0 and keyCode=='DOWN':
            exit()
