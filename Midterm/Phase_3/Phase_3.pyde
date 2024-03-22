def setup():
    size(800, 800) # sets canvas size
    noFill() # idsable drawing fill
def drawUnit():
    triangle(-70, -70, -70, 70, 70, 70) # draws a triangle
    #quad(-30, -30, 0, -100, 60, 0, 20, -70) # draws a 4 sided shape
    #rect(0, 0, 17, 23) # draws a square
def drawObject(x, y, s):
    push() # saves the current drawing position
    translate(x + 100 * s, y + 100 * s) # translates current origin.
    scale(s) 
    for i in range(24):
        drawUnit()
        rotate(PI/12)
    pop()
def draw():
   drawObject(0,0,2)
   drawObject(400,0,2)
    
