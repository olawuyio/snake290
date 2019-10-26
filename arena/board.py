class Board:
    """
    Represents board containing snake and food

    Attributes:
    ===========
    width: int
        width of board
    height: int
        height of board
    board: List[[]]
        2d array representing the elements on the board


    Methods:
    ========
    is_valid_position(int, int) -> bool
        check if coordinates provided are valid
    is_position_empty(int, int) -> bool
        check if position is empty
    get_random_empty_cell -> (int, int)
        get random cell location that is empty
    """

    width: int
    height: int
    board: list

    def __init__(self, width, height):
        """Initialize board"""
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def is_valid_position(self, x, y) -> bool:
        """Check if position is valid

        :param x: x coordinate of position
        :param y: y coordinate of position
        :return: whether or not the position is valid
        """
        raise NotImplementedError

    def is_position_empty(self, x, y) -> bool:
        """Check if position is empty (no snake or food)

        :param x: x coordinate of position
        :param y: y coordinate of position
        :return: whether or not the position is empty
        """
        raise NotImplementedError

    def get_random_empty_position(self) -> (int, int):
        """Get a random empty position

        :return: a position that is empty
        """
        raise NotImplementedError
