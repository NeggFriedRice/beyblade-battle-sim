from colorama import Fore, Back, Style
yellow = Fore.YELLOW
colres = Style.RESET_ALL

def trophy(player):
    print (yellow + f'''
        .-=========-.
        \'-=======-'/
        _|   .=.   |_
       ((|    1    |))
        \|   /|\   |/
         \__ '`' __/
           _`) (`_
         _/_______\_
        /___________\ 
        {player.name} and {player.beyblade.name}
        2023 Champions\n''' + colres)

# Trophy art courtesy of jgs: https://github.com/joeky888/ASCII-Art-collection/blob/master/t/trophy.txt

def smiley():
    print (yellow + """
      _.-'''''-._
    .'  _     _  '.
   /   (o)   (o)   |
  |                 |
  |  \           /  |
   \  '.       .'  /
    '.  `'---'`  .'
      '-._____.-' \n""" + colres)
    
def sad_smiley():
    print (yellow + """
      _.-'''''-._
    .'  _     _  '.
   /   (o)   (o)   |
  |            `'   |
   \    .----._    .'  
    '. '       ' .'
      '-._____.-' \n""" + colres)