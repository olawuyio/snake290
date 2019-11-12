import random
from typing import List, Optional


class Board:
    """
    Represents board containing snake and food

    Attributes:
    ===========
    width: int
        width of board
    height: int
        height of board
    board: List[List[int]]
        2d array of integers representing the elements on the board
        Integer codes:
            0 represents an empty position
            1 represents a snake part
            2 represents a food item


    Methods:
    ========
    is_valid_position(int, int) -> bool
        check if coordinates provided are valid
    is_position_empty(int, int) -> bool
        check if position is empty
    get_random_empty_cell -> Optional[(int, int)]
        get random position that is empty
    get_all_empty_positions -> List[(int, int)]
        get all empty positions
    """

    width: int
    height: int
    board: List[List[int]]

    def __init__(self, width: int, height: int):
        """Initialize board with specified width and height dimensions"""
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if position is valid

        :param x: x coordinate of position
        :param y: y coordinate of position
        :return: whether or not the position is valid
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def is_position_empty(self, x: int, y: int) -> bool:
        """Check if position is empty (no snake or food)

        :param x: x coordinate of position
        :param y: y coordinate of position
        :return: whether or not the position is empty,
        if position is invalid return False
        """
        if not self.is_valid_position(x, y):
            return False
        return self.board[y][x] == 0

    def get_random_empty_position(self) -> Optional[tuple]:
        """Get a random empty position

        :return: a tuple position (x, y) that is empty,
        if there is no valid position return None
        """
        positions = self.get_all_empty_positions()
        if not positions:
            return None
        return positions[random.randrange(len(positions))]

    def get_all_empty_positions(self) -> List[tuple]:
        """Get all empty positions

        :return: a list containing tuples (x, y) of all empty positions
        """
        positions = []
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    positions.append((x, y))
        return positions
