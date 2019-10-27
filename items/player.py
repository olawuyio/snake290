import pygame
from board import Board
from food import Food
from item import Item

class Player(Item):
    """
    A class to represent the snake on the board. This includes all
    attributes or methods that the snake must have.

    Attributes:
    ===========
    x: int
        x coordinate of this actor's location on the stage
    y: int
        y coordinate of this actor's location on the stage

    Methods:
    ========
    get_score() -> None
        update the score of the game
    move(SnakeGame) -> None
        update the position of the Snake
    grow(self) -> None
        grow the snake by 1
    """

    x: int
    y: int

    def __init__(self, x: int, y: int, color: tuple, size: tuple) -> None:
        """Initialize a Snake at the position <x> and <y> on the stage.
        """

        Item.__init__(x, y, color, size)
        self.color = (0, 128, 0)
        self.width, self.height = size
        self.keys_pressed = None
        self._score = 0
        
    def render(self, scene: pygame.Surface) -> None:
        """
        Main scene the game is showing
        """
        dimensions = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(scene, self.color, dimensions)

    def move(self, game: 'SnakeGame') -> None:
        """
        Move the snake in the <game> based on key presses.
        """
        dx, dy = 0, 0
        self.keys_pressed = pygame.key.get_pressed()
        if self.keys_pressed[pygame.K_LEFT] or self.keys_pressed[pygame.K_a]:
            dx -= 1
        elif self.keys_pressed[pygame.K_RIGHT] or self.keys_pressed[pygame.K_d]:
            dx += 1
        elif self.keys_pressed[pygame.K_UP] or self.keys_pressed[pygame.K_w]:
            dy -= 1
        elif self.keys_pressed[pygame.K_DOWN] or self.keys_pressed[pygame.K_s]:
            dy += 1

        new_x, new_y = self.x + dx, self.y + dy
        # Check what object is at the new position
        obj = Item.get_actor(new_x, new_y)
        if Board.is_position_empty():
            self.x, self.y = new_x, new_y
        elif isinstance(item, Food):
            obj.eat()
            self.x, self.y = new_x, new_y
            self._score += 1
        elif isinstance(item, Player):
            self.x, self.y = new_x, new_y
            game.game_over()
        elif isinstance(item, Wall):
            self.x, self.y = new_x, new_y
            game.game_over()

    def grow(self) -> None:
        """
        Grow the snake by 1
        """
        pass
