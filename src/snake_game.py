"""
SnakeGame is a representation of the classic game snake
"""

from random import randint
from typing import List

import pygame

from arena.board import Board
from src.render_handler import RenderHandler
from src.state import State


class SnakeGame:
    """
    Handles running the game and defining the pygame stage

    Attributes
    ==========
    state: State
        represents what state the game currently is in
    scene: Screen
        where the data will be rendered to
    b_color: Tuple (int, int, int)
        rgb representation of the background colour
    handler: RenderHandler
        object that renders all the items onto the screen
    """

    state: State
    scene: pygame.Surface
    b_color: tuple
    handler: RenderHandler
    board: Board

    # DIMENSIONS FOR THE GAME BOARD
    BOARD_HEIGHT = 480
    BOARD_WIDTH = 640

    # Frame rate
    FPS = 50

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")

        self.b_color = 0, 0, 0
        self.state = State()
        self.scene = pygame.display.set_mode((self.BOARD_WIDTH,
                                              self.BOARD_HEIGHT))
        self.handler = RenderHandler([], self.scene)
        self.board = Board(self.BOARD_HEIGHT // 10, self.BOARD_WIDTH // 10)

    def on_quit(self):
        """Close pygame window"""
        pygame.quit()

    def on_event(self, event):
        """Handle a event.

        :param event: the event to handle
        """
        if event.type == pygame.QUIT:
            self.running = False

    def handle_events(self):
        """Handle all current events"""
        for event in pygame.event.get():
            self.on_event(event)

    def update(self) -> List[List[int]]:
        """
        Handles all game ticks
        :return:
        """
        # Todo add all game ticks and remove random generator
        board = self.board.board
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = randint(0, 3)

        return board

    # Todo get this to use states and render handler also remove test map
    def on_run(self) -> None:
        """
        Starts the game and keeps running it, updating game logic and rendering
        items

        """
        self.state.set_to_running()

        clock = pygame.time.Clock()
        self.scene.fill(self.b_color)

        while self.running:
            # Ensure game runs at same speed across all devices
            clock.tick(self.FPS)

            # Handle all current events
            self.handle_events()

            # Todo add the menu and pause functions
            # Display the game while the state is running
            if self.state == "running":

                self.scene.fill(self.b_color)

                # Update and render game
                board = self.update()
                # print(board)
                self.handler.update(board)
                self.handler.render()

                pygame.display.flip()

            elif self.state == "menu":
                pass
            elif self.state == "pause":
                pass

        self.on_quit()


if __name__ == "__main__":
    game = SnakeGame()
    game.on_run()
