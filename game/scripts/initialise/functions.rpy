init python:
    def EscolherFundo():
        global locations
        global ImagemFundo
        ImagemFundo = location.lower()
        ImagemFundo = ImagemFundo.replace(" ", "_")
        ImagemFundo = "images/places/" + ImagemFundo + ".png"

    def CharacterClick(loc):
        global Dialogue
        global Chain
        global UIreturn
        global ChoiceList
        ChoiceList = []
        for q in Dialogue:
            if q.participant == UIreturn:
                if q.location == loc or q.location == "":
                    ch = q.chain
                    sq = q.sequence
                    if sq == Chain[ch].sequence:
                        ChoiceList.append((q.initText, q.lbl))

    def DialogueTriggerCheck():
        global Dialogue
        global LavelsToCall
        LabelsToCall = []
        for q in Dialogue: 
            if q.check:
                LabelsToCall.append(q.lbl)