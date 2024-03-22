sin_wave = []
num = 12
s = 4
def setup():
    size(num * s, num * s)
    noFill()
    background(255)
    
def drawUnit():
    pushMatrix()
    triangle(-.35*width, -.35*height, -.35*width, .35*height, .35*width, .35*height)
    #quad(-.15*width, -.15*height, 0, -.5*height, .3*width, 0, .1*width, -.35*height)
    #rect(0, 0, .085*width, .115*height)
def draw():
    translate(width/2, height/2)
    for i in range(num*2):
        rotate(PI/num)
        drawUnit()
    

    
    
    
