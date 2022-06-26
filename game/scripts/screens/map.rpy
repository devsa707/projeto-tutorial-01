screen map():
    add "/ui/map/mapbg.jpg"
    imagebutton:
        xpos 10
        ypos 10
        focus_mask True
        hover "/ui/map/mapa_icone.png"
        idle "/ui/map/mapa_icone.png"
        action SetVariable("clickType", "mapCancel"), Return(None)

    for q in Rooms:
        if q.unlocked:
            $ TempName = "/ui/map/mapa_" + q.local + ".png"
            imagebutton:
                idle TempName
                hover TempName
                focus_mask True
                action SetVariable("clickType","mapSelect"), Return(q.name)