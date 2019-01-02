import argparse
from game_class import SwineEscape


parser = argparse.ArgumentParser(description = "Solve the swine escape game.")
parser.add_argument("-l", "--boardlength",
                    help = "Custom board length",
                    required=False,
                    default=12,
                    type=int)
parser.add_argument("-s", "--swinestart",
                    help = "Custom swine starting position",
                    required=False,
                    default=7,
                    type=int)
parser.add_argument("-b", "--butcherstart",
                    help = "Custom butcher starting position",
                    required=False,
                    default=1,
                    type=int)
parser.add_argument("-m", "--method",
                    help = "Solution method (either 'dp' or 'markov'). Default: dp",
                    required=False,
                    default='dp',
                    type=str)
argument = parser.parse_args()

print('\nSolving game using {}.'.format(argument.method))
game = SwineEscape(board_size=argument.boardlength,
                   swine_start=argument.swinestart,
                   butcher_start=argument.butcherstart)
print('\nBoard length: {}\nSwine start: {}\nButcher start: {}'.format(game.board_size,
                                                                      game.swine_start,
                                                                      game.butcher_start))

game.solve_game(argument.method)
print("Swine's chance of winning: {:.1f}%".format(game.winning_prob*100))
