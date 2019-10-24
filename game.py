import pygame

import configparser

# read configuration file
config = configparser.ConfigParser()
config.read('config.ini')


class Game:
    """This is the main class for game"""

    def __init__(self):
        """Initialize attributes and setup game window"""
        pygame.display.set_caption(config["Window"]["Name"])
        dimensions = (int(config["Window"]["Width"]), (int(config["Window"]["Height"])))
        self.screen = pygame.display.set_mode(dimensions)
        self.running = True

    def on_event(self, event):
        """Handle a event.

        Args:
            event: the event to handle
        """
        if event.type == pygame.QUIT:
            self.running = False

    def handle_events(self):
        """Handle all current events"""
        for event in pygame.event.get():
            self.on_event(event)

    def on_quit(self):
        """Close pygame window"""
        pygame.quit()

    def on_play(self):
        """Play game"""
        while self.running:
            self.handle_events()
        self.on_quit()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.on_play()
