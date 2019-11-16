from typing import Optional

from items.player import Player


class Body(Player):
    """
    Linked list that represents the body of the snake

    Attributes
    ==========
    previous: Player
        This is the first item on the body
    node: Player
        Next item on the body
    """
    previous: Player

    def __init__(self, x: int, y: int, previous: Player):
        Player.__init__(self, x, y, previous.board, previous.food)

        self.previous = previous
        self.node = None

        self.x_dir = previous.x_dir
        self.y_dir = previous.y_dir

    def set_to_next(self, node):
        self.node = node

    def has_next(self) -> bool:
        if not self.node:
            return False
        return True

    def update(self):
        self.x_dir = self.previous.x_dir
        self.y_dir = self.previous.y_dir

        self.board.board[self.x][self.y] = 0

        # Update the current item to take the position of the previous item
        self.x = self.previous.x - self.previous.x_dir
        self.y = self.previous.y - self.previous.y_dir

        self.board.board[self.x][self.y] = 1
