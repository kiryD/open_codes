x = 0
y = 30
def setup():
    size(600,480)
        
#def draw():    
#    if keyPressed:
#        if key == 'q' or key == 'Q' or key == u'й' or key == u'Й':
#            text("q", 10, 30)
#        if key == 'w' or key == 'W' or key == u'ц' or key == u'Ц':
#            text("w", 20, 30)
#        if key == 'e' or key == 'E' or key == u'у' or key == u'У':
#            text("e", 30, 30)
#        if key == 'r' or key == 'R' or key == u'к' or key == u'К':
#            text("r", 40, 30)
#    if key == 't' or key == 'T' or key == u'е' or key == u'Е':
#            text("t", 50, 30)
def draw():
    global x,y
    if keyPressed:
        x += 10
        text(key,x,y)
    if x == 450:
        y += 10
        x -= 600
        
