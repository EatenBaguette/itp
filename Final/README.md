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

            # If we have a winner, return him or her. Otherwise, ignore
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
 