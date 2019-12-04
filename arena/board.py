import random
from typing import List, Optional


class Board:
    """
    Represents board containing snake and food.

    Attributes:
    ===========
    dimensions: tuple
        width and height of board
    board: List[List[int]]
        2d array of integers representing the elements on the board

    Methods:
    ========
    get_width() -> int
        get width of board
    get_height() -> int
        get height of board
    is_valid_position(int, int) -> bool
        check if coordinates provided are valid
    is_position_empty(int, int) -> bool
        check if position is empty
    get_random_empty_cell -> Optional[(int, int)]
        get random position that is empty
    get_all_empty_positions -> List[(int, int)]
        get all empty positions

    Representation Invariants
    =========================
    dimensions = (int x, int y)

    0 <= x <= 64
    0 <= y <= 48

    Spots on the board
    0 represents an empty position
    1 represents a snake part
    2 represents a food item
    """

    dimensions: tuple
    board: List[List[int]]

    def __init__(self, dimensions: tuple):
        """
        Initialize board with specified width and height dimensions.
        """
        self.dimensions = dimensions
        self.board = self._initialize_board()

    def get_width(self) -> int:
        """Get board width.

        :return: board width.
        """
        return self.dimensions[0]

    def get_height(self) -> int:
        """Get board height.

        :return: board height.
        """
        return self.dimensions[1]

    def get_code(self, position: tuple) -> int:
        return self.board[position[0]][position[1]]

    def is_valid_position(self, position: tuple) -> bool:
        """Check if position is valid.

        :param position: x, y coordinates of position.
        :return: whether or not the position is valid.
        """
        return 0 <= position[0] < self.get_width() \
               and 0 <= position[1] < self.get_height()

    def is_position_empty(self, position: tuple) -> bool:
        """Check if position is empty (no snake or food).

        :param position: x, y coordinates of position.
        :return: whether or not the position is empty,
        if position is invalid return False.
        """
        if not self.is_valid_position(position):
            return False
        return self.board[position[0]][position[1]] == 0

    def get_random_empty_position(self) -> Optional[tuple]:
        """Get a random empty position.

        :return: a tuple position (x, y) that is empty,
        if there is no valid position return None.
        """
        positions = self.get_all_empty_positions()
        if not positions:
            return None
        return positions[random.randrange(len(positions))]

    def get_all_empty_positions(self) -> List[tuple]:
        """Get all empty positions

        :return: a list containing tuples (x, y) of all empty positions.
        """
        positions = []
        for y in range(self.get_height() - 1):
            for x in range(self.get_width() - 1):
                if self.board[y][x] == 0:
                    positions.append((y, x))
        return positions

    def _initialize_board(self) -> List[List[int]]:
        """
        Creates a basic 2D array of integers with 3's on the boarder.
        :return: game board as 2D array of integers.
        """
        board = [[0 for _ in range(self.get_width())] for _ in
                 range(self.get_height())]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == 63 or j == 0 or j == 47:
                    board[i][j] = 3
        return board
