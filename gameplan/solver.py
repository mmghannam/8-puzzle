from gameplan.frontier import Frontier
from gameplan.state import GameState
from heapq import heappop, heappush
from time import time


class List():
    def __init__(self):
        self.entries = set()

    def empty(self):
        return len(self.entries) == 0

    def __contains__(self, item):
        # for entry in self.entries:
        #     if entry == item:
        #         return True
        # return False
        return item in self.entries

    def __str__(self):
        return str(self.entries)

    def append(self, entry):
        self.entries.add(entry)


class DFSFrontier(Frontier):
    def add_to(self, entry, priority=None):
        self.entries.append(entry)
        self.items.add(entry)

    def remove_from(self):
        # last = self.entries[-1]
        # self.entries = self.entries[:-1]

        last = self.entries.pop()
        self.items.remove(last)
        return last


class BFSFrontier(Frontier):
    def add_to(self, entry, priority=None):
        self.entries.append(entry)
        self.items.add(entry)

    def remove_from(self):
        # first = self.entries[0]
        # self.entries = self.entries[1:]

        first = self.entries.popleft()
        self.items.remove(first)
        return first


class AstarFrontier(Frontier):
    def __init__(self):
        super(AstarFrontier, self).__init__()
        self.entries = []

    def add_to(self, entry, priority=0):
        heappush(self.entries, (priority, entry))

    def remove_from(self):
        entry_removed = heappop(self.entries)
        return entry_removed[1]

    def __contains__(self, item):
        for entry in self.entries:
            if entry[1] == item:
                return True
        return False


def print_path(goal, parent):
    temp = goal
    cost = 0
    depth = 0
    print('''\n##########
## Path ##
##########
    ''')
    print(goal[0])
    print('\n\t|\n\t|\n')
    while parent[temp]:
        depth += 1
        print('Heuristic = {}'.format(parent[temp][1]))
        cost += parent[temp][1]
        print(parent[temp][0])
        temp = parent[temp]
        print('\t|\n\t|\n')

    print('''\n################
   Start Here 
   Path cost={}
   Search depth={}
################
        '''.format(cost, depth))


def solve(start_state: GameState, frontierClass, heuristic='how_many_wrong', show_path=True):
    # f = open('progress.txt', 'a')
    start = time()
    frontier = frontierClass()
    explored = List()
    priority = 0
    n_priority = 0

    if frontierClass == AstarFrontier:
        priority = start_state.configuration.heuristic_value(heuristic)

    parent = {(start_state, priority): None}

    frontier.add_to(start_state, priority)

    while not frontier.empty():
        state = frontier.remove_from()
        explored.append(state)

        if frontierClass == AstarFrontier:
            priority = state.configuration.heuristic_value(heuristic)

        # print(state)
        if state.is_goal():
            print("\nstates explored =  {}".format(len(explored.entries)))
            print("\nrunning time =  {}".format(time() - start))
            if show_path:
                print_path((state, priority), parent)
            return state
        for i, neighbour in enumerate(state.neighbours()):
            if neighbour not in frontier and neighbour not in explored:
                frontier.add_to(neighbour, priority)
                if frontierClass == AstarFrontier:
                    n_priority = neighbour.configuration.heuristic_value(heuristic)
                parent[(neighbour, n_priority)] = (state, priority)

        if len(explored.entries) % 100 == 0:
            with open('progrs.txt', 'a') as f:
                f.write(str(len(explored.entries)) + " in explored\n")
                f.write(str(len(frontier.entries)) + " in frontier\n")
                f.write(str(time() - start) + " seconds\n\n")
    return None
