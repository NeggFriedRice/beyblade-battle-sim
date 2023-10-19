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
        self.money = 200
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
        hud()
        choice = input("")
        if choice == "1":
            print(f"Your BeyBlade stats:\nStrength: {player.strength}\nSpeed: {player.speed}\nStamina: {player.stamina}")

class Battle:
    rounds_to_play = 3

def hud():
    print(f'''
Rounds left: {Battle.rounds_to_play} | Total BeyBlade power: {player.total_stats} | Money: {player.money}
          ''')    

player = BeyBlade(input("What would you like to name your BeyBlade?\n"))
player.present_beyblade()
menu()


