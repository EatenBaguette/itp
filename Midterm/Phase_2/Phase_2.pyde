def setup():
    size(200, 200)
    noFill()
def drawUnit():
    triangle(-70, -70, -70, 70, 70, 70)
def draw():
    translate(100, 100)
    for i in range(24):
        rotate(PI/12)
        drawUnit()
    
    
