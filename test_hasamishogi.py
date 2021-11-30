import unittest
from HasamiShogiGame import *

class HasamiTests(unittest.TestCase):
    """List of tests used during the development of Library.py its functions"""
    def test01_vertical_move(self):
        """This test ensures that the turns alternate after a successful move."""
        print("Test 01")
        game = HasamiShogiGame()
        player = game.get_active_player()
        self.assertEqual(player, "BLACK")
        game.make_move("i1", "f1")
        move2 = game.get_active_player()
        self.assertEqual(move2, "RED")
        game.display_game()
        game.make_move("a1", "e1")
        move3 = game.get_active_player()
        game.display_game()
        self.assertEqual(move3, "BLACK")

    
    def test02_horizontal_move(self):
        "This test checks that the pieces can move up without obstructions."""
        game = HasamiShogiGame()
        game.make_move("i1", "f1")
        game.make_move("a1", "e1")
        # print(f"SHOULD BE: {game.get_active_player()}")
        # checks to move right
        game.make_move("f1", "f5")
        game.make_move("e1", "e5")
        game.display_game()
        # checks to move left
        game.make_move("f5", "f1")
        game.make_move("e5", "e1")
        # checks to move right but out of bounds
        game.make_move("f1", "w2")
        # checks to move left but out of bounds
        game.make_move("f5", "f9")
        game.make_move("i2", "e2")
        game.display_game()

    def test03_vertical_up_obstructed(self):
        "This test checks that the pieces can down without obstructions."""
        game = HasamiShogiGame()
        not_allowed = game.make_move("i1", "a1")
        self.assertFalse(not_allowed)
        # game.make_move("a1", "i1")
        filled_space = game.get_square_occupant("i1")
        game.display_game()
        self.assertEqual(filled_space, "BLACK")
    
    def test04_move_to_index(self):
        """This test checks and determines if the square is converted correctly to an index."""
        game = HasamiShogiGame()
        square = game.move_to_index("a1")
        self.assertEqual(square, "00")
        square = game.move_to_index("z0")
        self.assertFalse(square)
        square = game.move_to_index("i9")
        self.assertEqual(square, "88")

    def test05_index_to_move(self):
        """This converts an index to a move parameter."""
        game = HasamiShogiGame()
        square = game.index_to_move("00")
        self.assertEqual(square, "a1")
        square = game.index_to_move("76")
        self.assertEqual(square, "h7")

    def test_05_vertical_capture(self):
        """This test checks the potential for a potential capture vertically above."""
        game = HasamiShogiGame()
        game.make_move('i2','b2')
        game.make_move('a3','c3')
        game.make_move('b2','b3')
        game.make_move('a9','b9')
        game.make_move('i3','d3')
        game.display_game()
        game.get_num_captured_pieces("RED")
    
    def test_06_vertical_capture_double(self):
        """This test checks the potential for a potential capture vertically above."""
        game = HasamiShogiGame()
        game.make_move('i5','e5')
        game.make_move('a5','d5')
        game.make_move('i4','f4')
        game.make_move('a9','g9')
        game.make_move('f4','f5') # Black
        print(game.get_active_player())
        game.make_move('g9','g5')
        game.display_game()
        game.get_num_captured_pieces("RED")
        game.get_num_captured_pieces("BLACK")

    def test_07_vertical_capture_down_single(self):
        """This test checks the potential for a potential capture vertically below."""
        game = HasamiShogiGame()
        game.make_move('i5','e5')
        game.make_move('a4','f4')
        game.make_move('i4','g4')
        game.make_move('f4','f5')
        game.make_move('g4','g5')
        game.display_game()
        game.get_num_captured_pieces("RED")
        game.get_num_captured_pieces("BLACK")

    def test_08_check_left(self):
        game = HasamiShogiGame()
        pos1 = game.move_to_index('a1')
        pos2 = game.move_to_index('b2')
        pos3 = game.move_to_index('c3')
        pos4 = game.move_to_index('i9')
        self.assertFalse(game.check_left(pos1)) #1 space from left wall
        self.assertFalse(game.check_left(pos2)) #2 space from left wall
        self.assertTrue(game.check_left(pos3))  #3 spaces from left wall
        self.assertTrue(game.check_left(pos4))  #4 spaces from left wall    

    def test_09_check_right(self):
        game = HasamiShogiGame()
        pos1 = game.move_to_index('a9')
        pos2 = game.move_to_index('b8')
        pos3 = game.move_to_index('c7')
        pos4 = game.move_to_index('i7')
        self.assertFalse(game.check_right(pos1)) #1 space from rightwall
        self.assertFalse(game.check_right(pos2)) #2 space from rightwall
        self.assertTrue(game.check_right(pos3))  #3 spaces from right wall
        self.assertTrue(game.check_right(pos4))  #2 spaces from right wall    

    def test_10_capture_bot_right_corner(self):
        game = HasamiShogiGame()
        game._game_board = \
            [["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["B", "R", "R", "_", "_", "_", "R", "B", "B"],
            ["_", "R", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "B"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "B"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "R"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "B"],
            ["_", "R", "_", "_", "B", "R", "R", "_", "R"]]
        game.make_move('c8', 'i8')
        game.make_move('d2', 'd9')
        game.display_game()
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(3, red_caps)
        black_caps = game.get_num_captured_pieces('black')
        self.assertEqual(2, black_caps)
        # self.assertFalse(post_game_move)
    
    def test_11_capture_left(self):
        game = HasamiShogiGame()
        game.make_move('i6','b6')
        game.make_move('a5','b5')
        game.make_move('i4','b4')
        game.display_game()
        game.get_num_captured_pieces("RED")
        game.get_num_captured_pieces("BLACK")

    def test_12_capture_left_multiples(self):
        """Checks if multiple pieces are captured when checking left."""
        game = HasamiShogiGame()
        game.make_move('i4','h4')
        game.make_move('a3','h3')
        game.make_move('i5','h5')
        game.make_move('a9','b9')
        game.make_move('i6','h6')
        game.make_move('a7','h7')
        game.display_game()
        game.get_num_captured_pieces("RED")
        game.get_num_captured_pieces("BLACK")
        self.assertEqual(3, game.get_num_captured_pieces("BLACK"))

    def test_13_capture_right_multiples(self):
        """Checks if multiple pieces are captured when checking right."""
        game = HasamiShogiGame()
        game.make_move('i4','h4')
        game.make_move('a7','h7')
        game.make_move('i5','h5')
        game.make_move('a9','b9')
        game.make_move('i6','h6')
        game.make_move('a3','h3')
        game.display_game()
        game.get_num_captured_pieces("RED")
        game.get_num_captured_pieces("BLACK")
        self.assertEqual(3, game.get_num_captured_pieces("BLACK"))

    def test_14_corner_scenarios(self):
        """Edge scenarios along the borders. Includes multi-capture. (NOT CORNERS)"""
        game = HasamiShogiGame()
        game.make_move('i2','g2')
        game.make_move('a1','h1')
        game.make_move('g2','g1')
        game.make_move('a2','i2')
        game.make_move('i9','b9')
        game.make_move('a8','c8')
        game.make_move('g1','a1')
        game.make_move('c8','c9')
        game.make_move('i8','a8')
        game.make_move('c9','i9')
        # game.display_game()
        game.make_move('a1','a2')
        game.make_move('i9', 'i8')
        game.display_game()

    def test_15_game_state(self):
        "Tests the game state scenarios."
        game = HasamiShogiGame()
        state = game.get_game_state()
        print(state)
        self.assertEqual(state, "UNFINISHED")
        game.make_move('i2', 'g2')
        game.make_move('a1', 'h1')
        game.make_move('g2', 'g1')
        game.display_game()
        game.make_move('a2', 'i2')
        game.make_move('i9', 'b9')
        game.make_move('a8', 'c8')
        game.make_move('g1', 'a1')
        game.make_move('a9', 'a8')
        game.make_move('b9', 'a9')
        game.make_move('c8', 'h8')
        game.display_game()
        game.get_square_occupant('a1')
        game.make_move('a1', 'a2')
        state1 = game.get_game_state()
        self.assertEqual("UNFINISHED", state1)
        

    # def test_16_corner_check_top_right(self):
        """Tests a capture scenario for the top right corner."""
        game = HasamiShogiGame()
        game.make_move('i9', 'b9')
        game.make_move('a8', 'c8')
        game.make_move('i8', 'd8')
        game.make_move('c8', 'c2')
        game.make_move('d8', 'a8')
        game.display_game()
        state = game.get_game_state()
        self.assertEqual("UNFINISHED", state)
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(1, red_caps)

    def test_17_corner_check_top_left(self):
        """Tests a capture scenario for the top left corner."""
        game = HasamiShogiGame()
        game._game_board = [["R", "B", "R", "R", "R", "R", "R", "R", "B"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["B", "_", "B", "B", "B", "B", "B", "B", "R"]]
        game.display_game()
        game.make_move('i1', 'b1')
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(1, red_caps)
        game.make_move('i9','b9')
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(1, red_caps)
        black_caps = game.get_num_captured_pieces('black')
        self.assertEqual(1, black_caps)
        game.display_game()


    def test_18_boundaries_vertical(self):
        """Checks to make sure the vertical bounds are properly checked."""
        game = HasamiShogiGame()
        game._game_board = [["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "B", "_", "_", "_", "_", "_", "_", "_"],
            ["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["R", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["B", "_", "B", "B", "B", "B", "B", "B", "R"]]
        game.make_move('e2','e1')
        game.display_game()

    def test_19_game_state_red_wins(self):
        """Tests to make sure that RED can win."""
        game = HasamiShogiGame()
        game._game_board = [["_", "_", "_", "R", "R", "R", "R", "R", "R"],
        ["R", "B", "B", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "B", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
        ["R", "B", "B", "B", "B", "B", "B", "B", "_"]]
        game.make_move('B2','A2')
        game.make_move('a9','i9')
        game.make_move('B3','A3')
        game.make_move('B1','A1')
        game.display_game()
        state = game.get_game_state()
        self.assertEqual("RED_WON", state)
        # Games over, should not be able to make a move now
        not_allowed = game.make_move("a1", "a2")
        self.assertFalse(not_allowed)
        not_allowed = game.make_move("e5", "e6")
        self.assertFalse(not_allowed)

    def test_20_double_scenarios(self):
        """Captures left and downward"""
        game = HasamiShogiGame()
        game._game_board = \
            [["_", "B", "R", "R", "_", "_", "_", "_", "B"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"]]
        game.make_move('a9','a5')
        game.display_game()
    
    def test_21_triple_scenarios(self):
        """Captures left, right, and downwards."""
        game = HasamiShogiGame()
        game._game_board = \
            [["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["B", "R", "R", "R", "_", "R", "R", "R", "B"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"]]
        game.make_move('a5','c5')
        game.display_game()
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(7, red_caps)

    def test_22_triple_scenarios_top(self):
        """Captures left, right, and downwards."""
        game = HasamiShogiGame()
        game._game_board = \
            [["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["B", "R", "R", "R", "_", "R", "R", "R", "B"],
            ["_", "R", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "R", "_", "_", "B", "_", "_", "_", "_"]]
        game.display_game()
        game.make_move('i5','c5')
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(7, red_caps)
        game.make_move('d2','c2')
        game.make_move('c5','c3')
        game.display_game()
        red_caps = game.get_num_captured_pieces('red')
        self.assertEqual(8, red_caps)
        post_game_move = game.make_move('c3','c5')
        self.assertFalse(post_game_move)
        post_game_move = game.make_move('i2','i3')
        self.assertFalse(post_game_move)
        game.display_game()

    def test_23_triple_scenarios_top(self):
        """Captures left, right, and downwards. Various invalid move attempts."""
        game = HasamiShogiGame()
        game.make_move('i1', 'i1')
        game.make_move('i1', 'i1')
        game.make_move('i1', 'i1')
        game.make_move('i1', 'i1')
        game.make_move('i1', 'i1')
        game.make_move('a1', 'b1')
        game.make_move('a1', 'b1')
        game.make_move('a1', 'b1')
        game.make_move('i1', 'i2')
        game.make_move('i1', 'h1')
        game.make_move('a1', 'b1')

    def test_24_gradescope(self):
        """Tests to see if error is still encountered in gradescope"""
        game = HasamiShogiGame()
        game.make_move('i4','d4')
        game.make_move('a5','d5')
        game.display_game()

    def test_25_get_sq_occupant(self):
        """Debugging get_square_occupant."""
        game = HasamiShogiGame()
        occupant = game.get_square_occupant('a4')
        self.assertEqual("RED", occupant)
    
    def test_26_blocked_moves(self):
        """Tests to see if the piece can moved to obstructed zones."""
        game = HasamiShogiGame()
        game._game_board = \
            [["_", "_", "_", "_", "R", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "R", "_", "B", "_", "R", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "B", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "B", "_", "_", "_", "_"]]
        # moving vertical/horizontally obstructed
        game.make_move('e5','a5')
        game.make_move('e5','e8')
        game.make_move('e5','e1')
        game.make_move('e5','i5')
        # moving to diagonals
        game.make_move('e5','a1')
        game.make_move('e5','a9')
        game.make_move('e5','i1')
        game.make_move('e5','i9')
        game.display_game()



        
if __name__ == '__main__':
    unittest.main()
