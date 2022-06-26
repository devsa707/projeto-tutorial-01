# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

    # This ends the game.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    $ Playing = True
    while Playing:
        $ clickType = ""
        $ UIreturn = renpy.call_screen("mainUI")

        if clickType == "move":
            $ location = UIreturn

        if clickType == "cheat":
            $ MC.cash += UIreturn
        
        if clickType == "Construir":
            $ Rooms[UIreturn].unlocked = True
            $ MC.cash -= Rooms[UIreturn].cost

        if clickType == "mapOpen":
            call mapNav

        if clickType == "Clicky":
            call expression UIreturn
            
    return

label alterarLocal:
    python:
        TempMenu = []
        for q in Rooms:
            if q.unlocked:
                TempMenu.append((q.name, q.name))
        TempMenu.append(("Cancelar", -1))    
    $ renpy.say(None,"Onde você gostaria de ir?", interact=False)
    $ mover = renpy.display_menu(TempMenu)
    if not mover == -1:
        $ location = mover
    return

label comprarLocais:
    python:
        TempMenu = []
        for i, q in enumerate(Rooms):
            if (MC.cash >= q.cost) and (not q.unlocked):
                TempMenu.append((q.name, i))
        TempMenu.append(("Cancelar", -1))
    $ renpy.say(None,"Qual local você gostaria de comprar?", interact=False)
    $ builder = renpy.display_menu(TempMenu)
    if not builder == -1:
        $ Rooms[builder].unlocked = True
        $ MC.cash -= Rooms[builder].cost
    return