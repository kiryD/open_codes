z=100
x=200
c = 200
v = 200
def setup():
    size(600,480)
    background(255)
def draw():   
    global z,x
    background(255)
    if keyPressed:
        if keyCode == UP:
            z -= 10
        if keyCode == DOWN:
            z += 10
        if key == "w":
            x -= 10
        if key == "s":
            x += 10
    if z == -10:
        z = 100
    if z == 480:
        z = 400 
    if x == -10:
        x = 200
    if x == 480:
        x = 400                  
    if c == 600:
        c = rotate(90)
    if v == 480:
        v = 400
    fill(0)
    rect(0,z,60,160)
    rect(540,x,60,160)
    ellipse(200,c,200,v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
