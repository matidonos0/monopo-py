import random

class Box :
    box_instances = []

    def __init__(self, name, cost, color, kind, place, owner):
        self.name = name
        self.cost = cost
        self.color = color
        self.kind = kind
        self.place = place
        self.owner = owner
        Box.box_instances.append(self)

class Player :
    player_count = 0
    player_instances = []

    def __init__(self, name) :
        self.name = name
        self.status = 1 #ubication in the board
        self.balance = 1500 #money
        self.story = [0] #where has the player been
        self.total_laps = 0 #laps around the board
        Player.player_instances.append(self)
        Player.player_count += 1

    def roll_dices(player) :
        throw = random.randint(1, 6) + random.randint(1, 6)
        player.status = player.status ++ throw
        if player.status > 40 :
            player.status = player.status - 40
            player.balance += 200
            player.total_laps += 1
            player.story.append(player.status)
        else :
            player.story.append(player.status)
        return print(throw, player.status, player.total_laps)

    def reset_player(player) : 
        player.status = 1
        player.balance = 1500
        player.story = [0]
        return print('success!',player.story)