import settings as s

players = []

def create_players() :
    n_players = input('How many players?: ')
    for n in range(int(n_players)) :
        player = input('Name of the player ' + str(n + 1) + ' ')
        player = s.Player(str(player))
        players.append(player)
    return print(players)
