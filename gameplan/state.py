class GameState:
    def __init__(self, initial_conf):
        self.configuration = initial_conf

    def neighbours(self):
        raise NotImplementedError

    def is_goal(self):
        raise NotImplementedError


class Configuration:
    pass

