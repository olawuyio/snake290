import pygame

from arena.board import Board
from arena.food import Food
from src.state import State


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

    x: int
    y: int
    x_dir: int
    y_dir: int
    keys_pressed: pygame
    board: Board

    def __init__(self, x: int, y: int, board: Board, food: Food) -> None:
        """Initialize a Snake at the position <x> and <y> on the stage.
        """
        self.size = 4
        self.keys_pressed = None
        self.board = board
        self.food = food
        self.x, self.y = x, y

        self.x_dir, self.y_dir = 0, 0

        # self.positions = []
        #
        # for i in range(y, y + 4):
        #     self.positions.append((x, y))

    def get_size(self):
        return len(self.positions)

    def update(self):
        # for position in self.positions:

        self.board.board[self.x][self.y] = 0
        self.x += self.x_dir
        self.y += self.y_dir

        self.board.board[self.x][self.y] = 1

    def get_head_position(self):
        return self.positions[0][0], self.positions[0][1]

    def move(self, direction: tuple, game: State) -> None:
        """
        Move the snake in the <game> based on key presses.
        """
        # direction = (0, 0)

        # self.keys_pressed = pygame.key.get_pressed()
        # if self.keys_pressed[pygame.K_LEFT] or self.keys_pressed[pygame.K_a]:
        #     direction = (-1, 0)
        # elif self.keys_pressed[pygame.K_RIGHT] or self.keys_pressed[pygame.K_d]:
        #     direction = (0, 1)
        # elif self.keys_pressed[pygame.K_UP] or self.keys_pressed[pygame.K_w]:
        #     direction = (0, -1)
        # elif self.keys_pressed[pygame.K_DOWN] or self.keys_pressed[pygame.K_s]:
        #     direction = (0, 1)

        # old_position = self.get_head_position()
        # print(direction)
        # new_x = direction[0] + old_position[0]
        # new_y = direction[1] + old_position[1]
        # print(new_x)
        # print(new_y)
        # Check what object is at the new position
        # obj = self.return_item(new_x, new_y)

        # if Board.is_position_empty(self.board, (new_x, new_y)):
        #     self.x, self.y = new_x, new_y
        #
        # elif self.board.board[self.x][self.y] == 2:
        #     self.food.eat()
        #     self.x, self.y = new_x, new_y
        #     self.grow()
        #
        # elif self.board.board[self.x][self.y] == 1:
        #     self.x, self.y = new_x, new_y
        #     # game.set_to_end()
        #
        # elif self.board.board[self.x][self.y] == 3:
        #     self.x, self.y = new_x, new_y
        #     # game.set_to_end()

        self.x_dir, self.y_dir = direction

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

    def return_item(self, x: int, y: int) -> object:
        """
        Return the item that exists in the location given by
        <x> and <y>. If there isn't an item in that location, return None.
        """
        for item in self.board.items:
            if item.x == x and item.y == y:
                return item
        return None
