screen topBar():
    imagebutton:
        xpos 25
        ypos 100
        hover "/ui/map/mapa_icone.png"
        idle "/ui/map/mapa_icone.png"
        action SetVariable("clickType", "mapOpen"), Return(None)

    frame:
        xpos 0
        ypos 0
        xsize 1280
        ysize 75
        hbox:
            xsize 1280            
            text location
            button:
                xalign 0.9
                text "R$" +str(MC.cash) 
                action SetVariable("clickType","cheat"), Return(1000)