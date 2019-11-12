from arena.board import Board


class Food:
    """
    Represents food on the board

    Attributes:
    ===========
    dimensions: tuple
        x, y coordinates of food
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

    position: tuple
    board: Board
    on_board: bool

    def __init__(self, board: Board):
        """Initialize food on board"""
        self.position = board.get_random_empty_position()
        self.board = board
        self.board.board[self.get_x()][self.get_y()] = 2
        self.on_board = True

    def get_x(self):
        """Get x coordinate of food

        :return: x coordinate of food
        """
        return self.position[0]

    def get_y(self):
        """Get y coordinate of food

        :return: y coordinate of food
        """
        return self.position[1]

    def eat(self) -> None:
        """Eat food on board"""
        self.board.board[self.get_x()][self.get_y()] = 0
        self.on_board = False

    def spawn_food(self, board: Board) -> None:
        """Spawn food item on board

        :param board: board to spawn food
        """
        self.__init__(board)
