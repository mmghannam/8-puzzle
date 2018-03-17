class Frontier:
    def __init__(self):
        self.entries = []

    def add_to_front(self, entry):
        self.entries = [entry] + self.entries

    def append(self, entry):
        self.entries.append(entry)

    def remove_last(self):
        last = self.entries[-1]
        self.entries = self.entries[:-1]
        return last

    def remove_first(self):
        first = self.entries[0]
        self.entries = self.entries[1:]
        return first

    def empty(self):
        return len(self.entries) == 0

    def __str__(self):
        return str(self.entries)
