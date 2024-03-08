def setup():
    size(200, 200)
    noFill()
def drawUnit():
    pushMatrix()
    triangle(-70, -70, -70, 70, 70, 70)
    quad(-30, -30, 0, -100, 60, 0, 20, -70)
    rect(0, 0, 17, 23)
def draw():
    translate(100, 100)
    for i in range(24):
        rotate(PI/12)
        drawUnit()
    
    
