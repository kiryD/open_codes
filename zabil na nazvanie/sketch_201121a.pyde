sizeEll=50
y=0
x = 0
def setup():
    background(255,255,255)
    size(600,400)
def draw():
    global sizeEll, x, y
    translate(0,0)
    ellipse(x,y,sizeEll,sizeEll)
    x += 1    
    if x == 600:
        x=0
        y=y + 50
        
