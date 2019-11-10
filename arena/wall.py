class Wall:
    """
    A class to represent the wall on the board.

    Attributes:
    ===========
    size: int
        the thickness of the wall, initialized to 2
    color: tuple
        the color of the wall.


    Methods:
    ========

    """
    size: int
    color: tuple

    def __init__(self) -> None:
        """Initialize a wall
        """
        self.color = (255, 170, 29)
        self.size = 2
