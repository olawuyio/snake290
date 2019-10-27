import pygame


class Item:
    """
    Abstract class should not be implemented on this own
    Base for how components in the game should be defined

    Attributes:
    ===========
    x: int
        the x coordinate
    y: int
        the y coordinate
    width: int
        the width of the item
    height: int
        the height of the item
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

    x: int
    y: int
    width: int
    height: int
    color: tuple

    def __init__(self, position: tuple, color: tuple, size: tuple):
        self.x, self.y = position
        self.color = color
        self.width, self.height = size

    def render(self, scene: pygame.Surface) -> None:
        """
        Defines how the function should be drawn on the screen
        :param scene: Main scene the game is showing
        """
        raise NotImplementedError

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
    
    def return_item(self, x: int, y: int) -> Item:
        """
        Return the item that exists in the location given by
        <x> and <y>. If there isn't an item in that location, return None.
        """
        for item in Board.items:
            if item.x == x and item.y == y:
                return object
        return None
