# Stone Face Documentation


## Pseudo Code / list to do

Add characters.

Copy and paste intro story into renpy.

Make it so small character image moves based on mouse click. Mousex and mousey.
Make it so minigame moves based on mouse click and freezes the menu screen.

Find picture of town center. Pictures inside wigwams. Maybe use Unity project to take pictures.

Make it so when collide with position of wigwam on top down, enter wigwam.


## The Process

I defined San Kisos, Coimazu and Kili for dialogue purposes.

Added town center but too small, cropped then resized in correct aspect ratio. Will have to do that for all bg images.
Added placeholder images for San Kisos (S) and Kali (K).

Switched focus to writing the background story for San Kisos.

Had to look up how to make text wait then display next line. Used extend feature to keep text on screen but change the image.

Finished background and made transition to main story.

Next step: finish filling in main story including what expressions. Then send the required expressions to Lex so he can draw them. Include any other needed sprites on list.

While writing the story I made some filler sprites for S and C to be able to practice changing the direction they're looking. However, the sprites are too big and now I have to figure out how to crop them all the same so that they don't move around when they change facial expressions.
I'm giving up, I'll just try to imagine it in my head while writing code. I looked up how to do it on photoshop and Lightroom, and neither of them seem to work well with exporting or bulk processing png.

I had to add some back to make an animation of Coimazu running away. Currently I need to figure out how to hide an image during an animation.
I figured out that I can use alpha 0.0 to make an image invisible even though it's still there. I changed the code to line up the images where they would appear instead of trying to move them in 0 seconds.

Next I should finish copying in the intro story and setting up facial expressions. Then I should make a list of sprites I need.
I finished the intro story and edited the fox to make the sizes of the two sprites match better.

Next I should send Lex the list of sprites I need plus the context. Maybe I should record the game so he can see the context.

Notes:
The whole canvas is 1920x1080. That means each sprite should be created on a canvas that is 1080 pixels tall. If the sprite takes up that whole canvas top to bottom, that would meant that the sprite is as tall as the screen. For some reference, the placeholder san kisos sprite is 940 pixels tall from head to knee. He is about 500 pixels wide. So make sure to turn on pixel rulers when drawing so that you can match that.
- To make it easier to draw multiple facial expressions and looking directions:
- draw a character with their body facing straight with their head turned one way
- copy paste canvas
- mirror the head the other way (copy, flip paste)
- copy canvas
- change just the facial expression for each direction by copying the canvas and changing just facial expression to keep everything else consistent.

Character general descriptions:
San Kisos: long dark hair braids, holding obsidian knife.
Coimazu: taller than San Kisos (maybe make his sprite 990 pixels tall, still in a 1080 tall canvas). Looks different than san kisos, more similar to Kili.
Their father looks similar to coimazu but older, same height (990 pixels).

List of needed sprites:
Family: father looking down smiling at young san kisos and young coimazu.
San Kisos and coimazu Neutral, happy, sad, each left and right (12 total)
San kisos surprised left
Kili thinking (right up)

Lex made the body and one facial expression looking right and sent the Procreate file. I separated the head and body and made the other expressions, then flipped the head to make the other direction sprites.


Next I'll make a background for the village level, then a quick small sprite of San Kisos. After, I'll figure out how to get the sprite to move to where the mouse is clicked.

The background and sprite are made but for some reason they're not displaying after the intro section. I put them in a separate label but nothing is showing. I wonder if I have to put text for it to show? And if so how to I get it to not have to display text?
It turns out putting "pause" requires a click to move on.

Some pseudocode for how I want to make the 2d levels.
Make a new class called level.
Setting attributes of the class: each instance of is based on where in the game the level is. So location should be a parameter in `def __init__()`
It's also a class based on a base class in renpy, `renpy.displayable` so it needs that notation. When instantiated, it needs to also instantiate itself in renpy. So add that line.

I need it to display the correct background. 

Oh ok, I found the section in the renpy documentation that goes over creator defined displayable. This will make this so much easier (probably not but still more helpful than just looking at the pong reference). So I basically need to read through this, figure out which functions I need to define, then do it. The result is underneath this text block.

Things I definitely need and why:

def__init__(): adds attributes to this instance.

def render(self, width, height, st, at): tells renpy what to show on the screen and for how long / some physics.

def event(self, ev, x, y, st): I will import pygame to this to track where the mouse clicks to control where the sprite moves.

