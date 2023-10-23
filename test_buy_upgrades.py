from unittest.mock import MagicMock
from colorama import Fore, Back, Style

colres = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
blue = Fore.BLUE
magenta = Fore.MAGENTA
white = Fore.WHITE
bright = Style.BRIGHT

##########################################################################################################
# buy_upgrades function objects used for testing
# Mock BeyBlade object
mock_beyblade = MagicMock()
mock_beyblade.strength = 100

# Mock player object
mock_player = MagicMock()
mock_player.upgrades_count = 1
mock_player.shop_visit = 1
mock_player.money = 200
mock_player.money_target = 250
mock_player.wins = 2
mock_player.beyblade = mock_beyblade

##########################################################################################################
# buy_upgrades function - Test 1 - Expect "You don't have enough money!" (Upgrade cost > self.money)
# Giving upgrade a set price ($250) above self.money ($200) to test else statement
strength_random_price = 250

def test_buy_upgrades1(self, price):
    if self.money >= price:
        print(green + "You bought a " + colres + red + "STRENGTH " + colres + green + "upgrade!\n\n")
        self.upgrades_count -= 1
        self.shop_visit = 0
        self.money -= price
    else:
        print(green + "You don't have enough money!\n" + colres)

# Expected result = "You don't have enough money!"
test_buy_upgrades1(mock_player, strength_random_price)
# Actual result = "You don't have enough money!"

##########################################################################################################
# buy_upgrades Test 2 - Expect upgrade bought, strength stat to increase, upgrades_count to reduce by 1, shop_visit count to reset to 0

# Giving upgrades a set price ($100) below self.money ($200) to test successful upgrade buy
strength_random_price = 100

def test_buy_upgrades2(self, price):
    if self.money >= price:
        self.beyblade.strength += 50 # Set stat increase to +50 (as original function uses random int)
        print(green + "You bought a " + colres + red + "STRENGTH " + colres + green + "upgrade!\n")
        self.upgrades_count -= 1
        self.shop_visit = 0
        self.money -= price
    else:
        print(green + "You don't have enough money!\n" + colres)

# Expected result = "You bought a STRENGTH upgrade", self.upgrades_count = 0, self.shop_visit = 0, self.money = 100, 
test_buy_upgrades2(mock_player, strength_random_price)
print(mock_player.__dict__)
# Actual result = "You bought a STRENGTH upgrade", self.upgrades_count = 0, self.shop_visit = 0, self.money = 100
print(mock_player.beyblade.__dict__)
# Actual result = self.beyblade.strength = 150