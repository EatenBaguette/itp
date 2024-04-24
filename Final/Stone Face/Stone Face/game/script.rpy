# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("San Kisos")
define c = Character("Coimazu")
define k = Character("Kili")


# The game starts here.

label start:
    scene bg alcove
    show young san kisos
    with dissolve

    window show dissolve

    "San Kisos was found as a boy whimpering in the alcove within an old oak tree near the Alipona village."

    "Nobody knew anything about him, and he didn’t tell anyone (if he even remembered). But he had the mark of the eclipse on his hand, for which many village members shunned him."

    scene bg boat wigwam
    show young family
    with dissolve

    window show dissolve

    "Except, one father, the main healer of the village, decided to raise him along with his child, Coimazu. They became like brothers."

    scene bg wigwam interior
    show card crafter
    with dissolve

    window show dissolve

    "The village card-crafter, trained in the magics of the world, knew that San Kisos had the potential to become a very powerful mage... "
    hide card crafter
    show obsidian knife at truecenter
    extend "yet San Kisos never showed any interest in card-making or wielding, preferring to stick to the obsidian knife."

    "He was trained as a fighter and taught to hunt and defend the tribe."

    scene bg forest
    show san kisos neutral at right
    show fox walking at left
    with dissolve

    "Animals around San Kisos tended to help him, even if they weren’t trained."

    show fox walking at center with move
    show fox sitting

    "Oddly, the only person in the village who noticed was Old Qitu, the village shaman. Everyone else seemed to move their attention away any time they saw it, as if their attention was a fish slipping out of the hands..."


label bad_news:

    scene bg town center with dissolve
    show coimazu happy
    show san kisos happy at right

    window show dissolve

    "Some years later..."

    show kili sad at left
    show san Kisos unsatisfied at right


    # These display lines of dialogue.

    k "Question?"

    s "Answer."

    # This ends the game.

    return
