def setup():
    size(600,300)

x = 0

def draw():
    background(0)
    global x
    rotate(x)
    stroke(255,255,0)
    strokeWeight(50)
    point(300,150)
    strokeWeight(5)
    line(300,150,300,250)
    line(300,150,350,150)
    line(300,150,400,100)
    line(300,150,450,50)
    line(300,150,-450,0)
    line(300,150,-400,-50)
    line(300,150,-350,-100)

    x = x + 1
