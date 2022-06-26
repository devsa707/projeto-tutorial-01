screen clickies():
    for q in Objects:
        if q.location == location and q.isActive:
            imagebutton:
                idle q.icon
                hover q.icon
                focus_mask True
                action SetVariable("clickType","Clicky"), Return(q.func)