import numpy.random as npr
from gymnasium.spaces import Discrete
from player import Player


class PlayerTesting(Player):
    def __init__(self, n_actions: int, table: dict, roulette_wheel: bool = False):
        super().__init__(n_actions=n_actions)

        # Configuration
        self.roulette_wheel = roulette_wheel
        self.table = table

    def choose_action(self, action_space: Discrete, action_mask: list[int], state_key: int):
        if self.roulette_wheel:
            # Roulette wheel selection from genetic algorithms
            # obtain probabilities based on the q values
            sum_values = sum([v for k, v in self.table[f'{state_key}'].items() if action_mask[k] == 1])
            values_list = [(v if (action_mask[k] == 1 and v > 0.0) else 0.0)
                           for k, v in self.table[f'{state_key}'].items()]
            selection_probs = [abs(value / sum_values) for value in values_list]
            action = npr.choice(len(values_list), p=selection_probs)
        else:
            # From the dictionary of q-values, obtaining the index of the best q-value
            action_values_masked = {k: v for k, v in self.table[f'{state_key}'].items() if action_mask[k] == 1}
            max_q_value = max(action_values_masked.values())
            action = [k for k, v in action_values_masked.items() if v == max_q_value][0]

        return action
