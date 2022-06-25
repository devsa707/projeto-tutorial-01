label mapNav:
    $ UIreturn = renpy.call_screen("map")
    if clickType == "mapCancel":
        return
    if clickType == "mapSelect":
        $ location = UIreturn
    
    return