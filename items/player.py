from typing import List

import pygame

from arena.board import Board
from items.food import Food
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
        board that the player is on
    food: Food
        food object player can interact with
    state: State
        current game state
    ate_food: Bool
        whether the food has been eaten or not
    x_dir: int
        x direction the player will move in
    y_dir: int
        y direction the player will move in

    Methods:
    ========
    move(SnakeGame) -> None
        update the position of the Snake
    grow(self) -> None
        grow the snake by 1, also increase 1 to the score
    get_head_position(self) ->
    get_score() -> Int
        return the current score of the game

    Representation Invariants
    =========================
    -1 <= x_dir <= 1
    -1 <= y_dir <= 1
    """

    positions: List[List[int]]
    keys_pressed: pygame
    board: Board
    food: Food
    state: State
    ate_food: bool
    x_dir: int
    y_dir: int

    def __init__(self, x: int, y: int, board: Board, food: Food,
                 state: State) -> None:
        """Initialize a Snake at the position <x> and <y> on the stage."""
        self.size = 4
        self.keys_pressed = None
        self.board = board
        self.food = food
        self.state = state
        self.ate = False
        self.positions = []
        self.x_dir = 0
        self.y_dir = 0

        # start the list of positions with the head of the player
        for i in range(y, y + 4):
            self.positions.append([x, y])

    def update(self) -> None:
        """Moves the player in the appropriate direction."""
        for position in self.positions:

            # self.board.board[position[0]][position[1]] = 0
            position[0] += self.x_dir
            position[1] += self.y_dir
            self.board.board[position[0]][position[1]] = 1

    def move(self, direction: tuple) -> None:
        """
        Change the players direction in the <game> based on key presses.
        """
        self.x_dir, self.y_dir = direction
        old_position = self.get_head_position()
        new_position = (self.x_dir + old_position[0],
                        self.y_dir + old_position[1])
        self.positions.append(new_position)

        # Check what object is at the new position
        if not self.board.is_valid_position(new_position):
            self.state.quit()
        else:
            if not self.ate:
                del self.positions[-1]
            self.ate = False

            # Player interacts with empty spot
            if self.board.get_code(new_position) == 0:
                pass

            # Player interacts with it's self
            elif self.board.get_code(new_position) == 1:
                self.state.quit()

            # Player interacts with food
            elif self.board.get_code(new_position) == 2:
                self.ate = True
                self.food.eat()
                self.food.spawn_food(self.board)

            # Player interacts with wall
            elif self.board.get_code(new_position) == 3:
                self.state.quit()

    def get_head_position(self) -> (int, int):
        return self.positions[0][0], self.positions[0][1]

    def get_score(self) -> int:
        return len(self.positions)
