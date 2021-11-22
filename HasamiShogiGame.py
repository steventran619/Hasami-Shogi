# Steven Tran
# CS-162 Project

class HasamiShogiGame():
    """Initializes a game of Hasami Shogi (Japanese Rook-Like Capture Game).
    """
    def __init__(self):
        """Initial Game Board"""
        self._rows = 9
        self._columns = 9
        self._top_label = list(range(1,10))
        self._side_label = ['a','b','c','d','e','f','g','h','i']
        self._game_board = []
        self._move_tracker = 1      # Tracks the number of moves performed in the game

        # Initializes Empty Game Board
        for row in range(self._rows):
            for column in range(self._columns):
                self._game_board[row, column] = "_"

    def get_top(self):
        return self._top_label

    def get_side(self):
        return self._side_label

    def set_RED(self,):
        """Sets the specified location to RED."""
        return "RED"

    def set_BLACK(self):
        return "BLACK"

    def get_square

    def display_game():
        """Displays the current state of the game. """
        for row in self._rows:
            for column in self._columns:
                print(self._game_board)

    def get_game_state(self):
        """Function determines the current progress of the game. If there's a current winner or if its still in play.

        Returns:
            str: state of the board game
        """
        if game_state is None:
            return "UNFINISHED"
        elif game_state is "RED_WON":
            return "RED_WON"
        else:
            return "BLACK_WON"

    def get_active_player(self):
        """Returns whose turn it is based on number of turns partaken

        Returns:
            str: "RED" or "BLACK"
        """
        if move_tracker % 2 == 1:
            return "BLACK"
        else:
            return "RED"

    def get_num_captured_pieces(self, color = None):
        if color.upper() is "RED":
            # Returns the number of red pieces captured
            pass
        if color.upper() is "BLACK":
            # Returns the number of red pieces captured
            pass
        else:
            # Raises some Error for inputting a correct color value.
            pass

    def make_move(self, start_loc, end_loc):
        """Moves a piece from the 1st parameter's location to the 2nd parameter's location as long as it is a valid move. 
        Checks for:
            * Valid Turn (if its RED or BLACK's turn)
            * Valid Move (if the start_loc can actually reach end_loc without any obstructions)

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: updated location with the piece. Also updates start_loc to an empty location again. Updates the active player, and move_tracker
            False: if any moment of the move is invalid
        """
        pass

    def get_square_occupant(self, square = ""):
        """Determines if the square is occupied or not"""
        if len(square) != 2:
            # Raise error for invalid space or outside of range
            pass
        self._row = square[0]
        self._column = square[1]
        if self._game_board[self._row][self._column] is "BLACK":
            return "BLACK"
        elif self._game_board[self._row][self._column] is "RED":
            return "RED"
        else:
            return "NONE"

* A method called `make_move` that takes two parameters - strings that represent the square moved from and the square moved to.  For example, make_move('b3', 'b9').  If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has already been won, then it should just return False.  Otherwise it should make the indicated move, remove any captured pieces, update the game state if necessary, update whose turn it is, and return True.


game = HasamiShogiGame()
game.display_game()

# move_result = game.make_move('i6', 'e3')
# print(game.get_active_player())
# print(game.get_square_occupant('a4'))
# print(game.get_game_state())