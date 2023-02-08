#settings.py
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

    def reset_player() : 
        Player.status = 0
        Player.balance = 1500
        Player.story = [0]
        return print('success!')
        
