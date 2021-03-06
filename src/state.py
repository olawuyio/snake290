class State:
    """Defines a string which represents what the game should be doing.

    Public attributes:
    ==================
    state: string
        what state the game currently is in

    *** Note***
    Only call the state but do not set it directly

    Representation Invariants
    =========================
    sate will be one of the following strings
    running (default): the game is currently running
    pause: the game is paused
    menu: the game is on the main menu
    """
    running: bool
    state: str

    def __init__(self):
        """Initialize state."""
        self.running = True
        self.state = "running"

    def set_to_menu(self) -> None:
        """Changes state to "menu"."""
        self.state = "menu"

    def set_to_pause(self) -> None:
        """Changes state to "pause"."""
        self.state = "pause"

    def set_to_running(self) -> None:
        """Changes state to "running"."""
        self.state = "running"

    def quit(self):
        """Changes state to "quit"."""
        self.running = False

    def __eq__(self, other):
        return self.state == other
