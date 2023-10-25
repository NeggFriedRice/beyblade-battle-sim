import random

from art import *
from colorama import Fore, Style
from functions import *


# Variable shortcuts for colorama styling
colres = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
blue = Fore.BLUE
magenta = Fore.MAGENTA
white = Fore.WHITE
bright = Style.BRIGHT


# Player object
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


# Beyblade object
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

    # Stat randomisers
    def modifierRand(self):
        return (random.randint(10, 16)) / 10

    def statRand(self):
        return random.randint(82, 95)

    # Total stats getter
    def get_total_stats(self):
        return round(self.strength
                     * self.strength_modifier
                     + self.speed
                     * self.speed_modifier
                     + self.stamina
                     * self.stamina_modifier)


# Battle class
class Battle:

    # Battle lobby that gives player opportunity to check opponent stats
    # and go back to the shop to upgrade
    def battle_lobby(self, opponent):
        delay_print(green + "Do you want to battle? (" + white + "Y" +
                    green + " or " + white + "N" + green + ")\n" +
                    colres)
        try:
            battle_yes_no = input().lower()
            if battle_yes_no not in "yn":
                raise InputError
            if battle_yes_no == "y":
                Battle.battle(self, opponent)
            else:
                print("")
        except InputError:
            clear_screen()
            print(green + "This is not a valid selection" + colres)

    # Battle mechanic
    def battle(self, opponent):
        # Subtracts 1 from number of rounds player needs to be play
        self.rounds_to_play -= 1
        # Allows player to refresh new opponent after battle
        self.opponents_count += 1
        # Allows player to buy another upgrade after battle
        self.upgrades_count = 1
        # Allows player to visit shop again after battle
        self.shop_visit = 1
        delay_print_slow(yellow + "\n============================= BATTLING"
                         " ================================\n\n" + colres)
        if (self.beyblade.get_total_stats() >
                opponent.beyblade.get_total_stats()):  # Win outcome
            # Add 1 to player win counter
            self.win_counter += 1
            # Randomise win awarded money
            win_money = random.randint(25, 65)
            # Add awarded money to player money
            self.money += win_money
            delay_print(white + f"{self.beyblade.name.capitalize()} " +
                        green + "has won the battle!\n" + colres)
            delay_print(green + f"You get ${win_money} for winning this "
                        "round!\n\n" + colres)
        elif (self.beyblade.get_total_stats() ==
                opponent.beyblade.get_total_stats()):  # Draw outcome
            self.rounds_to_play += 1
            delay_print(green + "It's a draw! No money awarded! You'll need"
                        " to play an extra round!\n\n" + colres)
        else:  # Lose outcome
            lose_money = random.randint(5, 25)
            self.money -= lose_money
            delay_print(white + f"{self.beyblade.name.capitalize()} " +
                        green + "has lost the battle!\n" + colres)
            delay_print(green + f"You give ${lose_money} for losing this"
                        "round! :(\n\n" + colres)


# Opponent object that inherits attributes from Player object; with added list
# for randomised opponent name
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

    def __init__(self, name, player):
        super().__init__()
        self.opponents_count -= 1
        self.name = name
        # Stat balancer as rounds progress to give opponent chance of higher
        # stats to nudge player into buying upgrade
        stats_list = [
            self.beyblade.strength,
            self.beyblade.speed,
            self.beyblade.stamina,
        ]
        if player.rounds_to_play == 2:
            self.beyblade.strength = max((max(stats_list)
                                          * (1 + (random.randint(15, 20)
                                             / 100))),
                                         150)
        elif player.rounds_to_play == 1:
            self.beyblade.strength = max(((max(stats_list)
                                           * (1 + (random.randint(20, 30)
                                              / 100)))),
                                         200)


