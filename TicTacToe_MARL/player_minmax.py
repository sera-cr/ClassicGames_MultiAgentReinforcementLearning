from gymnasium.spaces import Discrete
from player import Player


class PlayerMinMax(Player):

    def choose_action(self, action_space: Discrete, action_mask: list[int], state_key: int) -> int:
        pass
