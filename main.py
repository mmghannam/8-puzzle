from puzzle.puzzle import *
from gameplan.frontier import *

game = Puzzle(3, 3)
print(game.solve(AstarFrontier, 'wrong_and_manhattan'))
