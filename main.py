from art import *
from classes import *
from functions import *
    
# Main
subprocess.call(['tput', 'reset'])      # Clear screen before starting
intro_banner()
player = Player()                       # Create player object
try:                                    # Begin game and dialogue
    Dialogue.intro(player)
    Dialogue.name_beyblade(player)
    Dialogue.present_beyblade(player)
    Dialogue.rules(player)
    Menu.menu(player)
except KeyboardInterrupt:               # Player can gracefully exit at any time
    Dialogue.quit_game()