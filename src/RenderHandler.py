import pygame

from items.ItemExample import BlueItem, GreenItem, RedItem


class RenderHandler:
    """
    Takes a 2d array and is able to convert that into objects for pygame

    Attributes
    ==========
    objects: List[[]]
        A list designed to mirror the game bord with objects that represent the
        values rather than numbers. This list may contain none, which represents
        that that spot is empty
    screen: pygame.Surface
        The screen the objects will be rendered onto

    Methods
    =======
    update(List[[]] -> none
        takes in a list representing the game in terms of ints, and converts
        that into a mirrored list but with objects

    Representation Invariants
    =========================
    game == 2d array containing only 0, 1, 2, 3
    len(objects) == len(game)
    screen will be a valid pygame surface
    """
    objects: list
    screen: pygame.Surface

    def __init__(self, game: list, screen: pygame.Surface):

        # Todo: make the dimensions relative to a global variable

        # Initialize an empty game board
        for i in range(len(game)):
            for j in range(len(game[i])):
                self.objects[i][j] = None

        self.update(game)
        self.screen = screen

    def update(self, game: list) -> None:
        """
        Loop through the game list and mirror it to a list of objects such that
        the objects represent visually what is going on in the game

        Both lists are iterated on in parallel, if the object list contains an
        item where the new game list is empty remove that item. If they are
        different change it to the new one
        """

        # Todo: Add constants to ensure the scale of the items is always correct

        temp_list = []
        for row in range(len(game)):
            temp_col = []

            # Create a object based on the item in the list
            for col in range(len(game[row])):
                current = game[col][row]

                # Check which item is in the spot
                if current == 0:
                    temp_col.append(None)

                elif current == 1:  # add red item
                    item = RedItem((row * 100, col * 100), (100, 100))
                    temp_col.append(item)

                elif current == 2:  # add blue item
                    item = BlueItem((row * 100, col * 100), (100, 100))
                    temp_col.append(item)

                elif current == 3:  # add green item
                    item = GreenItem((row * 100, col * 100), (100, 100))
                    temp_col.append(item)

                else:
                    temp_col.append(None)

            temp_list.append(temp_col)

        self.objects = temp_list

    # Todo: Remove this method
    def draw(self) -> None:
        red_item = RedItem((300, 200), (20, 20))
        green_item = RedItem((100, 200), (20, 20))
        blue_item = RedItem((100, 100), (20, 20))
        red_item.render(self.screen)
        green_item.render(self.screen)
        blue_item.render(self.screen)

    def render(self) -> None:
        """
        Goes through each object in the game and renders it
        """
        for row in self.objects:
            for item in row:
                if item:  # Ensure the spot is not empty
                    item.render(self.screen)
