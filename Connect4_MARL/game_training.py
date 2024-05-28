import random
from game import Game
from player_training import PlayerTraining


class GameTraining(Game):
    def __init__(self, render_mode: str, player0: PlayerTraining, player1: PlayerTraining):
        """
                Configurations
                :param render_mode: 'rgb_array' for training or multiple game testing. 'human' for rendering game
                :param player0: First player of the game. Training version.
                :param player1: Second player of the game. Training version.
                """
        super().__init__(render_mode=render_mode)
        self.player0 = player0
        self.player1 = player1

    def choose_starting_player(self) -> None:
        """
                Select the starting player. Player1 always will be the starting one.
                Chosen by flipping coin.
                :return:
                """
        if random.uniform(0, 100) > 51:
            temp = self.player0
            self.player0 = self.player1
            self.player1 = temp

    def play_game(self):
        for agent in self.env.agent_iter():
            observation, _, terminated, truncated, _ = self.env.last()

            state_key = self.get_hash()

            if terminated or truncated:
                action = None
                self.env.step(action)
            else:
                if agent == 'player_0':
                    current_player = self.player0
                else:
                    current_player = self.player1

                current_player.check_state_key(state_key)
                action = current_player.choose_action(self.env.action_space(agent),
                                                      observation['action_mask'],
                                                      state_key)

                self.env.step(action)

                next_state, reward, termination, truncation, info = self.env.last()
                next_key = self.get_hash()
                current_player.check_state_key(next_key)
                current_player.update_q_values(state_key, action, reward, next_key,
                                               self.env.action_space(agent), next_state['action_mask'])
