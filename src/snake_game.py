from typing import List

import pygame

from arena.board import Board
from items.food import Food
from items.player import Player
from src.render_handler import RenderHandler
from src.state import State


class SnakeGame:
    """
    Handles running the game and defining the pygame stage.

    Attributes
    ==========
    state: State
        represents what state the game currently is in
    scene: Screen
        where the data will be rendered to
    background_color: Tuple (int, int, int)
        RGB representation of the background colour
    handler: RenderHandler
        object that renders all the items onto the screen
    player: Player
        snake object that the player uses
    food: Food
        food item that player can eat
    """

    state: State
    scene: pygame.Surface
    background_color: tuple
    handler: RenderHandler
    board: Board
    player: Player
    food: Food
    running = True

    DIMENSIONS = (640, 480)  # Width and height of the board
    FPS = 60  # Frame rate the game should run at
    SCALE = 10  # The scale between the pygame screen and game board

    def __init__(self):

        # Initialize pygame window
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.scene = pygame.display.set_mode(self.DIMENSIONS)

        # Initialize backend components
        self.background_color = 0, 0, 0
        self.board = Board((self.DIMENSIONS[1] // 10, self.DIMENSIONS[0] // 10))
        self.state = State()
        self.handler = RenderHandler([], self.scene)

        # Initialize game objects
        self.food = Food(self.board)
        self.player = Player(self.DIMENSIONS[0] // 20, self.DIMENSIONS[1] // 20,
                             self.board, self.food, self.state)

    def on_quit(self) -> None:
        """Close pygame window."""
        pygame.quit()

    def on_event(self, event: pygame.event) -> bool:
        """Handle a specific event.

        :param event: the event to handle
        :return: whether move is made
        """
        if event.type == pygame.QUIT:
            self.state.quit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.player.move((-1, 0))
            return True
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.player.move((1, 0))
            return True
        elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.player.move((0, -1))
            return True
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.player.move((0, 1))
            return True

        return False

    def handle_events(self) -> None:
        """Handle all current events."""
        move_made = False

        for event in pygame.event.get():
            if self.on_event(event):
                move_made = True

        if not move_made and (self.player.x_dir != 0 or self.player.y_dir != 0):
            self.player.move((self.player.x_dir, self.player.y_dir))

    def update(self) -> List[List[int]]:
        """
        Handles all game ticks.

        :return: game board as 2D array of integers
        """
        board = self.board.board
        self.player.update()

        return board

    def on_run(self) -> None:
        """
        Starts the game and keeps running it, updating game logic and rendering
        items.
        """
        self.state.set_to_running()

        clock = pygame.time.Clock()
        self.scene.fill(self.background_color)

        while self.state.running:
            # Ensure game runs at same speed across all devices
            clock.tick(self.FPS)

            # Handle all current events
            self.handle_events()

            # Display the game while the state is running
            if self.state == "running":

                self.scene.fill(self.background_color)

                # Update and render game
                board = self.update()
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