class Upgrades:

    # Set upgrade prices to zero initially
    strength_random_price = 0
    speed_random_price = 0
    stamina_random_price = 0

    # Show upgrades to player
    def show_upgrades(self):
        clear_screen()
        upgrades_banner()
        # Subtract shop_visit counter by 1 to only allow player to visit shop
        # once per round
        self.shop_visit -= 1
        Upgrades.strength_random_price = random.randint(15, 35)
        Upgrades.speed_random_price = random.randint(15, 35)
        Upgrades.stamina_random_price = random.randint(15, 35)
        delay_print(green + "Welcome to the UPGRADES shop!\n\n" + colres)
        print(green + "[" + colres + "A" + green + "] Buy " + red +
              "STRENGTH " + colres + green + f"stat upgrade: "
              f"{Upgrades.strength_random_price} dollars" + colres)
        print(green + "[" + colres + "B" + green + "] Buy " + cyan + "SPEED "
              + colres + green +
              f"stat upgrade: {Upgrades.speed_random_price} dollars" + colres)
        print(green + "[" + colres + "C" + green + "] Buy " + magenta +
              "STAMINA " + colres + green + "stat upgrade:"
              f"{Upgrades.stamina_random_price} dollars\n" + colres)
        Menu.hud(self)
        choice = input("")
        if (choice.upper() == "A" or choice.upper() == "B" or
                choice.upper() == "C"):
            Upgrades.buy_upgrade(self, choice)
        else:
            raise InputError()

    def buy_upgrade(self, input):
        clear_screen()
        # Upgrade failsafe, upgrades_count check prevents user from buying
        # more than one upgrade per round
        if self.upgrades_count >= 1:
            if (input.upper() == "A" and self.money >=
                    Upgrades.strength_random_price):
                # Add random int to stat if bought
                upgrades_banner()
                self.beyblade.strength += random.randint(40, 65)
                delay_print(green + "You bought a " + colres + red +
                            "STRENGTH " + colres + green + "upgrade!\n\n")
                self.upgrades_count -= 1
                self.shop_visit = 0
                self.money -= Upgrades.strength_random_price
            elif (input.upper() == "B" and self.money >=
                    Upgrades.speed_random_price):
                self.beyblade.speed += random.randint(40, 65)
                upgrades_banner()
                delay_print(green + "You bought a " + colres + cyan +
                            "SPEED " + colres + green + "upgrade!\n\n")
                self.upgrades_count -= 1
                self.shop_visit = 0
                self.money -= Upgrades.speed_random_price
            elif self.money >= Upgrades.stamina_random_price:
                upgrades_banner()
                self.beyblade.stamina += random.randint(40, 65)
                delay_print(green + "You bought a " + colres + magenta +
                            "STAMINA " + colres + green + "upgrade!\n\n")
                self.upgrades_count -= 1
                self.shop_visit = 0
                self.money -= Upgrades.stamina_random_price
            else:
                upgrades_banner()
                delay_print(green + "You don't have enough money!\n" + colres)
        else:
            clear_screen()
            upgrades_banner()
            delay_print(green + "Oops! You don't have any upgrade slots "
                        "available!\n" + colres)


