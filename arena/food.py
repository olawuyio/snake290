from arena.board import Board
from items import item


class Food(item):
    """
    Represents food on the board

    Attributes:
    ===========
    x: int
        the x coordinate of food on board
    y: int
        the y coordinate of food on board
    board: Board
        the board the food is on
    on_board: bool
        shows whether or not food is on board


    Methods:
    ========
    eat() -> None
        eat food on board
    spawn_food(Board) -> None
        spawn food item on board
    """

    x: int
    y: int
    board: Board
    on_board: bool

    def __init__(self, board: Board):
        """Initialize food on board"""
        self.x, self.y = board.get_random_empty_position()
        self.board = board
        self.board.board[self.x][self.y] = 2
        self.on_board = True

    def eat(self) -> None:
        """Eat food on board"""
        self.board.board[self.x][self.y] = 0
        self.on_board = False

    def spawn_food(self, board: Board) -> None:
        """Spawn food item on board

        :param board: board to spawn food
        """
        self.__init__(board)
