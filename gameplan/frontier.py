from collections import deque

class Frontier:
    def __init__(self):
        self.entries = deque()  # override this to use other type for entries
        self.items = set() # for fast checking

    def add_to(self, entry, priority=None):
        raise NotImplementedError

    def remove_from(self):
        raise NotImplementedError

    # def add_to_front(self, entry):
    #     self.entries = [entry] + self.entries
    #
    # def append(self, entry):
    #     self.entries.append(entry)
    #
    # def remove_last(self):
    #     last = self.entries[-1]
    #     self.entries = self.entries[:-1]
    #     return last
    #
    # def remove_first(self):
    #     first = self.entries[0]
    #     self.entries = self.entries[1:]
    #     return first

    def empty(self):
        return len(self.entries) == 0

    def __contains__(self, item):
        # for entry in self.entries:
        #     if entry == item:
        #         return True
        # return False
        return item in self.items

    def __str__(self):
        return str(self.entries)
