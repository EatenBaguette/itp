# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("San Kisos")
define c = Character("Coimazu")
define k = Character("Kili")

transform kili:
    zoom 0.8
    yoffset 50
    yzoom 1.1

transform foxSitPos:
    xalign 0.75

image coimazu_kisos_move:
    contains: #coimazu sad left
        "images/coimazu sad left.png"
        xalign 0.5
        yalign 1.0
        linear 1.5 xalign 0.2
        linear 2.0 xalign 0.2
        alpha 0.0
        xalign 0.5
        pause 3.0
        alpha 1.0
    contains: #coimazu sad right
        "images/coimazu sad right.png"
        alpha 0.0
        xalign 0.2
        yalign 1.0
        pause 3.5
        alpha 1.0
        linear 3.0 xalign 0.5
        alpha 0.0
    contains: #san Kisos
        "images/san kisos sad left.png"
        xalign 1.0
        yalign 1.0
        linear 0.3 xalign 1.0
        alpha 0.0
    contains:
        "images/San Kisos Left Neutral.png"
        xalign 1.0
        yalign 1.0
        alpha 0.0
        pause 0.3
        alpha 1.0
        linear 1.2 xalign 0.3
        linear 2.0 xalign 0.4
        alpha 0.0
        xalign 1.0
        pause 3.0
        alpha 1.0
    contains: #san kisos sad right
        "images/San Kisos Right Neutral.png"
        alpha 0.0
        xalign 0.4
        yalign 1.0
        pause 3.5
        alpha 1.0
        linear 3.0 xalign 1.0
        alpha 0.0


# The game starts here.

label start:
    menu:
        "Where to?"
        "Village Level":
            jump village_level

        "Intro":
            jump intro


label intro:
    scene bg alcove
    show young san kisos
    with dissolve

    window show dissolve

    "San Kisos was found as a boy whimpering in the alcove within
an old oak tree near the Alipona village."

    "Nobody knew anything about him, and he didn’t tell anyone
(if he even remembered). But he had the mark of the eclipse on
his hand, for which many village members shunned him."

    scene bg boat wigwam
    show young family
    with dissolve

    window show dissolve

    "Except, one father, the main healer of the village, decided
to raise him along with his child, Coimazu. They became like brothers."

    scene bg wigwam interior
    show card crafter
    with dissolve

    window show dissolve

    "The village card-crafter, trained in the magics of the world,
    knew that San Kisos had the potential to become a very powerful mage... "
    hide card crafter
    show obsidian knife at truecenter
    extend "yet San Kisos never showed any interest in card-making or
wielding, preferring to stick to the obsidian knife."

    "He was trained as a fighter and taught to hunt and defend the tribe."

    scene bg forest
    show san kisos happy left at right
    show fox walking at left
    with dissolve

    "Animals around San Kisos tended to help him, even if they weren’t trained."

    show fox walking at foxSitPos with move


    show fox sitting

    "Oddly, the only person in the village who noticed was Old Qitu,
the village shaman. Everyone else seemed to move their attention away
any time they saw it, as if their attention was a fish slipping out of the hands..."


label bad_news:

    scene bg town center with dissolve
    show coimazu happy right at center
    show san kisos happy left at right
    show kili angry at offscreenleft, kili

    window show dissolve

    "Some years later..."

    show kili at left with move
    show san kisos neutral left behind kili
    show coimazu neutral left behind kili, san

    c "Uhh, Kili... What are you doing back already?"

    k "There’s… something terrible happened!"

    c "{i}Oh no..{/i} Is everyone.. Is my father alright?"

    show kili sad
    k "I... I don't think so."

    show san sad
    c "I'm going then!"

    hide san
    hide coimazu
    show coimazu_kisos_move behind kili
    s "Wait!"

    s "Coimazu, they need you here at the village.
If… if anything happened to Ikidod…"

    s "You’ve been training as a healer. What if wolves attack
and you’re gone, or what if you get hurt too? Let me go."

    c "Ok... Kili, were any others injured?"

    k "Yes, but not physically. You should prepare for soul healing."

    hide coimazu_kisos_move
    show san kisos left sad at right
    show coimazu sad at center behind kili:
        pause 1.0
        linear 1.0 xalign -1.0
    c "I understand."

    k "He... He was turned to stone."

    show san surprised
    show kili thinking
    k "We didn’t remember what happened, just woke up feeling not
ourselves, and Ikidod was a statue."

    show san sad
    show kili angry
    k "If
you’re going, you should make a glider. I think it might have
something to do with the Itikandu."

    show san neutral
    s "The Itikandu... Ok, I'll gather what I need. Thank you Kili."

    show san right at offscreenright with move

    jump village_level

label village_level:
    scene bg village level
    show san sprite:
        xalign 0.25
        yalign 0.50
    pause
