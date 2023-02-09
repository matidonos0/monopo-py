import random

class Box :
    def __init__(self, name, cost, color, kind):
        self.name = name
        self.cost = cost
        self.color = color
        self.kind = kind

class Player :
    def __init__(self, name) :
        self.name = name
        self.status = 0
        self.balance = 1500
        self.story = [0]

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
        
