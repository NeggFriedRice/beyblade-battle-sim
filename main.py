import random, time, sys, subprocess
from art import trophy, smiley, sad_smiley, intro_banner
from colorama import Fore, Back, Style

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def delay_print_slow(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

colres = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
blue = Fore.BLUE
magenta = Fore.MAGENTA
white = Fore.WHITE
bright = Style.BRIGHT
dim = Style.DIM

class Player:
    def __init__(self):
        self.name = ""
        self.beyblade = BeyBlade()
        self.money = 200
        self.playing = True
        self.win_counter = 0
        self.rounds_to_play = 3
        self.upgrades_count = 1
        self.opponents_count = 1
        self.shop_visit = 1
        self.money_target = 0

class BeyBlade:
    def __init__(self):
        self.name = ""
        self.strength = self.statRand()
        self.strength_modifier = self.modifierRand()
        self.speed = self.statRand()
        self.speed_modifier = self.modifierRand()
        self.stamina = self.statRand()
        self.stamina_modifier = self.modifierRand()
        self.total_stats = self.get_total_stats()
        self.stat_favour = ""

        
    def modifierRand(self):
        return (random.randint(10, 20)) / 10
    
    def statRand(self):
        return random.randint(85, 100)
    
    def get_total_stats(self):
        return round(self.strength * self.strength_modifier + self.speed * self.speed_modifier + self.stamina * self.stamina_modifier)

class Battle:
    def battle_lobby(self, opponent):
        delay_print(green + "Do you want to battle? (" + white + "Y" + green + " or " + white + "N" + green + ")\n" + colres)            
        try:
            battle_yes_no = input().lower()
            if battle_yes_no not in "yn":
                raise InputError
            if battle_yes_no == "y":
                Battle.battle(player, opponent)
            else:
                print("")

        except InputError:
            print(green + "This is not a valid selection" + colres)

    def battle(self, opponent):
        self.rounds_to_play -= 1
        self.opponents_count += 1
        self.upgrades_count += 1
        delay_print_slow(yellow + "\n============================= BATTLING ================================\n\n" + colres)
        if self.beyblade.get_total_stats() > opponent.beyblade.get_total_stats():
            self.shop_visit += 1
            self.win_counter += 1
            win_money = random.randint(25, 65)
            self.money += win_money
            delay_print(white + f"{self.beyblade.name.capitalize()} " + green + "has won the battle!\n" + colres)
            delay_print(green + f"You get ${win_money} for winning this round!\n\n" + colres)
        elif self.beyblade.get_total_stats() == opponent.beyblade.get_total_stats():
            self.shop_visit += 1
            self.rounds_to_play += 1
            delay_print(green + "It's a draw! No money awarded! You'll need to play an extra round!\n\n" + colres)
        else:
            lose_money = random.randint(5, 25)
            player.shop_visit += 1
            player.money -= lose_money
            delay_print(white + f"{self.beyblade.name.capitalize()} " + green + "has lost the battle!\n" + colres)
            delay_print(f"You give ${lose_money} for losing this round! :(\n\n" + colres)

class Opponent(Player):
    name_list = [
        "Ash Ketchum", 
        "Spock", 
        "Taylor Swift", 
        "Hagrid", 
        "Ron Weasley", 
        "John Howard",
        "Captain America",
        "Dwight Schrute",
        "Michael Scott",
        "Michael Cera",
        "Danny DeVito",
        "Edward Scissorhands",
        "Britney Spears",
        "Chris Phenalthamakhunam"
        ]
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        stats_list = [
            player.beyblade.strength,
            player.beyblade.speed,
            player.beyblade.stamina,
        ]
        player.opponents_count -= 1
        if player.rounds_to_play == 2:
            self.beyblade.strength = max(stats_list) * (1 + (random.randint(15, 30) / 100))
        elif player.rounds_to_play == 1:
            self.beyblade.strength = max(stats_list) * (1 + (random.randint(22, 30) / 100))

class Upgrades:
    strength_random_price = 0
    speed_random_price = 0
    stamina_random_price = 0

    def show_upgrades():
        subprocess.call(['tput', 'reset']) 
        Upgrades.strength_random_price = random.randint(12, 30)
        Upgrades.speed_random_price = random.randint(12, 30)
        Upgrades.stamina_random_price = random.randint(12, 30)
        delay_print(green + "** Welcome to the UPGRADES shop! **\n\n" + colres)
        print(green + "[" + colres + "A" + green + "] Buy " + red + "STRENGTH " + colres + green + f"stat upgrade: {Upgrades.strength_random_price} dollars" + colres)
        print(green + "[" + colres + "B" + green + "] Buy " + cyan + "SPEED " + colres + green + f"stat upgrade: {Upgrades.speed_random_price} dollars" + colres)
        print(green + "[" + colres + "C" + green + "] Buy " + magenta + "STAMINA " + colres + green + f"stat upgrade: {Upgrades.stamina_random_price} dollars\n" + colres)

        player.shop_visit -= 1

    def buy_upgrade(input):
        subprocess.call(['tput', 'reset'])
        if player.upgrades_count >= 1:
            if input.upper() == "A":
                player.beyblade.strength += random.randint(45, 65)
                delay_print(green + "You bought a " + colres + red + "STRENGTH " + colres + green + "upgrade!\n\n")
                player.upgrades_count -= 1
                player.shop_visit = 0
                player.money -= Upgrades.strength_random_price
            elif input.upper() == "B":
                player.beyblade.speed += random.randint(45, 65)
                delay_print(green + "You bought a " + colres + cyan + "SPEED " + colres + green + "upgrade!\n\n")
                player.upgrades_count -= 1
                player.shop_visit = 0
                player.money -= Upgrades.speed_random_price
            else:
                player.beyblade.stamina += random.randint(45, 65)
                delay_print(green + "You bought a " + colres + magenta + "STAMINA " + colres + green + "upgrade!\n\n")
                player.upgrades_count -= 1
                player.shop_visit = 0
                player.money -= Upgrades.stamina_random_price
        else:
            subprocess.call(['tput', 'reset'])
            delay_print(green + "Oops! You don't have any upgrade slots available!\n" + colres)

class Dialogue:
    def intro():
        welcome_message = (green + "Welcome to the 2023 Battle BeyBlade Bonanza!\n")
        delay_print(welcome_message)
        delay_print("Before we get started, could we please have your name for registration?\n" + colres)
        player.name = input()
        delay_print(green + f"\nThank you for registering " + white + bright + f"{player.name.capitalize()}" + colres + green + "! We are so glad to have you here!\n\nAs per the tournament rules, you will be renting one of our Tournament BeyBlades!\n")
        
    def name_beyblade():
        delay_print("What would you like to name your BeyBlade?\n" + colres)
        player.beyblade.name = input()

    def rules():
        player.money_target = random.randint(175, 235)

        delay_print(green + f'''
TOURNAMENT RULES:
- 3 round tournament
- To win you will need to win at least 2 out of 3 rounds AND
- Have {player.money_target} dollars left in the bank to fly home!
                    
Goodluck!\n\n''' + colres)

    def present_beyblade(self):
        delay_print(green + "\nHere is your Tournament BeyBlade " + white + bright + f"~ {self.beyblade.name.capitalize()} ~ " + green + "with a total power of " + white + bright + f"{self.beyblade.total_stats}!\n" + colres)
        if self.beyblade.strength_modifier > self.beyblade.speed_modifier and self.beyblade.strength_modifier > self.beyblade.stamina_modifier:
            self.beyblade.stat_favour = (red +"STRENGTH" + colres)
            delay_print(green + "It appears that your BeyBlade favours " + red + "STRENGTH " + green + "upgrades!\n" + colres)
        elif self.beyblade.speed_modifier > self.beyblade.stamina_modifier:
            self.beyblade.stat_favour = (cyan +"SPEED" + colres)
            delay_print(green + "It appears that your BeyBlade favours " + cyan + "SPEED " + green + "upgrades!\n" + colres)
        else:
            self.beyblade.stat_favour = (magenta +"STAMINA" + colres)
            delay_print(green + "It appears that your BeyBlade favours " + magenta + "STAMINA " + green + "upgrades!\n" + colres)
    
    def beyblade_stats():
        subprocess.call(['tput', 'reset'])
        delay_print(green + "Your BeyBlade stats:\n\n" + colres) 
        print(green + "Name: " + white + f"{player.beyblade.name}\n" + red + "STRENGTH: " + white + f"{player.beyblade.strength}\n" + cyan + "SPEED: " + white + f"{player.beyblade.speed}\n" + magenta + "STAMINA: " + white + f"{player.beyblade.stamina}\n" + green + "Total power: " + white + f"{player.beyblade.get_total_stats()}\n" + colres)
        delay_print(green + f"Your BeyBlade favours {player.beyblade.stat_favour} " + green + "upgrades\n(Your BeyBlade has hidden unique stat modifiers that we can't check!)\n\n" + colres)
        delay_print(green + "Go to the store to upgrade your stats!\n\n" + colres)

    def player_stats():
        subprocess.call(['tput', 'reset'])
        delay_print(green + "Player Information:\n\n" + colres) 
        print(green + "Name: " + white + f"{player.name.capitalize()}\n" + green + "BeyBlade: " + white + f"{player.beyblade.name.capitalize()}\n"+ green + "Money: " + white + f"{player.money}\n"+ green + "Money needed to get home: " + white + f"{player.money_target}\n" + green + "Wins: " + white + f"{player.win_counter}\n" + colres)

    def end_game():
        delay_print(yellow + "===================================================================\n\n" + colres + green + "That's the end of the tournament!\n")
        if player.win_counter >= 2 and player.money >= player.money_target:
            trophy(player)
            delay_print(green + "Congratulations! You take home the trophy!\nHave a safe flight home!\n\n" + colres)
        elif player.win_counter >= 2:
            trophy(player)
            delay_print(green + "Congratulations! You get the trophy but you don't have enough money to fly home!\nI've got an Auntie that runs a fish and chip shop in town if you need to make a bit of money..?\n\n" + colres)
        elif player.money >= player.money_target:
            smiley()
            delay_print(green + "Unfortunately you didn't win the tournament this time :(\nHave a safe flight home, we'll see you next time!\n\n" + colres)
        else:
            sad_smiley()
            delay_print(green + "Yikes, you didn't win the tournament and you don't have enough money to get home.\nMy brother has 6 children, I heard he's looking for a babysitter...\n\n" + colres)

    def quit_game():
        subprocess.call(['tput', 'reset'])
        print(green + "Thanks for playing, see you next time!")
        time.sleep(3)
        exit()
        
class InputError(Exception):
    pass

class Menu:
    def menu():
        while player.playing == True:
            if player.rounds_to_play == 0:
                Dialogue.end_game()
                break
            else:
                Menu.hud()
                try:
                    choice = input("")
                    if choice not in "1234abcq":
                        raise InputError()
                    if choice == "1":
                        Dialogue.beyblade_stats()
                    elif choice == "2":
                        if player.shop_visit > 0:
                            Upgrades.show_upgrades()
                        else:
                            delay_print(green + "Sorry, the shop has closed for the day!\n\n" + colres)
                    elif choice == "3":
                        subprocess.call(['tput', 'reset']) 
                        if player.opponents_count > 0:
                            opponent = Opponent(random.choice(Opponent.name_list))
                            delay_print(green + "Your opponent is " + colres + white + bright + f"{opponent.name}" + colres + green + ". Their BeyBlade has a total power of " + white + f"{opponent.beyblade.get_total_stats()}.\n" + colres)
                            Battle.battle_lobby(player, opponent)
                        else:
                            delay_print(green + f"You have to beat " + white + f"{opponent.name} " + green + "(Total power: " + white + f"{opponent.beyblade.get_total_stats()}" + green+ ") first before battling someone else!\n" + colres)
                            Battle.battle_lobby(player, opponent)
                    elif choice == "4":
                        Dialogue.player_stats()
                    elif choice.upper() == "Q":
                        Dialogue.quit_game()
                    elif choice.upper() == "A" or choice.upper() == "B" or choice.upper() == "C":
                        Upgrades.buy_upgrade(choice)
                except InputError:
                    print(green + "This is not a valid selection" + colres)
                    
    def hud():
        print(yellow + f'''=======================================================================
Rounds left: {player.rounds_to_play}   |   Total BeyBlade power: {player.beyblade.get_total_stats()}   |   Money: {player.money}\n''')
        print("[" + white + "1" + yellow + "] Check BeyBlade Stats | [" + white + "2" + yellow + "] Go to Upgrades Store | [" + white + "3" + yellow + "] Battle Lobby")
        print("[" + white + "4" + yellow + "] Check Player Info                                         [" + white + "Q" + yellow + "] Quit")
        print("=======================================================================" + colres) 
    
# Main
subprocess.call(['tput', 'reset'])
intro_banner()
player = Player()
Dialogue.intro()
Dialogue.name_beyblade()
Dialogue.present_beyblade(player)
Dialogue.rules()
Menu.menu()

