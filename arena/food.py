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
    size: tuple
        the display size of the food on board
    color: tuple
        the display color of the food on board
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
    size: tuple
    color: tuple
    on_board: bool

    def __init__(self, x: int, y: int, color: tuple, size: int, board: Board):
        """Initialize food on board"""
        self.x, self.y = board.get_random_empty_position()
        self.size = (4, 4)
        self.color = (255, 0, 0)
        item.__init__(x, y, color, size)
        # set the location of food on the board as non-empty
        board.board[self.x][self.y] = 1
        self.on_board = True

    def eat(self) -> None:
        """Eat food on board"""
        self.on_board = False

    def spawn_food(self, board: Board) -> None:
        """Spawn food item on board

        :param board: board to spawn food
        """
        self.__init__(board)
