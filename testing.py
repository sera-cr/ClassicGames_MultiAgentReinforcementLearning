import json
from game_testing import GameTesting
from player_testing import PlayerTesting
from pettingzoo.classic import connect_four_v3
from pettingzoo.classic import tictactoe_v3


class Testing:
    def __init__(self, number_games: int, roulette_wheel_p0: bool, roulette_wheel_p1: bool, player0_model_filename: str,
                 player1_model_filename: str, s_game: int = 0, render_mode: str = 'rgb_array',
                 testing_filename: str = 'testing_log', coinflip: bool = True):
        # Testing options
        self.n_games = number_games
        self.render_mode = render_mode
        self.roulette_wheel_p0 = roulette_wheel_p0
        self.roulette_wheel_p1 = roulette_wheel_p1
        self.testing_filename = testing_filename
        self.selected_game = s_game
        self.p0_model_name = player0_model_filename
        self.p1_model_name = player1_model_filename
        self.coinflip = coinflip

        if self.selected_game == 0:
            environment = tictactoe_v3.env(render_mode=self.render_mode)
            self.n_actions = 9
        else:
            environment = connect_four_v3.env(render_mode=self.render_mode)
            self.n_actions = 7

        # Load tables
        table0, table1 = self.load_training(player0_model_filename, player1_model_filename)

        # Game
        self.player0 = PlayerTesting(n_actions=self.n_actions, roulette_wheel=self.roulette_wheel_p0, table=table0)
        self.player1 = PlayerTesting(n_actions=self.n_actions, roulette_wheel=self.roulette_wheel_p1, table=table1)
        self.game = GameTesting(render_mode=self.render_mode, environment=environment,
                                player0=self.player0, player1=self.player1)

    def testing(self):
        for i in range(0, self.n_games):
            self.game.reset()
            if self.coinflip:
                self.game.choose_starting_player()
            self.game.play_game()

        self.game.changing_back_orders()
        self.write_testing_log()
        print('Testing finished.')

    def load_training(self, player0_filename: str, player1_filename: str):
        game = 'tictactoe' if self.selected_game == 0 else 'connect4'
        with open(f'models/{game}/{player0_filename}') as player0:
            table0 = json.load(player0)

        with open(f'models/{game}/{player1_filename}') as player1:
            table1 = json.load(player1)

        return table0, table1

    def write_testing_log(self):
        game = 'TICTACTOE' if self.selected_game == 0 else 'CONNECT4'
        testing_log = open(f'logs/tests/{self.testing_filename}.txt', 'w')
        testing_log.write(f'{game} TRAINING WITH Q-LEARNING -- TESTING\n')
        testing_log.write('Version: 1.0 \n')
        testing_log.write(f'{game} environment: PettingZoo 1.24.2\n')
        testing_log.write(f'Number of games played: {self.n_games}\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.write('CONFIGURATION:\n')
        testing_log.write(f'Player 0 filename: {self.p0_model_name}\n')
        testing_log.write(f'Player 1 filename: {self.p1_model_name}\n')
        testing_log.write(f'Player 0 roulette_wheel: {self.roulette_wheel_p0}\n')
        testing_log.write(f'Player 1 roulette_wheel: {self.roulette_wheel_p1}\n')
        testing_log.write(f'Coinflip enabled: {self.coinflip}\n')
        testing_log.write(f'Render mode: {self.render_mode}\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.write('RESULTS:\n')
        testing_log.write('\n')
        testing_log.write(f'Number of games won by player0: {self.game.p0_wins}\n')
        testing_log.write(f'Number of games won by player1: {self.game.p1_wins}\n')
        if self.coinflip:
            testing_log.write(f'Number of coins flipped: {self.game.coins_flipped}\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.write('END FILE\n')
        testing_log.write('=' * 70 + '\n')
        testing_log.close()


if __name__ == '__main__':
    n_games = 1000
    roulette_wheel_p0_testing = True
    roulette_wheel_p1_testing = True
    render_mode_testing = 'human'

    # Selected game
    # 0 -> TicTacToe
    # 1 -> Connect4
    selected_game = 1

    # Enable coinflip?
    enabled_coinflip = True

    filename0 = 'ql_nr_ad3_gd6_ed3_200001_p1.json'
    filename1 = 'sa_nr_ad3_gd6_ed3_200001_p0.json'

    # Filename convention:
    # ql -> QLearning
    # sa -> SARSA
    # nr -> No roulette wheel
    # r -> Roulette wheel
    # a -> learning rate or alpha
    # g -> discount factor or gamma
    # e -> random exploration or epsilon
    # d -> "dot" i.e: d5 = 0.5
    # x -> the tested value. If we have ex_3vs1 it means we are testing two models with epsilon 0.3 vs epsilon 0.1

    test_file = f'a3g6e3_qlvsa_200001_{"ttt" if selected_game == 0 else "c4"}'

    testing = Testing(number_games=n_games, roulette_wheel_p0=roulette_wheel_p0_testing,
                      roulette_wheel_p1=roulette_wheel_p1_testing, render_mode=render_mode_testing,
                      player0_model_filename=filename0, player1_model_filename=filename1,
                      testing_filename=test_file, s_game=selected_game, coinflip=enabled_coinflip)
    testing.testing()
