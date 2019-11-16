from arena.board import Board
from arena.food import Food
from items.body import Body
from items.player import Player


class Snake:
    head: Player
    body: Body

    def __init__(self, board: Board, food: Food):
        x, y = board.dimensions
        self.head = Player(x // 2, y // 2,
                           board, food)
        self.body = None

    def update(self):
        self.head.update()

        if not self.head.food.on_board:
            self.grow()

        if self.body:
            curr = self.body

            while curr.has_next():
                curr.update()
                curr = curr.node

    def grow(self) -> None:
        """
        Grows the snake by 1, add 1 to the score.
        """
        if self.body == None:
            self.body = Body(self.head.x, self.head.y, self.head)
        elif self.body.node == None:
            self.body.set_to_next(
                Body(self.body.x - self.body.x_dir, self.body.y - self.body.y,
                     self.body))

        else:
            curr = self.body

            # Get last node on the snake
            # This loop stops 1 before the last item
            while curr.node.has_next():
                curr = curr.node
            curr = curr.node

            # Add body to last piece
            curr.set_to_next(Body(curr.x - curr.x_dir, curr.y - curr.y, curr))

        self.head.grow()
