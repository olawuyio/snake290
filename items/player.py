from typing import List

import pygame

from arena.board import Board
from arena.food import Food
from src.state import State


class Player:
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
    food: Food
    state: State
    ate_food: bool
    x_dir: int
    y_dir: int

    def __init__(self, x: int, y: int, board: Board, food: Food, state: State) -> None:
        """Initialize a Snake at the position <x> and <y> on the stage.
        """
        self.size = 4
        self.keys_pressed = None
        self.board = board
        self.food = food
        self.state = state
        self.ate = False
        self.positions = []
        for i in range(y, y + 4):
            self.positions.append((x, i))

    def update(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                if self.board.board[i][j] == 1:
                    self.board.board[i][j] = 0
        for position in self.positions:
            self.board.board[position[0]][position[1]] = 1

    def get_head_position(self):
        return self.positions[0][0], self.positions[0][1]

    def move(self, direction: tuple) -> None:
        """
        Move the snake in the <game> based on key presses.
        """
        old_position = self.get_head_position()
        new_position = (direction[0] + old_position[0], direction[1] + old_position[1])
        self.positions.insert(0, new_position)
        # Check what object is at the new position
        if not self.board.is_valid_position(new_position):
            self.state.quit()
        else:
            if not self.ate:
                del self.positions[-1]
            self.ate = False
            if self.board.get_code(new_position) == 0:
                pass
            elif self.board.get_code(new_position) == 1:
                self.state.quit()
            elif self.board.get_code(new_position) == 2:
                self.ate = True
                self.food.eat()
                self.food.spawn_food(self.board)
        print(self.positions)

    def get_score(self) -> int:
        """
        :return: the current score the player has
        """
        return len(self.positions)
