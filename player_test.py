import unittest
import json

from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_bet_request_should_return_integer(self):
        with open('HighCard.json') as json_file:
            game_state = json.load(json_file)
        self.assertIsInstance(self.player.betRequest(game_state), int)

    def test_high_card(self):
        with open('HighCard.json') as json_file:
            game_state = json.load(json_file)

        self.assertEqual(self.player.betRequest(game_state), 300)

if __name__ == '__main__':
    unittest.main()