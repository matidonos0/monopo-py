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
        self.box_instances.append(self)

class Player :
    #counter isnt working
    player_count = 0
    player_instances = []

    def __init__(self, name) :
        self.name = name
        self.status = 0
        self.balance = 1500
        self.story = [0]
        self.player_count += 1
        self.player_instances.append(self)

    def roll_dices(player) :
        throw = random.randint(1, 6) + random.randint(1, 6)
        player.status = player.status ++ throw
        player.story.append(player.status)
        return print(throw, player.status)

    def reset_player(player) : 
        player.status = 0
        player.balance = 1500
        player.story = [0]
        return print('success!',player.story)