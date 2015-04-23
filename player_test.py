import unittest
import json

from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        with open('HighCard.json') as json_file:
            self.game_state = json.load(json_file)

    def test_bet_request_should_return_integer(self):
        self.assertIsInstance(self.player.betRequest(self.game_state), int)

if __name__ == '__main__':
    unittest.main()