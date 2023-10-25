
from unittest.mock import MagicMock
from art import *
from classes import *


##########################################################################################################

# OBJECTS SETUP: 
mock_beyblade = MagicMock()
mock_beyblade.name = "Mock_Beyblade"

# Mock player 1 object for Test 1 (Win tournament and fly home: Wins >= 2 and player money >= player money target)
mock_player1 = MagicMock()
mock_player1.beyblade = mock_beyblade
mock_player1.name = "Mock Player 1"
mock_player1.money = 250
mock_player1.money_target = 201
mock_player1.win_counter = 2

# Mock player 2 object for Test 2 (Lose tournament and fly home: Wins < 2 and player money >= player money target)
mock_player2 = MagicMock()
mock_player2.beyblade = mock_beyblade
mock_player2.name = "Mock Player 2"
mock_player2.money = 201
mock_player2.money_target = 200
mock_player2.win_counter = 1

# Mock player 3 object for Test 3 (Win tournament and can't fly home: Wins >= 2 and player money < player money target)
mock_player3 = MagicMock()
mock_player3.beyblade = mock_beyblade
mock_player3.name = "Mock Player 3"
mock_player3.money = 199
mock_player3.money_target = 200
mock_player3.win_counter = 2

# Mock player 4 object for Test 4 (Lose tournament and can't fly home: Wins < 2 and player money < player money target)
mock_player4 = MagicMock()
mock_player4.beyblade = mock_beyblade
mock_player4.name = "Mock Player 4"
mock_player4.money = 199
mock_player4.money_target = 200
mock_player4.win_counter = 1

##########################################################################################################

# FUNCTION TO TEST: test_end_game:

def test_end_game(self):
    print(yellow + "===================================================================\n\n" + colres + green + "That's the end of the tournament!\n")
    # Display different message based on player end game stats
    if self.win_counter >= 2 and self.money >= self.money_target:
        trophy(self)
        print(green + "Congratulations! You take home the trophy!\nHave a safe flight home!\n\n" + colres)
        # Menu.end_game_option() # Need to remove end_game_option to stop game ending after test
    elif self.win_counter >= 2:
        trophy(self)
        print(green + "Congratulations! You get the trophy but you don't have enough money to fly home!\nI've got an Auntie that runs a fish and chip shop in town if you need to make a bit of money..?\n\n" + colres)
        # Menu.end_game_option() # Need to remove end_game_option to stop game ending after test
    elif self.money >= self.money_target:
        smiley()
        print(green + "Unfortunately you didn't win the tournament this time :(\nHave a safe flight home, we'll see you next time!\n\n" + colres)
        # Menu.end_game_option() # Need to remove end_game_option to stop game ending after test
    else:
        sad_smiley()
        print(green + "Yikes, you didn't win the tournament and you don't have enough money to get home.\nMy brother has 6 children, I heard he's looking for a babysitter...\n\n" + colres)
        # Menu.end_game_option() # Need to remove end_game_option to stop game ending after test

##########################################################################################################

# Test 1
# Expected result: Trophy ASCII art + "Congratulations! You take home the trophy!" + "Have a safe flight home!"
test_end_game(mock_player1)
# Actual result: Trophy ASCII art + "Congratulations! You take home the trophy!" + "Have a safe flight home!"

# Success

##########################################################################################################

# Test 2
# Expected result: Smiley face ASCII art + "Unfortunately you didn't win the tournament this time :(" + "Have a safe flight home, we'll see you next time!"
test_end_game(mock_player2)
# Actual result: Smiley face ASCII art + "Unfortunately you didn't win the tournament this time :(" + "Have a safe flight home, we'll see you next time!"

# Success

##########################################################################################################

# Test 3
# Expected result: Trophy ASCII art + "Congratulations! You get the trophy but you don't have enough money to fly home!" + "I've got an Auntie that runs a fish and chip shop in town if you need to make a bit of money..?"
test_end_game(mock_player3)
# Actual result: Trophy ASCII art + "Congratulations! You get the trophy but you don't have enough money to fly home!" + "I've got an Auntie that runs a fish and chip shop in town if you need to make a bit of money..?"

# Success

##########################################################################################################

# Test 4
# Expected result: Sad face ASCII art + "Yikes, you didn't win the tournament and you don't have enough money to get home." + "My brother has 6 children, I heard he's looking for a babysitter..."
test_end_game(mock_player4)
# Actual result: Sad face ASCII art + "Yikes, you didn't win the tournament and you don't have enough money to get home." + "My brother has 6 children, I heard he's looking for a babysitter..."

# Success
