screen moveUI():
    frame:
        xpadding 25
        ypadding 25
        xalign 0.0
        yalign 0.5
        has vbox
        label "Local" xminimum 300
        for q in Rooms:
            if q.unlocked:
                button:
                    text q.name
                    ypadding 3
                    xpadding 14
                    action SetVariable("clickType","move"), Return(q.name)