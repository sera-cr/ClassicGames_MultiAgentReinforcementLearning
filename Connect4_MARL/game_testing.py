import random

from game import Game
from player_testing import PlayerTesting


class GameTesting(Game):
    def __init__(self, render_mode: str, player1: PlayerTesting, player2: PlayerTesting):
        """
        Configurations
        :param render_mode: 'rgb_array' for training or multiple game testing. 'human' for rendering game
        :param player1: First player of the game. Testing version.
        :param player2: Second player of the game. Testing version.
        """
        super().__init__(render_mode=render_mode)
        self.player1 = player1
        self.player2 = player2
        self.coins_flipped = 0
        self.p1_wins = 0
        self.p2_wins = 0

    def choose_starting_player(self):
        """
        Select the starting player. Player1 always will be the starting one.
        Chosen by flipping coin.
        :return:
        """
        if random.uniform(0, 100) > 51:
            temp = self.player1
            self.player1 = self.player2
            self.player2 = temp

            temp = self.p1_wins
            self.p1_wins = self.p2_wins
            self.p2_wins = temp

            self.coins_flipped += 1

    def play_game(self):
        for agent in self.env.agent_iter():
            observation, reward, terminated, truncated, info = self.env.last()

            state_key = self.get_hash()

            if terminated or truncated:
                action = None
                self.env.step(action)
                if agent == 'player_1' and reward > 0:
                    self.p1_wins += 1
                elif agent == 'player_2' and reward > 0:
                    self.p2_wins += 1
            else:
                if agent == 'player_1':
                    current_player = self.player1
                else:
                    current_player = self.player2

                current_player.check_state_key(state_key)
                action = current_player.choose_action(self.env.action_space(agent),
                                                      observation['action_mask'],
                                                      state_key)
                self.env.step(action)

