screen buildUI():
    frame:
        xpadding 25
        ypadding 25
        xalign 1.0
        yalign 0.5
        has vbox
        label "Construir" xminimum 300
        for i, q in enumerate(Rooms):
            if (MC.cash >= q.cost) and (not q.unlocked):
                button:
                    text q.name
                    ypadding 6
                    xpadding 10
                    action SetVariable("clickType","Construir"), Return(i)