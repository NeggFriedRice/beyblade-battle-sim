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
        self.rounds_to_play = 3
        
    def modifierRand(self):
        return (random.randint(10, 20)) / 10
    
    def statRand(self):
        return random.randint(80, 100)
    
    # def get_total_strength(self):
    #     return self.strength * self.strength_modifier
    
    # def get_total_speed(self):
    #     return self.speed * self.speed_modifier
    
    # def get_total_stamina(self):
    #     return self.stamina * self.stamina_modifier
    
    def get_total_stats(self):
        return round(self.strength * self.strength_modifier + self.speed * self.speed_modifier + self.stamina * self.stamina_modifier)

    def present_beyblade(self):
        print(f"Here is your new BeyBlade ~ {self.name.capitalize()} ~ with a total power of {self.total_stats}")
        if self.strength_modifier > self.speed_modifier and self.strength_modifier > self.stamina_modifier:
            print(f"It appears that your BeyBlade favours STRENGTH upgrades!")
        elif self.speed_modifier > self.stamina_modifier:
            print(f"It appears that your BeyBlade favours SPEED upgrades!")
        else:
            print(f"It appears that your BeyBlade favours STAMINA upgrades!")
        
def menu():
    while player.playing == True:
        hud()
        choice = input("")
        if choice == "1":
            print(f"Your BeyBlade stats:\nStrength: {player.strength}\nSpeed: {player.speed}\nStamina: {player.stamina}\n(Stat modifiers are hidden)")


def hud():
    print(f'''
===================================================================
Rounds left: {player.rounds_to_play}   |   Total BeyBlade power: {player.total_stats}   |   Money: {player.money}''')
    print(f'''[1] Check BeyBlade Stats | [2] Go to Upgrade Store | [3] Battle
===================================================================\n''')    

player = BeyBlade(input("What would you like to name your BeyBlade?\n"))
# print(player.__dict__)
player.present_beyblade()
menu()


