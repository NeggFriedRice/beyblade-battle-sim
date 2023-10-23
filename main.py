from art import *
from classes import *
from functions import *
    
# Main
subprocess.call(['tput', 'reset'])
intro_banner()
player = Player()
try:
    Dialogue.intro(player)
    Dialogue.name_beyblade(player)
    Dialogue.present_beyblade(player)
    Dialogue.rules(player)
    Menu.menu(player)
except KeyboardInterrupt:
    Dialogue.quit_game()