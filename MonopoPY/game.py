import settings as s
import boxes

def new_game() :
    create_players()
    print('Game Ready')

def create_players() :
    n_players = input('How many players?: ')
    #this try except isnt working
    try :
        n_players = round(int(n_players))
    except:
        print('Please enter a number')
        n_players = input('How many players?: ')
    if n_players < 2 or n_players > 6 :
        print('Invalid player count, please choose a number between 2 and 6')
        n_players = input('How many players?: ')
    for n in range(int(n_players)) :
        player = input('Name of the player ' + str(n + 1) + ' ')
        player = s.Player(str(player))

def play() :
    playable = True
    while playable == True :
        instruction = input('Instruction :')
        if instruction == 'end':
            playable = False
            break
        elif instruction == 'dice':
            s.Player.player_instances[0].roll_dices()
            print('dados')
            pass
        else:
            break
