from gameplan.frontier import Frontier
from gameplan.state import GameState


class SearchAlgorithm:
    def __init__(self, frontier):
        self.frontier = frontier

    def add_to(self, entry):
        raise NotImplementedError

    def remove_from(self):
        raise NotImplementedError


class DFS(SearchAlgorithm):
    def add_to(self, entry):
        self.frontier.append(entry)

    def remove_from(self):
        return self.frontier.remove_last()


class BFS(SearchAlgorithm):
    def add_to(self, entry):
        self.frontier.append(entry)

    def remove_from(self):
        return self.frontier.remove_first()


def solve(start_state: GameState, alg):
    frontier = Frontier()
    explored = set()

    search_alg = alg(frontier)

    while not frontier.empty():
        state = search_alg.remove_from()
        explored.add(state)

        if state.is_goal():
            return state

        for neighbour in state.neighbours():
            if neighbour not in frontier or neighbour not in explored:
                alg.add_to(neighbour)
