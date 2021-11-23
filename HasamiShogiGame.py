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
        self._game_board = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"]]
        self._move_tracker = 1      # Tracks the number of moves performed in the game

        # Initializes Empty Game Board
        # for row in range(9):
        #     for column in self._game_board:
        #         # print(f"{row}{column}")
        #         self._game_board.append("_")

    def __repr__(self) -> str:
        """Printable Format of the Board Game State"""
        for i in self._side_label:
            print(self._side_label)

    def display_game(self):
        """Displays the current state of the game. """
        for row in range(self._rows):
            # for column in range(self._columns):
            pass
            for col in self._side_label:
                pass
            print(f"{col} {self._game_board[row]}")

    def get_top(self):
        return self._top_label

    def get_side(self):
        return self._side_label

    def set_RED(self, space):
        """Sets the specified location to RED."""
        if space is None:
            space = "r"
            return True

    def set_BLACK(self):
        if space == "_":
            space = "b"
            return True

    def set_empty(self):
        return None

    def get_game_state(self):
        """Function determines the current progress of the game. If there's a current winner or if its still in play.

        Returns:
            str: state of the board game
        """
        if game_state == None:
            return "UNFINISHED"
        elif game_state == "RED_WON":
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
        if color.upper() == "RED":
            # Returns the number of red pieces captured
            pass
        if color.upper() == "BLACK":
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
            False: if the current move is blocked by any pieces
        """
        pass

    def get_square_occupant(self, square = ""):
        """Determines if the square is occupied or not"""
        if len(square) != 2:
            # Raise error for invalid space or outside of range
            pass
        self._row = square[0]
        self._column = square[1]
        if self._game_board[self._row][self._column] == "BLACK":
            return "BLACK"
        elif self._game_board[self._row][self._column] == "RED":
            return "RED"
        else:
            return "NONE"

    ### Verifying Valid Moves
    def horizontal_move(self, start_loc, end_loc):
        """Checks to see if there are any pieces between the start_loc to the end_loc

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: move is valid
            False: move is not valid (something obstructs)
        """
        pass
    def corner_capture(self, start_loc, end_loc):
        """If the current move is nearby an opponent's corner piece, check to see if another active player's piece resides on the nearby corner. 

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: Captures the corner piece. Updates the active player, and move_tracker
            False: if corner capture condition is not met
        """
        pass

    def horizontal_capture(self, start_loc, end_loc):
        """After a valid move check, determines if the current move is horizontal to an opponent's piece. If so check to see if another active player's piece is on the opposite side. 

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: Captures the opponent's piece piece. Updates number of captured pieces, and move_tracker
            False: if horizontal capture condition is not met
        """
        pass

    def vertical_capture(self, start_loc, end_loc):
        """After a valid move check, determines if the current move is vertical to an opponent's piece. If so check to see if another active player's piece is on the opposite side. 

        Args:
            start_loc (str): a location with an active piece 
            end_loc (str): a valid location to move an active piece

        Returns:
            True: Captures the opponent's piece piece. Updates number of captured pieces, and move_tracker
            False: if vertical capture condition is not met
        """
        pass



game = HasamiShogiGame()
game.display_game()
print("repr representation\n")
print(game)

# move_result = game.make_move('i6', 'e3')
# print(game.get_active_player())
# print(game.get_square_occupant('a4'))
# print(game.get_game_state())