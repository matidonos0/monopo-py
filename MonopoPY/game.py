import settings as s
import boxes

players = []

def new_game() :
    create_players()

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
        players.append(player)
    return [print(player.name) for player in players]