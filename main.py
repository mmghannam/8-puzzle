from puzzle.puzzle import *
from gameplan.frontier import *

game = Puzzle(3, 3)
frontiers = {
    AstarFrontier: ['how_many_wrong', 'manhattan_distance', 'euclidean_distance', 'wrong_and_manhattan'],
    DFSFrontier: [''],
    BFSFrontier: ['']
}
for frontier in frontiers.keys():
    print("*********")
    print(frontier)
    print("*********")
    for heuristic in frontiers[frontier]:
        if heuristic:
            print("*********")
            print(heuristic)
            print("*********")
        game.solve(frontier, heuristic, show_path=True)
    print("-------------------------")
