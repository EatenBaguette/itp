# Midterm Documentation

## Phase 1

I want to create a rotated triangle pattern. I made a 25 by 25 grid and added a square, drew a circle inside the square, then a triangle inside the circle starting at (x,y) = (4,4). 

![sketch_without_rotation](img/Phase1_01.png)

Then I rotated it a bunch of times. I got lazy and stopped. Once I figure out the code, I'll let the computer finish it for me. Hopefully you get the basic idea though.

![sketch_with_rotation](img/Phase1_02.png)

## Phase 2

I started by giving each square on the grid 10 pixels. I didn't want any shape to have a fill, and I did want a stroke.

```
def setup():
    size(250, 250)
    noFill()
```

Then I made the first triangle.

```
def drawUnit():
    triangle(40, 40, 40, 210, 210, 210)
```
    
Then I tried to make it draw all the triangles. This did not work. I tried moving ```angle == 0``` to below the def, but it still didn't work.

```
def draw():
    for i in range (12):
        angle == 0
        rotate(radians(angle))
        drawUnit()
        angle += 10
```

I tried cutting the code down into this, and nothing was drawn. There's probably something wrong with the rotate function. I tried it with a rectangle just in case. Yes, the rotate function is not working.
```
def setup():
    size(250, 250)
    noFill()
def draw():
    rotate(PI/3.0)
    triangle(40, 40, 40, 210, 210, 210)
```

I learned about the transformation matrix. The rotation function just shifts the angle of where shapes are drawn to, so it shifts around (0,0). What I can do is move the origin using the translate function so that the rotation function will work better. The following changes the origin to the center of the canvas. The triangle looks the same as before but now it's entered differently. I also changed the canvas to 200x200 because it felt easier to me.

```
def setup():
    size(200, 200)
    noFill()
def draw():
    translate(100, 100)
    triangle(-70, -70, -70, 70, 70, 70)
```
I added rotation to test if it would work, and it did:

![rotate_test](img/Phase2_01.png)

Now I can try some of what I made before to see if it works.
```
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
```
It worked.

![translated triangle](img/Phase2_02.png)

I just realized I can do a lot by changing the drawUnit to make some interesting rotation art!
```
def drawUnit():
    pushMatrix()
    triangle(-70, -70, -70, 70, 70, 70)
    quad(-30, -30, 0, -100, 60, 0, 20, -70)
    rect(0, 0, 17, 23)
```

![added quad and rectangle](img/Phase2_03.png)

I checked what would happen without pushMatrix(). The lines become blurrier for some reason, so I'll keep it for now.

## Phase 3
I referenced the example for Phase 3 in the README [here on Github](https://github.com/rdwrome/261sp24/tree/main/07Midterm). Using the organization of the code, I kept the drawUnit function and made a new drawObject function with parameters x, y, and s. Following the example code, I pushed the matrix, set the translation, then the scale, then drew the shapes, then reset the matrix. The only issue I had was that I wanted to not let the shape go over the border, so I added a base translation of `100 * s` for x and y (because at a scale of 1, the origin needs to be at (100,100) to draw the shape without going over the border).

I added descriptions for each line for easy interpretation.

```python
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
```
This is what the code currently draws:

![two side by side](img/Phase3_01.png)

## Phase 4


