def setup():
    size(600,300)
    
x = 0
y = 0
 
def draw():
    global x,y
    translate(width / 2, height / 2)
    strokeWeight(45)
    stroke(255,0,0)
    point(-20,-30)
    point(-50,-30)
    strokeWeight(1)
    rotate(radians(45))
    fill(255,0,0)
    rect(-58,-10,45,45)
