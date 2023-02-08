import random

import settings
import boxes

def start_game() :
    #crear tablero
    #crear jugadores
    #crear banco
    pass

def roll_dice(player) :
    throw = random.randint(1, 6)
    player.status = player.status ++ throw
    player.story.append(player.status)
    return print(throw, player.status)

def buy_box(player, box) :
    pass

def auction_box(box) :
    pass