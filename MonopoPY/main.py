import game 
import boxes

game.new_game()
game.play()

print(game.s.Box.box_instances)
print('-----------------')
print('\n')
print(game.s.Player.player_instances)
print('-----------------')
print('\n')
print(game.s.Player.player_count)