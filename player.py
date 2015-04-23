from random import randint

class Player:
    VERSION = "Testing snake"

    def betRequest(self, game_state):
        if randint(0,1) < 0.5:
            return 100
        else:
            return 0

    def showdown(self, game_state):
        pass