class Dialogue:

    # Welcome message
    def intro(self):
        welcome_message = (green + "Welcome to the 2023 Battle BeyBlade "
                           "Bonanza!\n")
        delay_print(welcome_message)
        delay_print("Before we get started, could we please have your name "
                    "for registration?\n" + colres)
        # Prompt player for name
        self.name = input()
        delay_print(green + f"\nThank you for registering " + white + bright +
                    f"{self.name.capitalize()}" + colres + green + "! We are "
                    "so glad to have you here!\n\nAs per the tournament rules"
                    ", you will be renting one of our Tournament "
                    "BeyBlades!\n")

    # Prompt player to name their BeyBlade
    def name_beyblade(self):
        delay_print("What would you like to name your BeyBlade?\n" + colres)
        self.beyblade.name = input()

    # Display rules to player
    def rules(self):
        self.money_target = random.randint(185, 255)
        delay_print(green + f'''
TOURNAMENT RULES:
- 3 round tournament
- To win you will need to win at least 2 out of 3 rounds AND
- Have {self.money_target} dollars left in the bank to fly home!

Goodluck!\n\n
''' + colres)

    # Display BeyBlade to player and state which stat upgrades the BeyBlade
    # benefits the most from (stat modifier with the highest multiplier)
    def present_beyblade(self):
        delay_print(green + "\nHere is your Tournament BeyBlade " + white +
                    bright + f"~ {self.beyblade.name.capitalize()} ~ " +
                    colres + green + "with a total power of " + white +
                    bright + f"{self.beyblade.total_stats}!\n" + colres)
        if (self.beyblade.strength_modifier > self.beyblade.speed_modifier and
                self.beyblade.strength_modifier >
                self.beyblade.stamina_modifier):
            self.beyblade.stat_favour = (red + "STRENGTH" + colres)
            delay_print(green + "It appears that your BeyBlade favours " +
                        red + "STRENGTH " + green + "upgrades!\n" + colres)
        elif self.beyblade.speed_modifier > self.beyblade.stamina_modifier:
            self.beyblade.stat_favour = (cyan + "SPEED" + colres)
            delay_print(green + "It appears that your BeyBlade favours " +
                        cyan + "SPEED " + green + "upgrades!\n" + colres)
        else:
            self.beyblade.stat_favour = (magenta + "STAMINA" + colres)
            delay_print(green + "It appears that your BeyBlade favours " +
                        magenta + "STAMINA " + green + "upgrades!\n" + colres)

    # BeyBlade stats info (name, strength stat, speed stat, stamina stat,
    # highest stat modifier)
    def beyblade_stats(self):
        clear_screen()
        stats_banner()
        delay_print(green + "Your BeyBlade stats:\n\n" + colres)
        print(green + "Name: " + white +
              f"{self.beyblade.name.capitalize()}\n" + red + "STRENGTH: " +
              white + f"{self.beyblade.strength}\n" + cyan + "SPEED: " +
              white + f"{self.beyblade.speed}\n" + magenta + "STAMINA: " +
              white + f"{self.beyblade.stamina}\n" + green +
              "Total power: " + white +
              f"{self.beyblade.get_total_stats()}\n" + colres)
        delay_print(green + "Your BeyBlade favours "
                    f"{self.beyblade.stat_favour} " + green + "upgrades\n"
                    "(Your BeyBlade has hidden unique stat modifiers that we "
                    "can't check!)\n\n" + colres)
        delay_print(green + "Go to the store to upgrade your stats!\n\n" +
                    colres)

    # Player stats info (name, BeyBlade name, money, money needed to get home,
    # number of wins)
    def player_stats(self):
        clear_screen()
        player_info_banner()
        delay_print(green + "Player Information:\n\n" + colres)
        print(green + "Name: " + white + f"{self.name.capitalize()}\n" +
              green + "BeyBlade: " + white +
              f"{self.beyblade.name.capitalize()}\n" + green + "Money: " +
              white + f"{self.money}\n" + green + "Money needed to get home:" +
              white + f" {self.money_target}\n" + green + "Wins: " + white +
              f"{self.win_counter}\n" + colres)

    def end_game_stats(self):
        print(green + "Here are your end game stats: ")
        print(green + "Name: " + white + f"{self.name}" + colres)
        print(green + "BeyBlade: " + white +
              f"{self.beyblade.name.capitalize()}" + colres)
        print(red + "Strength: " + white + f"{self.beyblade.strength}" +
              colres)
        print(cyan + "Speed: " + white + f"{self.beyblade.speed}" + colres)
        print(magenta + "Stamina: " + white + f"{self.beyblade.stamina}\n" +
              colres)
        print(red + "Strength Modifier: " + white +
              f"{self.beyblade.strength_modifier}" + colres)
        print(cyan + "Speed Modifier: " + white +
              f"{self.beyblade.speed_modifier}" + colres)
        print(magenta + "Stamina Modifier: " + white +
              f"{self.beyblade.stamina_modifier}\n" + colres)
        print(green + "Wins: " + white + f"{self.win_counter}" + colres)
        print(green + "Money: " + white + f"{self.money}\n" + colres)
        Menu.end_game_option()

    # End game dialogue
    def end_game(self):
        clear_screen()
        finish_banner()
        delay_print(yellow + "==============================================="
                    "====================\n\n" + colres + green +
                    "That's the end of the tournament!\n")
        # Display different message based on player end game stats
        if self.win_counter >= 2 and self.money >= self.money_target:
            trophy(self)
            delay_print(green + "Congratulations! You take home the trophy!\n"
                        "Have a safe flight home!\n\n" + colres)
            Dialogue.end_game_stats(self)
            Menu.end_game_option()
        elif self.win_counter >= 2:
            trophy(self)
            delay_print(green + "Congratulations! You get the trophy but you "
                        "don't have enough money to fly home!\nI've got an "
                        "Auntie that runs a fish and chip shop in town if "
                        "you need to make a bit of money..?\n\n" + colres)
            Dialogue.end_game_stats(self)
            Menu.end_game_option()
        elif self.money >= self.money_target:
            smiley()
            delay_print(green + "Unfortunately you didn't win the tournament "
                        "this time :(\nHave a safe flight home, we'll see "
                        "you next time!\n\n" + colres)
            Dialogue.end_game_stats(self)
            Menu.end_game_option()
        else:
            sad_smiley()
            delay_print(green + "Yikes, you didn't win the tournament and "
                        "you don't have enough money to get home.\nMy "
                        "brother has 6 children, I heard he's looking for a "
                        "babysitter...\n\n" + colres)
            Dialogue.end_game_stats(self)
            Menu.end_game_option()

    # Quit game goodbye message
    def quit_game():
        clear_screen()
        thankyou_banner()
        print(green + "Thanks for playing, see you next time!")
        time.sleep(3)
        exit()


