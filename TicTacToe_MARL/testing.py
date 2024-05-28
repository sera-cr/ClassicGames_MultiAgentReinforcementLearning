import json
from game_testing import GameTesting
from player_testing import PlayerTesting


class Testing:
    def __init__(self, number_games: int, roulette_wheel_p1: bool, roulette_wheel_p2: bool, player1_model_filename: str,
                 player2_model_filename: str, render_mode: str = 'rgb_array', testing_filename: str = 'testing_log'):
        # Testing options
        self.n_games = number_games
        self.render_mode = render_mode
        self.roulette_wheel_p1 = roulette_wheel_p1
        self.roulette_wheel_p2 = roulette_wheel_p2
        self.testing_filename = testing_filename

        # Load tables
        table1, table2 = self.load_training(player1_model_filename, player2_model_filename)

        # Game
        self.player1 = PlayerTesting(roulette_wheel=self.roulette_wheel_p1, table=table1)
        self.player2 = PlayerTesting(roulette_wheel=self.roulette_wheel_p2, table=table2)
        self.game = GameTesting(render_mode=self.render_mode, player1=self.player1, player2=self.player2)

    def testing(self):
        for i in range(0, self.n_games):
            self.game.reset()
            self.game.choose_starting_player()
            self.game.play_game()

        self.write_testing_log()
        print('Testing finished.')

    @staticmethod
    def load_training(player1_filename: str, player2_filename: str):
        with open(player1_filename) as player1:
            table1 = json.load(player1)

        with open(player2_filename) as player2:
            table2 = json.load(player2)

        return table1, table2

    def write_testing_log(self):
        testing_log = open(f'{self.testing_filename}.txt', 'w')
        testing_log.write('TICTACTOE TRAINING WITH Q-LEARNING -- TESTING\n')
        testing_log.write('Version: 1.0 \n')
        testing_log.write('Chess environment: PettingZoo 1.24.2\n')
        testing_log.write(f'Number of games played: {self.n_games}\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.write('RESULTS:\n')
        testing_log.write('\n')
        testing_log.write(f'Number of games won by player1: {self.game.p1_wins}\n')
        testing_log.write(f'Number of games won by player2: {self.game.p2_wins}\n')
        testing_log.write(f'Number of coins flipped: {self.game.coins_flipped}\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.write('END FILE\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.close()


if __name__ == '__main__':
    n_games = 3
    roulette_wheel_p1_testing = True
    roulette_wheel_p2_testing = False
    render_mode_testing = 'human'

    filename1 = 'model_no_roulette_qlearning_player1.json'
    filename2 = 'model_no_roulette_qlearning_player2.json'

    testing = Testing(number_games=n_games, roulette_wheel_p1=roulette_wheel_p1_testing,
                      roulette_wheel_p2=roulette_wheel_p2_testing, render_mode=render_mode_testing,
                      player1_model_filename=filename1, player2_model_filename=filename2)
    testing.testing()
