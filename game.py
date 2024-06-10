from abc import abstractmethod
from typing import Optional


class Game:
    def __init__(self, render_mode: str, environment):
        """
        Configurations.
        :param render_mode: 'rgb_array' for training or multiple game testing. 'human' for rendering game
        """
        self.render_mode = render_mode
        self.env = environment

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
        return hash(tuple(self.env.unwrapped.board)) if isinstance(self.env.unwrapped.board, list)\
            else hash(tuple(self.env.unwrapped.board.squares))

    def reset(self) -> None:
        """
        Resets the environment.
        """
        self.env.reset()
