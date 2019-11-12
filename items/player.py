from typing import List

import pygame
from arena.board import Board
from arena.food import Food
from items.item import Item
from arena.wall import Wall


class Player():
    """
    A class to represent the snake on the board. This includes all
    attributes or methods that the snake must have.

    Attributes:
    ===========
    positions: List[tuple]
        list of tuple positions that the snake is on
    keys_pressed: pygame
        the keys the player presses
    board: Board
        board that the snake is on

    Methods:
    ========
    move(SnakeGame) -> None
        update the position of the Snake
    grow(self) -> None
        grow the snake by 1, also increase 1 to the score
    get_score() -> Int
        return the current score of the game
    """

    positions: List[tuple]
    keys_pressed: pygame
    board: Board

    def __init__(self, x: int, y: int, board: Board, food: Food) -> None:
        """Initialize a Snake at the position <x> and <y> on the stage.
        """
        self.size = 4
        self.keys_pressed = None
        self.board = board
        self.food = food
        for i in range(y, y + 4):
            self.positions.append = (x, y)

    def get_size(self):
        return len(self.positions)

    def update(self):
        for position in self.positions:
            self.board.board[position[0]][position[1]] = 1

    def get_head_position(self):
        return self.positions[0][0], self.positions[0][1]

    def move(self, key_state: pygame.key) -> None:
        """
        Move the snake in the <game> based on key presses.
        """
        direction = (0, 0)
        self.keys_pressed = pygame.key.get_pressed()
        if self.keys_pressed[pygame.K_LEFT] or self.keys_pressed[pygame.K_a]:
            direction = (-1, 0)
        elif self.keys_pressed[pygame.K_RIGHT] or self.keys_pressed[pygame.K_d]:
            direction = (0, 1)
        elif self.keys_pressed[pygame.K_UP] or self.keys_pressed[pygame.K_w]:
            direction = (0, -1)
        elif self.keys_pressed[pygame.K_DOWN] or self.keys_pressed[pygame.K_s]:
            direction = (0, 1)

        old_position = self.get_head_position()
        new_position = (direction[0] + old_position[0], direction[1] + old_position[1])

        # Check what object is at the new position
        obj = Item.return_item(new_x, new_y)
        if Board.is_position_empty():
            self.x, self.y = new_x, new_y
        elif isinstance(obj, Food):
            self.food.eat()
            self.x, self.y = new_x, new_y
            self.grow()
        elif isinstance(obj, Player):
            self.x, self.y = new_x, new_y
            game.game_over()
        elif isinstance(obj, Wall):
            self.x, self.y = new_x, new_y
            game.game_over()

    def grow(self) -> None:
        """
        Grows the snake by 1, add 1 to the score.
        """
        self.score += 1

    def get_score(self) -> int:
        """
        :return: the current score the player has
        """
        return self.score
