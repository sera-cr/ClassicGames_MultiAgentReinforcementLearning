import random
import numpy.random as npr
from player import Player


class PlayerTraining(Player):
    """
    Q-Table will be a dictionary with pairs key, value as:
    'state_key' => [0.0,0.0,0.0, ..., 0.0]
    being the value a list of 9 elements. Each index represents an action.

    List of actions:
    0 | 3 | 6
    1 | 4 | 7
    2 | 5 | 8
    """

    def __init__(self, alpha: float, gamma: float, epsilon: float, algorithm: int, roulette_wheel: bool = False):
        super().__init__()
        # Hyperparameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # Configuration
        self.roulette_wheel = roulette_wheel
        self.training_algorithm = algorithm

        self.next_action = None

    def choose_action(self, action_space, action_mask, state_key):
        self.check_state_key(state_key)

        if self.training_algorithm == 1 and self.next_action and action_mask[self.next_action] == 1:
            # SARSA needs to choose the next action before update
            # If the action has been chosen, use it if it's possible
            action = self.next_action
            self.next_action = None
        else:
            # If SARSA doesn't have a new action or
            # the algorithm doesn't require to choose the new one before update
            if self.roulette_wheel:
                # Roulette wheel selection from genetic algorithms
                # obtain probabilities based on the q values
                sum_values = sum([v for k, v in self.table[f'{state_key}'].items() if action_mask[k] == 1])
                values_list = [(v if (action_mask[k] == 1 and v > 0.0) else 0.0)
                               for k, v in self.table[f'{state_key}'].items()]
                selection_probs = [abs(value / sum_values) for value in values_list]
                action = npr.choice(len(values_list), p=selection_probs)
            else:
                if random.uniform(0, 1) < self.epsilon:
                    # Explore action space. Random action
                    action = action_space.sample(action_mask)
                else:
                    # From the dictionary of q-values, obtaining the index of the best q-value
                    action_values_masked = {k: v for k, v in self.table[f'{state_key}'].items() if action_mask[k] == 1}
                    max_q_value = max(action_values_masked.values())
                    action = [k for k, v in action_values_masked.items() if v == max_q_value][0]

        return action

    def update_q_values(self, state_key, action, reward, next_key, action_space, action_mask):
        if self.training_algorithm == 0:
            # Bellman equation algorithm
            old_value = self.table[f'{state_key}'][action]
            optimal_future_value = max(list(self.table[f'{next_key}'].values()))

            # Using bellman equation for obtaining the new q value and updating the value on the table
            new_value = (1 - self.alpha) * old_value + self.alpha * (float(reward) + self.gamma * optimal_future_value)
            self.table[f'{state_key}'][action] = new_value
        elif self.training_algorithm == 1:
            # SARSA algorithm
            if self.next_action is None:
                self.next_action = self.choose_action(action_space, action_mask, next_key)
            old_value = self.table[f'{state_key}'][action]
            next_value = self.table[f'{next_key}'][self.next_action]

            # SARSA equation
            new_value = (1 - self.alpha) * old_value + self.alpha * (float(reward) + self.gamma * next_value)
            self.table[f'{state_key}'][action] = new_value
