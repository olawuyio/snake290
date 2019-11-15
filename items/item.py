import pygame


class Item:
    """
    Represents how all the items in the game should look. This class includes
    attributes and methods all items must have.

    Attributes:
    ===========
    x: int
        the x coordinate
    y: int
        the y coordinate
    color: tuple
        the color of the item in rgb

    Methods:
    ========
    render(Surface) -> None
        draw the item onto the surface
    update(x, y) -> None
        change the position of the item
    in_bounds(item) -> bool
        checks if the passed in item touches the current item
    position() -> tuple
        returns the current (x,y) coordinate of the item

    Representation Invariants
    =========================
    0 <= x <= board width
    0 <= y <= board height

    width is a multiple of the game array length and the board size
    height is a multiple of the game array width and the board size

    colour's elements are in the range 0 - 255 as a tuple(int, int, int)

    """
    WIDTH = 10
    HEIGHT = 10
    x: int
    y: int
    color: tuple

    def __init__(self, position: tuple, color: tuple):
        self.x, self.y = position
        self.color = color

    def render(self, scene: pygame.Surface) -> None:
        """
        Defines how the function should be drawn on the screen
        :param scene: Main scene the game is showing
        """
        dimensions = (self.x, self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(scene, self.color, dimensions)

    def update(self, position: tuple) -> None:
        """
        Updates the x y coordinate of the game
        :param position: a tuple in the form (x: int, y: int)
        """
        self.x, self.y = position

    def in_bound(self, item2) -> bool:
        """
        checks to see if two objects are touching
        :param item2: an item object
        :return: True if touching, False if not
        """
        return pygame.Rect.colliderect(item2)

    def __str__(self) -> None:
        self.render()
