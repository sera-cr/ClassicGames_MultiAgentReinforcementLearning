from abc import abstractmethod
from gymnasium.spaces import Discrete


class Player:
    def __init__(self, n_actions: int):
        """
        Configuration
        """
        self.table = {}
        self.n_actions = n_actions

    def check_state_key(self, state_key: int) -> bool:
        """
        Checks if the current state_key exists in table.
        If not, it will initialize it in the table.
        """
        if f'${state_key}' not in self.table.keys():
            self.table[f'{state_key}'] = {key: 0.1 for key in range(self.n_actions)}
            return False
        return True

    @abstractmethod
    def choose_action(self, action_space: Discrete, action_mask: list[int], state_key: int) -> int:
        """
        To be implemented. It should return an action based on the parameters
        and following a specific algorithm.

        :param action_space: Provided by PettingZoo environment. It must be Discrete
        :param action_mask List of n values with only 0 and 1
        :param state_key The state of the game hashed as integer
        """
        pass

    def get_qtable(self) -> dict:
        """
        Returns the Q-Table of the player.
        """
        return self.table
