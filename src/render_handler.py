from typing import List

import pygame

from items.item import Item


class RenderHandler:
    """
    Takes a 2d array and is able to convert that into objects for pygame.

    Attributes
    ==========
    objects: List[[]]
        A list designed to mirror the game board with objects that represent the
        values rather than numbers. This list may contain none, which represents
        that that spot is empty
    screen: pygame.Surface
        The screen the objects will be rendered onto

    Methods
    =======
    update(List[[]]) -> none
        takes in a list representing the game in terms of ints, and converts
        that into a mirrored list but with objects
    render(self) -> none
        goes through objects and individually renders each one

    Representation Invariants
    =========================
    game == 2d array containing only 0, 1, 2, 3
    len(objects) == len(game)
    screen will be a valid pygame surface
    """
    objects: List[List[int]]
    screen: pygame.Surface

    SCALE = 10  # Constant to scale the 2d array to pygame surface

    def __init__(self, game: List[List[int]], screen: pygame.Surface):
        # Initialize an empty game board
        for i in range(len(game)):
            for j in range(len(game[i])):
                self.objects[i][j] = None

        self.update(game)
        self.screen = screen

    def update(self, game: List[List[int]]) -> None:
        """
        Loop through the game list and mirror it to a list of objects such that
        the objects represent visually what is going on in the game.

        Both lists are iterated on in parallel, if the object list contains an
        item where the new game list is empty remove that item. If they are
        different change it to the new one.
        """

        wall_color = (0, 0, 255)
        player_color = (0, 255, 0)
        food_color = (255, 0, 0)

        temp_list = []

        for row in range(len(game)):
            temp_col = []

            # Create a object based on the item in the list
            for col in range(len(game[row])):
                current = game[row][col]

                # Check which item is in the spot
                if current == 0:
                    temp_col.append(None)

                # add player object
                elif current == 1:
                    item = Item((row * self.SCALE, col * self.SCALE),
                                player_color)
                    temp_col.append(item)

                # add food object
                elif current == 2:
                    item = Item((row * self.SCALE, col * self.SCALE),
                                food_color)
                    temp_col.append(item)

                # add wall object
                elif current == 3:  # add green item
                    item = Item((row * self.SCALE, col * self.SCALE),
                                wall_color)
                    temp_col.append(item)

                else:
                    temp_col.append(None)

            temp_list.append(temp_col)

        self.objects = temp_list

    def render(self) -> None:
        """
        Goes through each object in the game and renders it.
        """
        for row in self.objects:
            for item in row:
                if item:  # Ensure the spot is not empty
                    item.render(self.screen)
