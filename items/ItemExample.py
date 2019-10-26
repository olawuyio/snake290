"""
Example of how to use the abstract item class

"""
import pygame

from items.Item import Item


class RedItem(Item):
    """
    Subclass of the item class
    Uses the initializer of the super class
    Must define render function
    """

    def __init__(self, position: tuple, size: tuple):
        super(RedItem, self).__init__(position, (255, 0, 0), size)

    def render(self, scene: pygame.Surface) -> None:
        """
        Defines how the function should be drawn on the screen
        :param scene: Main scene the game is showing
        """
        dimensions = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(scene, self.color, dimensions)


class BlueItem(Item):
    """
    Subclass of the item class
    Uses the initializer of the super class
    Must define render function
    """

    def __init__(self, position: tuple, size: tuple):
        super(BlueItem, self).__init__(position, (0, 0, 255), size)

    def render(self, scene: pygame.Surface) -> None:
        """
        Defines how the function should be drawn on the screen
        :param scene: Main scene the game is showing
        """
        dimensions = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(scene, self.color, dimensions)


class GreenItem(Item):
    """
    Subclass of the item class
    Uses the initializer of the super class
    Must define render function
    """

    def __init__(self, position: tuple, size: tuple):
        super(GreenItem, self).__init__(position, (0, 255, 0), size)

    def render(self, scene: pygame.Surface) -> None:
        """
        Defines how the function should be drawn on the screen
        :param scene: Main scene the game is showing
        """
        dimensions = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(scene, self.color, dimensions)
