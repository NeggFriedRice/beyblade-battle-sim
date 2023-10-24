from unittest.mock import MagicMock
from classes import *

##########################################################################################################

# OBJECTS SETUP: buy_upgrades function objects used for testing
# Mock BeyBlade object
mock_beyblade = MagicMock()
mock_beyblade.strength = 100

# Mock player object
mock_player = MagicMock()
mock_player.upgrades_count = 1
mock_player.shop_visit = 1
mock_player.money = 200
mock_player.beyblade = mock_beyblade
##########################################################################################################

# FUNCTION TO TEST: test_buy_upgrades
def test_buy_upgrades(self, price):
    if self.money >= price:
        self.beyblade.strength += 50 # Set stat increase to +50 (as original function uses random int)
        print(green + "You bought a " + colres + red + "STRENGTH " + colres + green + "upgrade!\n\n")
        self.upgrades_count -= 1
        self.shop_visit = 0
        self.money -= price
    else:
        print(green + "You don't have enough money!\n" + colres)

##########################################################################################################

# Variables as input to test
strength_random_price1 = 250 # Upgrade cost higher than player money
strength_random_price2 = 100 # Upgrade cost lower than player money

##########################################################################################################

# Test 1
# Expect result: "You don't have enough money!"

test_buy_upgrades(mock_player, strength_random_price1)

# Actual result: "You don't have enough money!""

# Success

##########################################################################################################

# Test 2 
# Expected result: strength upgrade bought, strength stat to increase, upgrades_count to reduce by 1, shop_visit count to reset to 0
# Expected mock_player.__dict__: self.upgrades_count = 0, self.shop_visit = 0, self.money = 100
# Expected mock_player.beyblade.__dict__: self.beyblade.strength = 150

test_buy_upgrades(mock_player, strength_random_price2)

# Actual mock_player.__dict__: self.upgrades_count = 0, self.shop_visit = 0, self.money = 100
# Actual mock_player.beyblade.__dict__: self.beyblade.strength = 150

# Sucess
