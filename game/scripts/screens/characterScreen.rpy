screen Character_Screen():
    $ Char_X = 900
    for q in Npc:
        if q.location == location:
            imagebutton:
                idle q.avatar
                hover q.avatar
                xpos Char_X
                yalign 1.0
                focus_mask True
                action SetVariable("clickType","CharacterClick"), Return(q.forename)
            $ Char_X -= 200