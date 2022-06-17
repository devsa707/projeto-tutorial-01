# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lili")


# The game starts here.

    # This ends the game.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg lecturehall

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sylvie blue giggle

    # These display lines of dialogue.

    l "Bom, acho que chegou a hora de começar a aprender não?."

    l "Mesmo que leve alguns anos, um dia espero que façamos um jogo e que ele seja incrível!"

    l "Bom Dia, [MC.name], vamos para o [location]"
    
    $ Playing = True
    while Playing:
        menu:
            "Dinheiro do [MC.name]: R$[MC.cash]"
            "Adicionar Dinheiro":
                $ MC.cash += 1000

    return
