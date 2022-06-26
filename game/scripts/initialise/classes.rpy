init python:   
    class place(object):
        def __init__(self,name,cost,unlocked):
            self.name = name
            self.cost = cost
            self.unlocked = unlocked
        
        @property
        def local(self):
            llocal = self.name.lower()
            llocal = llocal.replace(" ", "_")
            return llocal
    
    class person(object):
        def __init__(self,name,weight,cash):
            self.name = name
            self.weight = weight
            self.cash = cash

    MC = person("Trouxa",82,100)


    Rooms = []
    Rooms.append(place("Cozinha",0,True))
    Rooms.append(place("Quarto",0,True))
    Rooms.append(place("Corredor",0,True))
    Rooms.append(place("Sala de Estar",1000,False))
    Rooms.append(place("Adega",5000,False))
    Rooms.append(place("Salão de Festas",15000,False))
    Rooms.append(place("Sala Luxuosa",80000,False))
    Rooms.append(place("Quintal",4000,False))
    Rooms.append(place("Jardim",9000,False))
    Rooms.append(place("Quarto para visitas",7000,False))
    Rooms.append(place("Piscina",25000,False))

    location = Rooms[1].name

    class NPerson(object):
        def __init__(self, forename, surname, location, love):
            self.forename = forename
            self.surname = surname
            self.location = location
            self.love = love
        
        @property
        def name(self):
            return "{} {}".format(self.forename, self.surname)

        @property
        def avatar(self):
            mood = "_neutro.png"
            if -10 < self.love < 10:
                mood = "_neutro.png"
            elif self.love <= -10:
                mood = "_surpresa.png"
            elif self.love >= 10:
                mood = "_feliz.png"
            return "ui/avatars/" + self.forename + "/" + self.forename + mood
    
    Npc = []
    Npc.append(NPerson("Lili","Navarro", "Cozinha", 0))
    Npc.append(NPerson("Lili","Navarro", "Quarto", 0))
    Npc.append(NPerson("Lili","Navarro", "Sala de Estar", 0))
    Npc.append(NPerson("Lili","Navarro", "Cozinha", 0))
    Npc.append(NPerson("Lili","Navarro", "Cozinha", 0))
    Npc.append(NPerson("Lili","Navarro", "Cozinha", 0))
    Npc.append(NPerson("Lili","Navarro", "Cozinha", 0))

    class DIALOGUE(object):
        def __init__(self, location, participant, chain, sequence, lbl):
            self.location = location
            self.participant = participant
            self.chain = chain
            self.sequence = sequence
            self.lbl = lbl
        
        @property
        def check():
            global location
            global Npc
            for q in Npc:
                if q.forename == self.forename or self.forename == "":
                    if q.location == location == location:
                        return True
            return False
                    
    Dialogue = []
    
    Dialogue.append(DIALOGUE("","",0,0,"chain_0_0"))
    Dialogue.append(DIALOGUE("Cozinha","Danielle",0,1,"chain_0_1"))
    Dialogue.append(DIALOGUE("Quarto","",0,2,"chain_0_2"))
    
    class CHAIN(object):
        def __init__(self, evnt, sequence, isActive):
            self.evnt = evnt
            self.sequence = sequence
            self.isActive = isActive

    Chain = []
    for t in range(0,9):
        Chain.append(CHAIN([],0,False))
    
    for i,q in enumerate(Dialogue):
        tempInt = q.chain
        Chain[tempInt].evnt.append(i)