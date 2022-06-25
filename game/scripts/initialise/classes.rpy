init python:   
    class place(object):
        def __init__(self,name,cost,unlocked):
            self.name = name
            self.cost = cost
            self.unlocked = unlocked
    
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
    
    Npc = []
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))
    Npc.append(NPerson("Danielle","Smith", "Cozinha", 0))

    class DIALOGUE(object):
        def __init__(self, location, participant, chain, sequence):
            self.location = location
            self.participant = participant
            self.chain = chain
            self.sequence = sequence
        
        @property
        def check():
            global location
            global Npc
            for q in Npc:
                if q.name = self.forename:
                    if q.location = location:
                        Return True
            Return False
                    