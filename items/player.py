"""
The player class

"""
import pygame

from items.item import Item


class Player(Item):
    """
    Subclass of the item class
    """

    def __init__(self, position: tuple, size: tuple):
        super(Player, self).__init__(position, (255, 0, 0), size)

    def grow(self) -> None:
        """
        Grow the snake by 1.
        """
        pass

    def render(self, scene: pygame.Surface) -> None:
        """
        :param scene: Main scene the game is showing
        """
        dimensions = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(scene, self.color, dimensions)