# Exception handling
class InputError(Exception):

    clear_screen()
    print("This is not a valid input")


# Menu class
class Menu:

    def menu(self):
        while self.playing is True:
            # menu function checks after each input if end game requirements
            # satisfied (rounds_to_play == 0)
            if self.rounds_to_play == 0:
                Dialogue.end_game(self)
                break
            else:
                # If game is still in progress then HUD will show
                Menu.hud(self)
                try:
                    # Check player input and call function based on selection
                    choice = input("")
                    if choice not in "1234q":
                        raise InputError()
                    if choice == "1":  # BeyBlade stats
                        Dialogue.beyblade_stats(self)
                    elif choice == "2":  # Show upgrade store options
                        if self.shop_visit > 0:
                            Upgrades.show_upgrades(self)
                        # Only allow 1 shop visit per round, if no shop visits
                        # available show below message
                        else:
                            clear_screen()
                            upgrades_banner()
                            delay_print(green + "Sorry, the shop has closed "
                                        "for the day!\n\n" + colres)
                    elif choice == "3":
                        clear_screen()
                        battle_banner()
                        if self.opponents_count > 0:
                            # Create new opponent object if player enters the
                            # battle lobby
                            opponent = (Opponent(random.choice(
                                        Opponent.name_list), self))
                            delay_print(green + "Your opponent is " + colres +
                                        white + bright + f"{opponent.name}" +
                                        colres + green + ". Their BeyBlade "
                                        "has a total power of " + white +
                                        (f"{opponent.beyblade.get_total_stats()}")
                                        ".\n" + colres)
                            # Subtract 1 from player opponent count; ensures
                            # player cannot refresh opponent until win/lose
                            # against current opponent
                            self.opponents_count -= 1
                            Battle.battle_lobby(self, opponent)
                        else:
                            delay_print(green + f"You have to beat " + white +
                                        f"{opponent.name} " + green +
                                        "(Total power: " + white +
                                        f"{opponent.beyblade.get_total_stats()}"
                                        + green + ") first before battling "
                                        "someone else!\n" + colres)
                            Battle.battle_lobby(self, opponent)
                    # Show player stats
                    elif choice == "4":
                        Dialogue.player_stats(self)
                    # Quit game function
                    elif choice.upper() == "Q":
                        Dialogue.quit_game()
                except InputError:
                    clear_screen()
                    print(green + "This is not a valid selection" + colres)
                except KeyboardInterrupt:
                    Dialogue.quit_game()

    # Show menu HUD and info to player
    def hud(self):
        print(yellow +
              "=============================================================="
              "=========\n"
              f"Rounds left: {self.rounds_to_play}   |   Total BeyBlade "
              f"power: {self.beyblade.get_total_stats()}   |   Money: "
              f"{self.money}\n")
        print("[" + white + "1" + yellow + "] Check BeyBlade Stats | [" +
              white + "2" + yellow + "] Go to Upgrades Store | [" + white +
              "3" + yellow + "] Battle Lobby")
        print("[" + white + "4" + yellow + "] Check Player Info"
              "                                         [" + white + "Q" +
              yellow + "] Quit")
        print("=============================================================="
              "=========" + colres)

    # Exit game option after tournament ends
    def end_game_option():
        while True:
            choice = input(green + "[" + white + "Q" + green + "] to exit the "
                           "game: \n")
            if choice.lower() == "q":
                Dialogue.quit_game()
                break
