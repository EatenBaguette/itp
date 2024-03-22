from random import random as r

# how many pixels wide and tall should the square canvas be? Please enter a multiple of 100.
canvasSize = 800

# how many rows and columns will there be? 4 means a 4x4 grid.
gridSize = 10

# 1 means each object just touches. Set to between 0 and 1 to increase 
# the space between each object. Set above 1 to overlap objects.
scaleValue = 1 / float(gridSize)

rotations = 16 # how many rotations before reaching 2PI radians.

# calculates the pixel width/height of each cell of the grid.
cellSize = canvasSize / float(gridSize)

sine_wave = []
      
def setup():
    size(canvasSize, canvasSize) # sets canvas size
    noFill() # disables drawing fill
    noLoop()
    for i in range(canvasSize):
        radian = map(i, 0, canvasSize, 0, PI/2)
        sine_wave.append(abs(sin(radian)))

def drawUnit():
    triangle(-70, -70, -70, 70, 70, 70) # draws a triangle
    
    # Turn these off when tiling small because it gets too busy.
    #quad(-30, -30, 0, -100, 60, 0, 20, -70) # draws a 4 sided shape
    #rect(0, 0, 17, 23) # draws a square
    
def drawObject(x, y): # draws the object at a specified coordinate and scale.
    push() # saves the current drawing position
    translate(x + (100 * scaleValue * width / 200), y + (100 * scaleValue * width / 200)) # translates the origin.
    scale(scaleValue * width / 200) # scale around origin.
    for i in range(2 * rotations): # draws a unit, rotates around the origin, and repeats.
        drawUnit()
        rotate(PI/rotations)
    pop() # returns the saved drawing position.
    
def draw(): # draws a tiled pattern.
    for i in range(0,width):
        
        # Turn on for ombre pattern along x axis.
        #stroke(sine_wave[i] * 255 + 10)
        
        # Turn on for random along x axis.
        #stroke(r() * 255)
        if i % cellSize == 0:
            for j in range(height):
                
                # Turn on for random everywhere.
                #stroke(r() * 255)
                if j % cellSize == 0:
                    drawObject(i,j)
    
def mousePressed():
    redraw()

           
    
