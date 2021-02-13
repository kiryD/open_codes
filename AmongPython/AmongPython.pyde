def setup():
    size(600,400)
    fill(255,0,0)
def draw():
    translate(300,200)
    background(255)
    fill(0,0,255)
    ellipse(200,200,70,30)
    ellipse(200,200,30,70)
    fill(255)
    ellipse(200,200-10,40,30)
    rotate(radians(12))
    for s in range (10):        
        fill(255,0,0)
        ellipse(mouseX,mouseY,70,30)
        ellipse(mouseX,mouseY,30,70)
        fill(255)
        ellipse(mouseX,mouseY-10,40,30)
        rotate(radians(30))
