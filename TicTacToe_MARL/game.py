from abc import abstractmethod
from pettingzoo.classic import tictactoe_v3
from typing import Optional


class Game:
    def __init__(self, render_mode: str):
        """
        Configurations.
        :param render_mode: 'rgb_array' for training or multiple game testing. 'human' for rendering game
        """
        self.render_mode = render_mode
        self.env = tictactoe_v3.env(render_mode=self.render_mode)

    @abstractmethod
    def play_game(self) -> Optional[tuple[int, int]]:
        """
        Must be implemented. Loop of the game. It should work either for training or testing.
        """
        pass

    def get_hash(self) -> int:
        """
        Returns the hash of the current state of the game.
        """
        return hash(self.env.unwrapped.board)

    def reset(self) -> None:
        """
        Resets the environment.
        """
        self.env.reset()
