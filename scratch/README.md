# itp
# Scratch Documentation

The documentation (again, always in Markdown as a .md file) must have the following:
- what you did
- how you did it
- the problems you faced (ABDYD: always be documenting your debugging!)
- how you overcame them
- what code you used from others/elsewhere
- where to find that code (specific links!!!)
- Other folks' GitHub public repositories and Stack OverFlow Links to an external site. are the best places to go for help most of the time
- Correctly document all your debugging, especially if you code ultimately does not run as intended. I will take points off for code that does not run correctly, but will still give partial credit if it is well-documented.
- For the purposes of this class, your documentation also helps you prepare to talk about your code in class with your colleagues.


## Pseudocode <br>
  ### movement
1. if left arrow pressed, turn left and move left.
2. if right arrow pressed, turn right and move right.
3. if up arrow or w pressed, move up.
4. if down arrow or s clicked, move down.
<br>

### Actions
1. if press space, toggle sit down/lay down

<br>

### collection
1. if touch orange, collect it.
  - create a counter.
  - hide the orange.
2. if hit by bear, drop oranges.
  - using the counter to track how many oranges, create clone at or maybe move to position of fox
  - within fox, track the position, send to each of the oranges?
  - either -30 to -60 or 30 to 60. Could choose number random, if/else to either multiply by -1 or not.
    - also

if go near cave, scared by bear? No, bear is deeper in cave.
collect berries, make sound if collect berries.
if go close to bear, drop berries?

## Implementation
### Movement
- I used [this](https://scratch.mit.edu/projects/959988092/editor) demo scratch assignment to figure out the best way to get movement to happen.
- I realized the fox didn't have a walking sprite, so I made one with the feet swapped. After trying it, it didn't look good. I checked back to the demo and realied there were 4 sprites (I had forgotten the in between steps ones). I made 2 more sprites for the in between steps, then added two more blocks of move code to each arrow key and it looked pretty good.

- I didn't like that the sprite kept moving so long after taking finger off of arrow key, so I lowered the distance moved and time delay between each sprite. This didn't work so I switched back. I'll live with it.

- I want to make a boundary to stop the fox from going into the sky. At first I tried using another sprite and setting it so that when the fox was in contact with it, it moved y -20 (which is how much the fox can move vertically in one click of the arrow key). However, it seems like the engine creates hitboxes based on color, because when I set the color of the box to clear it didn't work.
  - I then looked at the different code blocks and realized I could use the x and y position and create an absolute value function to set my boundary. I got out some pencil paper and planned the points I wanted to calculate the slope. Then I set the vertex. Once the function was written, I put it into the code blocks. It worked!
- I also wanted to make a boundary stopping the fox from going onto a rock on the right. I had to use and x= absolute value function which I had some trouble with. I used pencil and paper and eventually figured out I had to change the sign of the y value inside the absolute value. It worked. I then played with the slope and position a little to fine tune it.
- I wanted to make it look like the fox was getting bigger as it walked -y (to create perspective). I increased the size at points along the y axis.

### Collection
- I set a public variable displaying the number of berries collected.
- I made it increase anytime a key is touched and the fox is touching the berry.
- It collected more than one because I didn't hide it so there were multiple collisions.
- I made it get hidden when touched.
- I needed a way to reset the count, so I made it so that clicking the flag resets the game. It shows all the berries, sets the berry count to zero, and sets the starting position and size of the fox.
- Now to figure out how to make them drop when hit by the bear.
- I created a variable called Fox X Position and another called Fox Y Position and set it equal to the foxes x and y positions so that the berries would know where the fox position is.
- I sent a message when a key is pressed and the fox is touching the bear.
- I received the message by the berry, created a clone of the berry at the position of the fox.
- this resulted in receiving hundreds of berries.
- I made it so it would set the value of berries collected to zero when touching the bear.
- It still was saying many berries.
- I made it drop the berry a random value away from the fox.
- Now the issue is it makes a new clone every time a key is pressed while touching the bear. I need it to make a number of clones equal to how many berries are collected.
- I just realized its not setting the x and y of the clones, its moving the actual berry which I don't want.
  - I just didn't want that because it moved the position of the actual berry, but I realized I can just quickly add a default position that each berry returns to when I click the flag and I don't need to bother with clones
- I made this work by adding three code blocks to each berry:
  1. The first resets it to default position.
  2. The second
  2. The second checks for a signal from the fox for when the fox is touching the bear.


### Level Design
- backdrops:
- [Cave Tunnel](https://www.istockphoto.com/vector/dark-terrible-cave-game-illustration-background-gm1158457256-316452413)
