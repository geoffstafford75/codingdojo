class Pet:
    def __init__( self,name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
    def sleep(self):
        self.energy += 25
        print("Sleeping")
    def eat(self):
        self.energy +=5
        self.health +=10
        print("Yummy Yum")
    def play(self):
        self.health +=5
        print("Doing Flips n Shit")
    def noise(self):
        print("Bow wow wow, Yippy yo, Yippy ye")