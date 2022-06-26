# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


label start:    
    $ Playing = True
    while Playing:
        window hide
        $ DialogueTriggerCheck
        while len (LabelsToCall) > 0:
            if renpy.has_label(LabelsToCall[0]):
                call expression LavelsToCall.pop(0)

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

        if clickType == "CharacterClick":
            $ CharacterClick(location)
            if ChoiceList <> []:
                $ LabelToCall = renpy.display_menu(ChoiceList, interact = True, screen = "choice")
                call expression LabelToCall

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