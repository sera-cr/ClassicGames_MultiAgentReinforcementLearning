import json
import time
from player_training import PlayerTraining
from game_training import GameTraining
from IPython.display import clear_output
from pettingzoo.classic import connect_four_v3
from pettingzoo.classic import tictactoe_v3


class Training:
    def __init__(self, alpha: float, gamma: float, epsilon: float, algorithm: int, roulette_wheel: bool,
                 coinflip_enabled: bool, max_episodes: int, render_mode: str = 'rgb_array', selected_game: int = 0,
                 training_filename: str = 'training_log'):
        # Hyperparameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # Training options
        self.max_episodes = max_episodes
        self.render_mode = render_mode
        self.training_algorithm = algorithm
        self.roulette_wheel = roulette_wheel
        self.coinflip = coinflip_enabled
        self.training_filename = training_filename

        # Training Environment
        if selected_game == 0:
            environment = tictactoe_v3.env(render_mode=self.render_mode)
            self.n_actions = 9
        else:
            environment = connect_four_v3.env(render_mode=self.render_mode)
            self.n_actions = 7
        self.selected_game = selected_game

        # Game
        self.player0 = PlayerTraining(alpha=self.alpha, gamma=self.gamma, epsilon=self.epsilon,
                                      algorithm=self.training_algorithm, n_actions=self.n_actions,
                                      roulette_wheel=self.roulette_wheel)
        self.player1 = PlayerTraining(alpha=self.alpha, gamma=self.gamma, epsilon=self.epsilon,
                                      algorithm=self.training_algorithm, n_actions=self.n_actions,
                                      roulette_wheel=self.roulette_wheel)
        self.game = GameTraining(render_mode=self.render_mode, environment=environment, player0=self.player0,
                                 player1=self.player1)

        # Training results
        self.epochs_counter = 0
        self.training_time = 0.0
        self.episode_times = []

    def training(self):
        training_start_time = time.time()
        for i in range(1, self.max_episodes):
            episode_start_time = time.time()
            self.game.reset()
            if self.coinflip:
                self.game.choose_starting_player()
            self.game.play_game()

            if i % 100 == 0:
                clear_output(wait=True)
                print(f'Episode: {i}')

            episode_end_time = time.time()
            self.episode_times.append(episode_end_time - episode_start_time)

        training_end_time = time.time()
        self.training_time = training_end_time - training_start_time
        self.save_training()
        self.write_training_log()
        print('Training finished.')

    def save_training(self):
        table0 = self.player0.get_qtable()
        table1 = self.player1.get_qtable()

        log_path = 'tictactoe' if self.selected_game == 0 else 'connect4'

        filename0 = f'./models/{log_path}/{self.training_filename}_{self.max_episodes}_p0.json'
        with open(filename0, 'w') as outfile:
            json.dump(table0, outfile)
        filename1 = f'./models/{log_path}/{self.training_filename}_{self.max_episodes}_p1.json'
        with open(filename1, 'w') as outfile:
            json.dump(table1, outfile)

    def write_training_log(self):
        env_text = 'TicTacToe' if self.selected_game == 0 else 'Connect4'
        log_path = 'tictactoe' if self.selected_game == 0 else 'connect4'
        training_log = open(f'./logs/{log_path}/{self.training_filename}_{self.max_episodes}.txt', 'w')
        training_log.write(f'{env_text} TRAINING\n')
        training_log.write('Version: 1.0 \n')
        training_log.write(f'{env_text} environment: PettingZoo 1.24.2\n')
        training_log.write('=' * 70 + '\n')
        training_log.write('HYPERPARAMETERS:\n')
        training_log.write('\n')
        training_log.write(f'Alpha: {self.alpha}\n')
        training_log.write(f'Gamma: {self.gamma}\n')
        training_log.write(f'Epsilon: {self.epsilon}\n')
        training_log.write('\n')
        training_log.write('CONFIGURATION:\n')
        training_log.write(f'Training algorithm: {"Q-Learning" if self.training_algorithm == 0 else "SARSA"}\n')
        training_log.write(f'Roulette_wheel: {self.roulette_wheel}\n')
        training_log.write(f'Max episodes: {self.max_episodes}\n')
        training_log.write(f'Render mode: {self.render_mode}\n')
        training_log.write('RESULTS:\n')
        training_log.write('\n')
        training_log.write(f'Episodes trained: {self.max_episodes - 1}\n')
        training_log.write(f'Epochs trained: {self.epochs_counter}\n')
        training_log.write(f'Training time: {self.training_time} seconds\n')
        training_log.write(f'Average episode time: {sum(self.episode_times) / len(self.episode_times)} seconds\n')
        training_log.write('\n')
        training_log.write('=' * 70 + '\n')
        training_log.write('EPISODES TIMES:\n')
        training_log.write('\n')
        for key, value in enumerate(self.episode_times):
            training_log.write(f'Episode {key}: {value} seconds.\n')
        training_log.write('=' * 70 + '\n')
        training_log.write('END FILE\n')
        training_log.write('=' * 70 + '\n')
        training_log.close()
        self.episodes_log()

    def episodes_log(self):
        log_path = 'tictactoe' if self.selected_game == 0 else 'connect4'
        episodes_log = open(f'./logs/{log_path}/{self.training_filename}_episodes_times_{self.max_episodes}.txt', 'w')
        for key, value in enumerate(self.episode_times):
            episodes_log.write(f'{value}\n')
        episodes_log.close()


if __name__ == '__main__':
    learning_rate = 0.3
    discount_factor = 0.6
    random_exploration = 0.7

    # Configuration
    # rgb_array -> no visualization
    # human -> 2D game
    render_mode_training = 'rgb_array'
    m_episodes = 30001
    roulette_wheel_algorithm = False
    coinflip = True

    # Training algorithm
    # 0 -> Q-Learning, Bellman equation
    # 1 -> SARSA
    training_algorithm = 1

    # Training game
    # 0 -> TicTacToe
    # 1 -> Connect4
    game = 1

    # Logs
    # filename translations:
    # ql -> QLearning
    # sa -> SARSA
    # nr -> No roulette wheel
    # r -> Roulette wheel
    # a -> learning rate or alpha
    # g -> discount factor or gamma
    # e -> random exploration or epsilon
    # d -> "dot" i.e: d5 = 0.5
    # Number of episodes is NEVER added to the filename
    filename = (f'{"ql" if training_algorithm == 0 else "sa"}_{"r" if roulette_wheel_algorithm else "nr"}'
                f'_ad{str(learning_rate).split(".")[1][:2]}_gd{str(discount_factor).split(".")[1][:2]}_ed'
                f'{str(random_exploration).split(".")[1][:2]}')

    # Creating training class
    training = Training(alpha=learning_rate, gamma=discount_factor, epsilon=random_exploration,
                        algorithm=training_algorithm, roulette_wheel=roulette_wheel_algorithm,
                        coinflip_enabled=coinflip, render_mode=render_mode_training, max_episodes=m_episodes,
                        selected_game=game, training_filename=filename)

    training.training()
