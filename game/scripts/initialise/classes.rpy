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