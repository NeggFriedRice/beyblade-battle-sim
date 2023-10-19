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
        self.upgrades_count = 1
        
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
    shop_visit = 1
    strength_random_price = random.randint(12, 48)
    speed_random_price = random.randint(12, 48)
    stamina_random_price = random.randint(12, 48)
    
    def show_upgrades():
        print(f''' ** Welcome to the UPGRADES shop! **
[A] Strength stat upgrade: {Upgrades.strength_random_price} dollars
[B] Speed stat upgrade: {Upgrades.speed_random_price} dollars
[C] Stamina stat upgrade: {Upgrades.stamina_random_price} dollars

You can only upgrade once before each battle!''')
        Upgrades.shop_visit -= 1

    def buy_upgrade(input):
        if player.upgrades_count >= 1:
            if input == "A":
                player.strength += random.randint(23, 55)
                print("You bought A")
                player.upgrades_count -= 1
                player.money -= Upgrades.strength_random_price
        else:
            print("You don't have any upgrade slots available!")

def menu():
    while player.playing == True:
        hud()
        choice = input("")
        if choice == "1":
            print(f"Your BeyBlade stats:\nStrength: {player.strength}\nSpeed: {player.speed}\nStamina: {player.stamina}\n\n(Stat modifiers are hidden)\nYou have one {player.upgrades_count} upgrade slot available!\n")
        elif choice == "2":
            if Upgrades.shop_visit > 0:
                Upgrades.show_upgrades()
            else:
                print("You already visited the shop!")
        elif choice == "3":
            pass
        elif choice == "A":
            Upgrades.buy_upgrade(choice)


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def hud():
    print(f'''
===================================================================
Rounds left: {player.rounds_to_play}   |   Total BeyBlade power: {player.get_total_stats()}   |   Money: {player.money}''')
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


