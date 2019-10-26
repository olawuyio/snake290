class State:
    """
    Defines a string which represents what the game should be doing

    Public attributes:
    ==================
    state: string
        what state the game currently is in

    *** Note***
    Only call the state but do not set it directly

    Representation Invariants
    =========================
    sate will be one of the following strings
    running: the game is currently running
    pause: the game is paused
    menu: the game is on the main menu


    """
    state: str

    def __init__(self):
        """
        Default state is menu
        """
        self.state = "menu"

    def set_to_menu(self) -> None:
        """
        changes the state to "menu"
        """
        self.state = "menu"

    def set_to_pause(self) -> None:
        """
        changes the state to "pause"
        """
        self.state = "pause"

    def set_to_running(self) -> None:
        """
        changes the state to "running"
        """
        self.state = "running"

    def __eq__(self, other):
        return self.state == other
