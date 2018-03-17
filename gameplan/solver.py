from gameplan.frontier import Frontier
from gameplan.state import GameState
from heapq import heappop, heappush


class List():
    def __init__(self):
        self.entries = []

    def empty(self):
        return len(self.entries) == 0

    def __contains__(self, item):
        for entry in self.entries:
            if entry == item:
                return True
        return False

    def __str__(self):
        return str(self.entries)

    def append(self, entry):
        self.entries.append(entry)


class DFSFrontier(Frontier):
    def add_to(self, entry):
        self.entries.append(entry)

    def remove_from(self):
        last = self.entries[-1]
        self.entries = self.entries[:-1]
        return last


class BFSFrontier(Frontier):
    def add_to(self, entry):
        self.entries.append(entry)

    def remove_from(self):
        first = self.entries[0]
        self.entries = self.entries[1:]
        return first


class AstarFrontier(Frontier):
    def add_to(self, entry, priority=None):
        heappush(self.entries, (priority, entry))

    def remove_from(self):
        return heappop(self.entries)[1]

    def __contains__(self, item):
        for entry in self.entries:
            if entry[1] == item:
                return True
        return False


def solve(start_state: GameState, frontierClass, heuristic='how_many_wrong'):
    frontier = frontierClass()
    explored = List()
    priority = 0

    if frontierClass == AstarFrontier:
        priority = start_state.configuration.heuristic_value(heuristic)

    frontier.add_to(start_state, priority)

    while not frontier.empty():
        state = frontier.remove_from()
        explored.append(state)

        if frontierClass == AstarFrontier:
            priority = state.configuration.heuristic_value(heuristic)

        print(state)
        if state.is_goal():
            return state
        for i, neighbour in enumerate(state.neighbours()):
            if neighbour not in frontier and neighbour not in explored:
                frontier.add_to(neighbour, priority)
        print(len(explored.entries))

    return None
