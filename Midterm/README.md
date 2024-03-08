# Midterm Documentation

## Phase 1

I want to create a rotated triangle pattern. I made a 25 by 25 grid and added a square, drew a circle inside the square, then a triangle inside the circle starting at (x,y) = (4,4). Then I rotated it a bunch of times to create [insert image here]

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
![rotate_test](img/01.png)