def visit(self): I need this because I'm using a child displayable (San Kisos Sprite) in the main displayable (the scene/level).

renpy.redraw(displayable, when): when to redraw a displayable. I might not need this since this will be a mostly static displayable until the sprite moves, which will redraw without this method.

raise renpy.IgnoreEvent(): for ignoring an event under the event function. Used in an if for whether to switch to inside a wigwam or not.

I could add a class wide attribute that defines an array of information about various locations to automatically load it based on the location.



First draft:
```python
class LevelDisplayable(renpy.Displayable):
    
    def __init__(self, location):
        
        renpy.Displayable.__init__(self)
        
        self.location = location
        
        # Sizes
        self.SANSPRITE_WIDTH = 92
        self.SANSPRITE_HEIGHT = 163
        
        
        # Displayables
        self.sansprite = Image("San Sprite.png")
        
        
        # If San Sprite is in range of a wigwam
        self.wigwam = False
        
    # Not sure if I need this, maybe it's a renpy attribute?
    def visit(self):
        return [ self.paddle, self.ball ]
```

Second draft: I followed along the example in the renpy documentation and looked at the definitions on [that page](https://www.renpy.org/doc/html/cdd.html). I also borrowed heavily from the pong example in the renpy tutorial for the physics equations. The issues with this draft (some of them were fixed before I remembered to paste here): `def __init__(self, location)` the location was never referenced and I deleted it; I thought that width and height worked as the project width and height which wasn't true so I added attributes called screenwidth and screenheight; I changed the `__init__` to 
```python
def __init__(self, **kwargs):
    super(LevelDisplayable, self).__init__(**kwargs)
```
as per the documentation example. It seems to have moved on to a new error so it probably helped; I changed the starting `targetx` and `targety` to 0 because `None` doesn't work to start; I misspelled the bool true; an error that says render not implemented when rendering sansprite. After looking around I tried changing `self.sansprite = renpy.Displayable("San Sprite.png")` to `self.sansprite = Image("San Sprite.png")` and it moved on to the next error so I assume this fixed that bug; sanspritex is not defined because I was supposed to type self.sanspritex; Oh yay! It "works" now. It's pretty janky though. 

Things I know I need to fix off the top of my head: 
- I need to set the default targetx and targety to the same spot as the default sanspritex and y so it doesn't start moving right when displaying the screen. Oh except that means it divides by zero...
- I need to only update the frames after clicking so that the sprite doesn't vibrate.
- I need to combine moving the sprite into one line so that it doesn't move by x and then y

This is draft 2.0 before some of the edits just listed:
```python

init python:

    class LevelDisplayable(renpy.Displayable):

        def __init__(self):

            # Sizes
            self.SANSPRITE_WIDTH = 92
            self.SANSPRITE_HEIGHT = 163
            self.screenheight = 1080
            self.screenwidth = 1920

            # Displayables
            self.sansprite = renpy.Displayable("San Sprite.png")

            # If San Sprite is in range of a wigwam
            self.wigwam = False

            # The position and speed of sansprite
            self.sanspritey = (self.screenheight/2)
            self.sanspritex = (self.screenwidth/2)
            self.sanspritespeed = 200.0

            # The target position of where the mouse was pressed
            self.targety = None
            self.targetx = None

            # time of the past render frame
            self.oldst = None

        def visit(self):
             return [ self.sansprite ]


        def render(self, width, height, st, at):

            # The render object being drawn into
            render = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Moves sansprite
            speed = dtime * self.sanspritespeed
            self.sanspritey += speed * (self.targety - self.sanspritey) / abs(self.targety - self.sanspritey)
            self.sanspritex += speed * (self.targetx - self.sanspritex) / abs(self.targetx - self.sanspritex)

            # draws sansprite
            sansprite_render = renpy.render(self.sansprite, width, height, st, at)
            render.blit(sansprite_render, (int(sanspritex), int(sanspritey)))

            # Re render quickly in order to show the next frame to make movement smooth
            renpy.redraw(self, 0)

            # return Render
            return render

        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == set the targetx and targety
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.targetx = x
                self.targety = y

                # Update the scren
                renpy.restart_interaction()
                
                
screen village_level():

    default village_level = LevelDisplayable()

    add "bg village level"

    add village_level

label start_village_level:

    window hide # to hide the window and quick menu while in village_level
    $ quick_menu = False

    call screen village_level

    $ quick_menu = true
    window show
```

Draft 2.1

```python

init python:

    class LevelDisplayable(renpy.Displayable):

        def __init__(self, **kwargs):

            super(LevelDisplayable, self).__init__(**kwargs)

            # Sizes
            self.SANSPRITE_WIDTH = 92
            self.SANSPRITE_HEIGHT = 163
            self.screenheight = 1080
            self.screenwidth = 1920

            # Displayables
            self.sansprite = Image("San Sprite.png")

            # If San Sprite is in range of a wigwam
            self.wigwam = False

            # The position and speed of sansprite
            self.sanspritey = (self.screenheight/2)
            self.sanspritex = (self.screenwidth/4)
            self.sanspritespeed = 200.0

            # The target position of where the mouse was pressed
            self.targety = 0.0
            self.targetx = 0.0

            # time of the past render frame
            self.oldst = None

        def visit(self):
             return [ self.sansprite ]


        def render(self, width, height, st, at):

            # The render object being drawn into
            render = renpy.Render(1920, 1080)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Moves sansprite
            speed = dtime * self.sanspritespeed
            self.sanspritey += speed * (self.targety - self.sanspritey) / abs(self.targety - self.sanspritey)
            self.sanspritex += speed * (self.targetx - self.sanspritex) / abs(self.targetx - self.sanspritex)

            # draws sansprite
            sansprite_render = renpy.render(self.sansprite, 1920, 1080, st, at)
            render.blit(sansprite_render, (int(self.sanspritex), int(self.sanspritey)))

            # Re render quickly in order to show the next frame to make movement smooth
            renpy.redraw(self, 0)

            # return Render
            return render

        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == set the targetx and targety
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.targetx = x
                self.targety = y

                # Update the scren
                renpy.restart_interaction()

screen village_level():

    default village_level = LevelDisplayable()

    add "bg village level"

    add village_level

label start_village_level:

    call screen village_level

```


Draft 3

Things I know I need to fix off the top of my head: 
- I need to set the default targetx and targety to the same spot as the default sanspritex and y so it doesn't start moving right when displaying the screen. Oh except that means it divides by zero...
- I need to only update the frames after clicking so that the sprite doesn't vibrate.
- I need to combine moving the sprite into one line so that it doesn't move by x and then y

To make it only update while moving I can check if its position is different than the target position maybe.

I wish I was less tired. I think I could use my knowledge of calculus but I'm too tired to remember the right steps to solve these problems.


## References

### Image links
[Cards](https://www.etsy.com/listing/545063035/secret-pocket-oracle-mildred-payne-mini?gpla=1&gao=1&&utm_source=google&utm_medium=cpc&utm_campaign=shopping_us_b-art_and_collectibles-artist_trading_cards&utm_custom1=_k_CjwKCAjwuJ2xBhA3EiwAMVjkVJHbrzVSqk9DIk85TQEZFXEqMVoE9NywV8FICSLhfq-73LmuSqYI8RoCWHoQAvD_BwE_k_&utm_content=go_12569400376_122439139591_507342873318_pla-355586253777_c__545063035_562648315&utm_custom2=12569400376&gad_source=1&gbraid=0AAAAADtcfRJYuDVDiH-YJop-HgqlOOwG7&gclid=CjwKCAjwuJ2xBhA3EiwAMVjkVJHbrzVSqk9DIk85TQEZFXEqMVoE9NywV8FICSLhfq-73LmuSqYI8RoCWHoQAvD_BwE)

[Alcove](https://www.shutterstock.com/image-photo/woods-tree-trunk-cave-forest-whimsical-2376330363)

[wigwam interior](https://www.flickr.com/photos/57608438@N08/5791905348)

[obsidian knife](https://www.tochtliwear.com/products/tecpatl-obsidian-knife)

[old growth forest](https://onetreeplanted.org/blogs/stories/old-growth-forest)


### Pong Code
init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 15
            self.BALL_HEIGHT = 15
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 380.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 350.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play("pong_beep.opus", channel=0)

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play("pong_boop.opus", channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "eileen"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "player"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return them. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add "bg pong field"

    add pong

    text "Player":
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text "Eileen":
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text "Click to Begin":
            xalign 0.5
            ypos 50
            size 40

label play_pong:

    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show

show eileen vhappy

if _return == "eileen":

    e "I win!"

else:

    e "You won! Congratulations."
 