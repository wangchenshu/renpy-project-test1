# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    image logo right = Image("images/logo.jpg", xalign=1.0)
    image walter happy = "char/walter.jpg"
    image eileen happy = im.Scale("char/eileen.jpg", 300, 300)
    image side walter happy = "char/side_walter.jpg"
    image side eileen happy = "char/side_eileen.jpg"
    image jack = im.Grayscale("char/jack.jpg")
    image jack_snowflakes = SnowBlossom("char/jack.jpg")

    define eileen = Character("Eileen", color="#c8ffc8", image="eileen")
    define walter = Character("Walter", color="#c8c8ff", image="walter")

    $ relation = 0
    $ pi = 3.1415926535

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show logo right
    show eileen happy

    show jack:
        #xpos 0      # ATL 屬性陳述 (xpos)：圖片的 x 軸位置，與螢幕的 x 軸 = 0 座標點重合
        #ypos 50
        ease 1.0 pos (0.0, 1.0)      # ATL 屬性陳述 (pos)：移動圖片到指定位置
        anchor (0.0, 1.0)   # ATL 屬性陳述 (anchor)：移動錨點到指定位置
        ease 2.0 alpha 0.5
        ease 2.0 rotate 30
        ease 1.0 align (0.0, 4.0)
        ease 1.0 align (0.0, 3.0)
        ease 1.0 align (0.0, 2.0)
        ease 1.0 align (0.0, 1.0)
        linear 2.0 rotate -30
        repeat

    # These display lines of dialogue.

    "Hello, world."

    eileen "You've created a new Ren'Py game."

    eileen "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "It's a story with pictures.":
             jump vn

        "It's a walter game.":
             jump walter

    label vn:
        eileen "It's a story with pictures and music."
        jump walter

    label walter:
        scene bg room
        #play music "1.ogg"
        voice "1.ogg"
        show walter happy
        walter "This is walter test, and play music canon."
        ".:. Good Ending."
        show eileen happy at topright #behind walter with dissolve
        eileen "hello, i am eileen"
        hide walter
        walter "walter go home"
    # This ends the game.

    menu:
        "Hello, 1 + 1 = ?"

        "11":
            eileen "sorry"
            $ relation = 4

        "1+1":
            eileen "wrong answer"
            $ relation = 5

        "2":
            eileen "nice work"
            $ relation = 6

    eileen "Thansk for your help."

    if relation == 1:
        walter "gift [relation]"
    elif relation == 2:
        walter "gift [relation]"
    else:
        walter "gift [relation]"

    "{i}PI{/i} is {color=#0f0}{u}[pi:.3]{/u}{/color}{nw}"
    return
