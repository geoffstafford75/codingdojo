import pets

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_nane = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print("Walking the pet")
        self.pet.play()
        return self
    def feed(self):
        print("Feeding Pet")
        self.pet.eat()
    def bathe(self):
        print("Walking the pet")
        self.pet.noise()


dog1 = Pet("Dogie", "Bulldog","flips 'n shit")
dog2 = Pet("DogieDoo", "Boxer","flips 'n shit")

NinjaGeoff = Ninja("Geoff","Stafford","bones","YummyFood",dog1)
NinjaGeoff.feed()
NinjaGeoff.walk()
NinjaGeoff.bathe()




# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
