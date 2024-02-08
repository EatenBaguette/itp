# itp
# Scratch Documentation

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
2. if hit by bear or spike, drop oranges.
  - using the counter to track how many oranges, create clone at or maybe move to position of fox
  - within fox, track the position, send to each of the oranges?
  - either -30 to -60 or 30 to 60. Could choose number random, if/else to either multiply by -1 or not.
    - also

if go near cave, scared by bear? No, bear is deeper in cave.
collect berries, make sound if collect berries.

### Level Design
- When starting, the bear should be seen for a second entering the cave, dropping a berry near the entrance.
- When entering the cave, the bear should be waiting at the end. It turns and keep going. This should only happen the first time.
  - when enter tunnel, check game progress. If less than value, show bear scene. If greater than value, no bear scene. When bear performs scene, it updates the game progress.
- when continuing through the cave, the bear is waiting. It stands up on its legs, then goes down. The cave rumbles. A red blink indicates where spikes are about to fall. Instructions will be given so the player knows to click space to change to sitting to take up less space and avoid the spikes.
- being hit by a spike gets rid of 1 of 3 lives and causes the fox to drop its berries.



## Implementation
### Movement
- I used [this](https://scratch.mit.edu/projects/959988092/editor) demo scratch assignment to figure out the best way to get movement to happen.
- I realized the fox didn't have a walking sprite, so I made one with the feet swapped. After trying it, it didn't look good. I checked back to the demo and realized there were 4 sprites (I had forgotten the in between steps ones). I made 2 more sprites for the in between steps, then added two more blocks of move code to each arrow key and it looked pretty good.

- I didn't like that the sprite kept moving so long after taking finger off of arrow key, so I lowered the distance moved and time delay between each sprite. This didn't work so I switched back. I'll live with it.

- I want to make a boundary to stop the fox from going into the sky. At first I tried using another sprite and setting it so that when the fox was in contact with it, it moved y -20 (which is how much the fox can move vertically in one click of the arrow key). However, it seems like the engine creates hitboxes based on color, because when I set the color of the box to clear it didn't work.
  - I then looked at the different code blocks and realized I could use the x and y position and create an absolute value function to set my boundary. I got out some pencil paper and planned the points I wanted to calculate the slope. Then I set the vertex. Once the function was written, I put it into the code blocks. It worked!
- I also wanted to make a boundary stopping the fox from going onto a rock on the right. I had to use and x= absolute value function which I had some trouble with. I used pencil and paper and eventually figured out I had to change the sign of the y value inside the absolute value. It worked. I then played with the slope and position a little to fine tune it.
- I wanted to make it look like the fox was getting bigger as it walked -y (to create perspective). I increased the size at points along the y axis.
  - I turned off the size change feature because I didn't feel like implementing it for all of the sprites.

- While working on the background change, I got annoyed at how slow the fox moves.
  - I added two variables, vertical and horizontal movement speed. At start (when flag is clicked), they are set normally.
  - I replaced each instance of move x/y with the movement speed. I multiplied by -1 for the opposite directions.
  - shift isn't an option so I picked z. If z is pressed while an arrow key is pressed, it multiplies the movement speed by a variable called movement speed multiplier.
  - it doesn't work because it triggers all of the "when any key pressed" blocks.
  - I'll keep the multiplier for coding so I can move around faster but wait on implementing sprinting for players.
- I fixed an issue where the fox kept the order of cycling costumes. I want it to reset every time the fox walks so that clicking space after walking always first makes the fox sit rather than lay. I added a set costume variable value to each arrow key.

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
  - I didn't want that because it moved the position of the actual berry, but I realized I can just quickly add a default position that each berry returns to when I click the flag and I don't need to bother with clones
- I made this work by adding three code blocks to each berry:
  1. The first resets it to default position.
  2. The second checks for a signal from the fox for when the fox is touching the bear.
  3. The third sets the count to 0, checks if it's hidden, then sets a random y and x position within a range of the fox (as if the fox dropped the berries), then shows it and sets hidden to 0.
- now the issue is it moves every berry when touching the bear, even if it wasn't collected. I need to add a check.
- I created a variable called Hidden for each berry. It sets to 1 when it is hidden. When touching the bear, it checks if the berry is hidden (meaning it was collected) before dropping it.
- I duplicated the boundary of tunnel 1 to tunnel 2.


### Level Design
- backdrops:
  - [Cave Tunnel](https://www.istockphoto.com/vector/dark-terrible-cave-game-illustration-background-gm1158457256-316452413)
- I placed some berries leading towards the cave entrance.
- I want to switch backdrops when the fox is close to the cave entrance.
- Adding code based on position to the stage affects all backdrops, so I need to add a check for each backdrop. I checked to see if the backdrop is arctic before using the fox position to change to the cave tunnel.
  - I added a transition. If in mountain, if the fox is close to the cave entrance, it fades the background and hides the fox, switches the background, moves the fox, shows the fox, and un-fades the background.
- I added a cave stinger that plays when entering the cave.
- I need to add a starting background when flag is clicked (Mountain).
- I need to move the boundary code that doesn't let the fox move into the sky to each background, otherwise it exists in all backgrounds. I already have a variable for the fox's position. I need to figure out how to get the fox position to move out of the boundary when the code block isn't actually in the fox sprite. Probably sending a message.
  - I had trouble with the right boundary and it was because I forgot to replace the change x position with my variable fox x position.
  - I also had trouble with the boundary feeling lower than before near the cave. I adjusted the slope of the boundary function to correct this.
- I realized I need to hide uncollected berries from other backgrounds.
  - I broadcast a message whenever switching to a new section. I received it and made it hide berries from other sections, and show berries for which hidden does not equal 1 (that means they were collected).
  - It's not working. I checked the hidden variable and it's 1 even when the berry is showing. I realized it wasn't working because I forgot to set the hidden variable to 0 on start. They were all considered hidden. Now it works.
- For some reason clicking any button re-triggers the switching to tunnel background. I'm gonna have to find a work around.
  - The issue was that I had an extra else as part of a condition for the transitioning between backgrounds that caused the current background to re-trigger every key press. I fixed it by combining the conditions of each if with an and, and getting rid of the else.
- There's an issue where switching quickly between backgrounds plays both audios.
  - I added a stop all sounds just before each background audio is played.
- I added a game progress variable so that certain "cutscenes" wouldn't re-trigger every time the fox enters a background.
- I added a 2nd tunnel, and a bear cutscene where it slams down. I sequenced the bear using move and costume changes. When it slammed down, I made it rumble the screen.
  - I added 2 backdrops called rumble and I offset them. I sent a signal to the backdrops that when they receive it, the backdrop switches quickly between the two rumble backdrops, making it wobble.
- I designed a spike sprite with a highlit version and regular version.
- I made the spikes flash while rumbling, then fall.
- I added a life variable and sprites and set the sprites so that they are hidden at different stages of the life variable. When less than 3, the first is hidden.
- I'm having trouble getting the spike to register as colliding with the fox if the fox isn't moving.
  - I set it to repeat a certain number of times. Now it loses too much life. To solve this, I made a time period of invulnerability by recieving lose life, setting invulnerable to 1, waiting, then setting back to 0. To register and lose life, the spike has to both be touching the fox and invulnerable variable has to be 0. This worked.
