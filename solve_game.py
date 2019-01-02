import sys
from game_class import SwineEscape

# If no arguments are given, use the default game setup.
if len(sys.argv) == 1:
    board_size = 12
    swine_start = 7
    butcher_start = 1
else:
    try:
        board_size = int(sys.argv[1])
        swine_start = int(sys.argv[2])
        butcher_start = int(sys.argv[3])
    except ValueError:
        print('Error: game setup should be expressed as 3 integer numbers indicating board size, swine start, and butcher start.')
        sys.exit()

game = SwineEscape(board_size=board_size, swine_start=swine_start, butcher_start=butcher_start)
print('\nBoard length: {}\nSwine start: {}\nButcher start: {}'.format(game.board_size,
                                                                      game.swine_start,
                                                                      game.butcher_start))
game.solve_game('dp')
print('Winning probability (DP): {:.1f}%'.format(game.winning_prob*100))
game.solve_game('markov')
print('Winning probability (Markov chain): {:.1f}%'.format(game.winning_prob*100))
