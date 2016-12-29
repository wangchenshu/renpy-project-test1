# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define w = Character("Walter", color="#c8c8ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "It's a story with pictures.":
             jump vn

        "It's a walter game.":
             jump walter

    label vn:
        e "It's a story with pictures and music."
        jump walter

    label walter:
        scene bg room
        play music "1.ogg"
        show walter happy
        w "This is walter test, and play music canon."
        ".:. Good Ending."

    # This ends the game.

    return
