from random import randint

class Player:
    VERSION = "BET, Python, BET!!!"

    def betRequest(self, game_state):
        ONE_HIGH_CARD = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'Q' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'K' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'J'

        OTHER_HIGH_CARD = game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'A' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'Q' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'K' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'J'

        if ONE_HIGH_CARD or OTHER_HIGH_CARD:
            return game_state['players'][game_state['in_action']]['stack']/6
        elif game_state['players'][game_state['in_action']]['bet'] > 0:
            if randint(0,1) < 0.5:
                return game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet']
            else:
                return game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet'] + game_state['current_buy_in']
        elif randint(0,1) < 0.5:
            return 100
        else:
            return 0

    def showdown(self, game_state):
        pass

