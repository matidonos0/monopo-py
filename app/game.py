import settings as s
import boxes as boxes

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
                playable = False #then endgame function
                break
            elif instruction == 'dice':
                s.Player.player_instances[turn].roll_dices()
                player_place = s.Player.player_instances[turn].status
                current_box = s.Box.box_instances[player_place - 1]
                print('Dices from : ' + s.Player.player_instances[turn].name)
                print('You are in : ' + current_box.name + ' and the owner is : ' + str(current_box.owner))
                if current_box.owner == None :
                    print('---------')
                    print('This property has no owner, you can buy it or itll get auctioned ')
                    print('\n')
                    box_decision = input('Please choose buy or auction...')
                    if box_decision == 'buy' :
                        print('you bought the property')
                        pass
                    elif box_decision == 'auction':
                        print('The property will get auctioned')
                        pass
                pass
            #elif instruction == 'story':
            #    print(s.Player.player_instances[turn].story)
            #    pass
            else:
                break
