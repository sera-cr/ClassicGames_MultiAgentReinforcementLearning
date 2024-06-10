import random

from game import Game
from player_testing import PlayerTesting


class GameTesting(Game):
    def __init__(self, environment, render_mode: str, player0: PlayerTesting, player1: PlayerTesting):
        """
        Configurations
        :param render_mode: 'rgb_array' for training or multiple game testing. 'human' for rendering game
        :param player0: First player of the game. Testing version.
        :param player1: Second player of the game. Testing version.
        """
        super().__init__(render_mode=render_mode, environment=environment)
        self.player0 = player0
        self.player1 = player1
        self.coins_flipped = 0
        self.p0_wins = 0
        self.p1_wins = 0
        self.p0_name = None
        self.p1_name = None

    def choose_starting_player(self):
        """
        Select the starting player. player0 always will be the starting one.
        Chosen by flipping coin.
        :return:
        """
        if random.uniform(0, 100) > 51:
            temp = self.player0
            self.player0 = self.player1
            self.player1 = temp

            temp = self.p0_wins
            self.p0_wins = self.p1_wins
            self.p1_wins = temp

            self.coins_flipped += 1

    def play_game(self):
        self.p0_name = self.env.agents[0]
        self.p1_name = self.env.agents[1]
        for agent in self.env.agent_iter():
            observation, reward, terminated, truncated, info = self.env.last()

            state_key = self.get_hash()

            if terminated or truncated:
                action = None
                self.env.step(action)
                if agent == self.p0_name and reward > 0:
                    self.p0_wins += 1
                elif agent == self.p1_name and reward > 0:
                    self.p1_wins += 1
            else:
                if agent == self.env.agents[0]:
                    current_player = self.player0
                else:
                    current_player = self.player1

                current_player.check_state_key(state_key)
                action = current_player.choose_action(self.env.action_space(agent),
                                                      observation['action_mask'],
                                                      state_key)
                self.env.step(action)

