import settings as s
import boxes

def new_game() :
    create_players()
    print('Game Ready')
    #create who throws first

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
        for turn in range(0, len(s.Player.player_instances)) :
            instruction = input('Instruction :')
            if instruction == 'end':
                playable = False
                break
            elif instruction == 'dice':
                #create turns like for and rotate the player instance
                s.Player.player_instances[turn].roll_dices()
                print('dados de : ' + s.Player.player_instances[turn].name)
                pass
            #elif instruction == 'story':
            #    print(s.Player.player_instances[turn].story)
            #    pass
            else:
                break
