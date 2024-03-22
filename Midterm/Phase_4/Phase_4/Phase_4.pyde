def setup():
    size(800, 800) # sets canvas size
    noFill() # disables drawing fill
    
def drawUnit():
    triangle(-70, -70, -70, 70, 70, 70) # draws a triangle
    #quad(-30, -30, 0, -100, 60, 0, 20, -70) # draws a 4 sided shape
    #rect(0, 0, 17, 23) # draws a square
    #they are turned off because they make the shape too busy when small scaled.
    
def drawObject(x, y, s): # draws the object at a specified coordinate and scale.
    push() # saves the current drawing position
    translate(x + 100 * s, y + 100 * s) # translates the origin.
    scale(s) # scale around origin.
    for i in range(24): # draws a unit, rotates around the origin, and repeats.
        drawUnit()
        rotate(PI/12)
    pop() # returns the saved drawing position.
    
def draw():
   drawObject(0,0,2)
   drawObject(400,0,2)
    
