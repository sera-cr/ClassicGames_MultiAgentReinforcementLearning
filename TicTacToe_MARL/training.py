import json
import time
from game_training import GameTraining
from player_training import PlayerTraining
from IPython.display import clear_output


class Training:
    def __init__(self, alpha: float, gamma: float, epsilon: float, algorithm_player1: int, roulette_wheel_p1: bool,
                 algorithm_player2: int, roulette_wheel_p2: bool, max_episodes: int, render_mode: str = 'rgb_array',
                 training_filename: str = 'training_log'):
        # Hyperparameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        # Training options
        self.max_episodes = max_episodes
        self.render_mode = render_mode
        self.algorithm_player1 = algorithm_player1
        self.algorithm_player2 = algorithm_player2
        self.roulette_wheel_p1 = roulette_wheel_p1
        self.roulette_wheel_p2 = roulette_wheel_p2
        self.training_filename = training_filename

        # Game
        self.player1 = PlayerTraining(alpha=self.alpha, gamma=self.gamma, epsilon=self.epsilon,
                                      algorithm=algorithm_player1, roulette_wheel=self.roulette_wheel_p1)
        self.player2 = PlayerTraining(alpha=self.alpha, gamma=self.gamma, epsilon=self.epsilon,
                                      algorithm=algorithm_player2, roulette_wheel=self.roulette_wheel_p2)
        self.game = GameTraining(render_mode=self.render_mode, player1=self.player1, player2=self.player2)

        # Training results
        self.epochs_counter = 0
        self.training_time = 0.0
        self.episode_times = []

    def training(self):
        training_start_time = time.time()
        for i in range(1, self.max_episodes):
            episode_start_time = time.time()
            self.game.reset()
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
        table1 = self.player1.get_qtable()
        table2 = self.player2.get_qtable()

        filename1 = './models/model_{roulette}_{algorithm}_{max_episodes}_player1.json'.format(
            roulette='roulette' if self.roulette_wheel_p1 else 'no_roulette',
            algorithm='qlearning' if self.algorithm_player1 == 0 else 'sarsa',
            max_episodes=self.max_episodes
        )
        with open(filename1, 'w') as outfile:
            json.dump(table1, outfile)
        filename2 = './models/model_{roulette}_{algorithm}_{max_episodes}_player2.json'.format(
            roulette='roulette' if self.roulette_wheel_p2 else 'no_roulette',
            algorithm='qlearning' if self.algorithm_player2 == 0 else 'sarsa',
            max_episodes=self.max_episodes
        )
        with open(filename2, 'w') as outfile:
            json.dump(table2, outfile)

    def write_training_log(self):
        training_log = open(f'./logs/{self.training_filename}.txt', 'w')
        training_log.write('TICTACTOE TRAINING\n')
        training_log.write('Version: 1.0 \n')
        training_log.write('TicTacToe environment: PettingZoo 1.24.2\n')
        training_log.write('=' * 70 + '\n')
        training_log.write('HYPERPARAMETERS:\n')
        training_log.write('\n')
        training_log.write(f'Alpha: {self.alpha}\n')
        training_log.write(f'Gamma: {self.gamma}\n')
        training_log.write(f'Epsilon: {self.epsilon}\n')
        training_log.write('\n')
        training_log.write('CONFIGURATION:\n')
        training_log.write(f'Player 1 training algorithm: {"Q-Learning" if self.algorithm_player1 == 0 else "SARSA"}\n')
        training_log.write(f'Player 2 training algorithm: {"Q-Learning" if self.algorithm_player2 == 0 else "SARSA"}\n')
        training_log.write(f'Player 1 roulette_wheel: {self.roulette_wheel_p1}\n')
        training_log.write(f'Player 2 roulette_wheel: {self.roulette_wheel_p2}\n')
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
        episodes_log = open(f'./logs/{self.training_filename}_episodes_times.txt', 'w')
        for key, value in enumerate(self.episode_times):
            episodes_log.write(f'{value}\n')
        episodes_log.close()


if __name__ == '__main__':
    learning_rate = 0.3
    discount_factor = 0.6
    random_exploration = 0.3

    # Configuration
    render_mode_training = 'rgb_array'
    m_episodes = 30001
    roulette_wheel_p1_training = False
    roulette_wheel_p2_training = False

    # Training algorithm
    # 0 -> Q-Learning, Bellman equation
    # 1 -> SARSA
    a_player1 = 1
    a_player2 = 1

    filename = 'sarsa_nr_both'

    # Creating training class
    training = Training(alpha=learning_rate, gamma=discount_factor, epsilon=random_exploration,
                        algorithm_player1=a_player1, roulette_wheel_p1=roulette_wheel_p1_training,
                        algorithm_player2=a_player2, roulette_wheel_p2=roulette_wheel_p2_training,
                        render_mode=render_mode_training, max_episodes=m_episodes, training_filename=filename)

    training.training()