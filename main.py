import random, time, sys

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
    
    def get_total_stats(self):
        return round(self.strength * self.strength_modifier + self.speed * self.speed_modifier + self.stamina * self.stamina_modifier)

    def present_beyblade(self):
        delay_print(f"Here is your new BeyBlade ~ {self.name.capitalize()} ~ with a total power of {self.total_stats}!\n")
        if self.strength_modifier > self.speed_modifier and self.strength_modifier > self.stamina_modifier:
            delay_print(f"It appears that your BeyBlade favours STRENGTH upgrades!\n")
        elif self.speed_modifier > self.stamina_modifier:
            delay_print(f"It appears that your BeyBlade favours SPEED upgrades!\n")
        else:
            delay_print(f"It appears that your BeyBlade favours STAMINA upgrades!\n")

class Upgrades:
    # Show upgrades and cost
    shop_refresh = 1
    def show_upgrades():
        strength_random_price = random.randint(12, 48)
        speed_random_price = random.randint(12, 48)
        stamina_random_price = random.randint(12, 48)
        print(f''' ** Welcome to the UPGRADES shop! **
[A] Strength stat upgrade: {strength_random_price}
[B] Speed stat upgrade: {speed_random_price}
[C] Stamina stat upgrade: {stamina_random_price}\n''')
        Upgrades.shop_refresh -= 1

def menu():
    while player.playing == True:
        hud()
        choice = input("")
        if choice == "1":
            print(f"Your BeyBlade stats:\nStrength: {player.strength}\nSpeed: {player.speed}\nStamina: {player.stamina}\n(Stat modifiers are hidden)\n")
        if choice == "2":
            if Upgrades.shop_refresh > 0:
                Upgrades.show_upgrades()
            else:
                print("You already visited the shop!")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def hud():
    print(f'''
===================================================================
Rounds left: {player.rounds_to_play}   |   Total BeyBlade power: {player.total_stats}   |   Money: {player.money}''')
    print(f'''[1] Check BeyBlade Stats | [2] Go to Upgrade Store | [3] Battle
===================================================================\n''')    

def intro():
    welcome_message = "Welcome to the 2023 Battle BeyBlade Bonanza!\n"
    delay_print(welcome_message)
    # print()
    delay_print("Before we get started, could we please have your name for registration?\n")
    player_name = input()
    delay_print(f"Thank you for registering {player_name}! We are so glad to have you here!\n")

def name_beyblade():
    delay_print("What would you like to name your BeyBlade?\n")

# Main
intro()
name_beyblade()
player = BeyBlade(input())
player.present_beyblade()
menu()


