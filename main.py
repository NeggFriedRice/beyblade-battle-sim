import random

class BeyBlade:
    def __init__(self, name):
        self.name = name
        self.strength = self.statRand()
        self.strength_modifier = self.modifierRand()
        self.speed = self.statRand()
        self.speed_modifier = self.modifierRand()
        self.stamina = self.statRand()
        self.stamina_modifier = self.modifierRand()
        self.total_stats = self.get_total_stats()
        self.money = 0
        self.playing = True
        
    def modifierRand(self):
        return (random.randint(10, 20)) / 10
    
    def statRand(self):
        return random.randint(70, 100)
    
    def get_total_strength(self):
        return self.strength * self.strength_modifier
    
    def get_total_speed(self):
        return self.speed * self.speed_modifier
    
    def get_total_stamina(self):
        return self.stamina * self.stamina_modifier
    
    def get_total_stats(self):
        return round(self.strength * self.strength_modifier + self.speed * self.speed_modifier + self.stamina * self.stamina_modifier)

    def present_beyblade(self):
        print(f"Here is your new BeyBlade {self.name.capitalize()} with a total power of {self.total_stats}")

def menu():
    while player.playing == True:
        choice = input("What would you like to do?\n[1] Check BeyBlade stats\n[2] Check Upgrade Shop\n[3] Battle\n")
        if choice == "1":
            print(f"Your BeyBlade stats:\nStrength: {player.strength}\nSpeed: {player.speed}\nStamina: {player.stamina}")    

player = BeyBlade(input("What would you like to name your BeyBlade?\n"))
player.present_beyblade()
menu()


