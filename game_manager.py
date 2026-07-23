from game_state import GameState


class GameManager:

    def __init__(self):

        self.state = GameState.WAIT_FOR_NEW_LEVEL

    def set_state(self, state):

        self.state = state

    def get_state(self):

        return self.state