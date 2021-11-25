import unittest
from HasamiShogiGame import *

class HasamiTests(unittest.TestCase):
    """List of tests used during the development of Library.py its functions"""
    def test01_get_active_player(self):
        """This test ensures that the turns alternate after a successful move."""
        game = HasamiShogiGame()
        player = game.get_active_player()
        self.assertEqual(player, "BLACK")
        game.make_move("i3", "d3")
        move2 = game.get_active_player()
        self.assertEqual(move2, "RED")
        game.make_move("a1", "b1")
        move3 = game.get_active_player()
        self.assertEqual(move3, "BLACK")
    
    def test02_vertical_up(self):
        "This test checks that the pieces can move up without obstructions."""
        game = HasamiShogiGame()
        game.make_move("i3", "d3")
        new_space = game.get_square_occupant(game.move_to_index("d3"))
        self.assertEqual(new_space, "BLACK")
        old_space = game.get_square_occupant(game.move_to_index("i3"))
        self.assertEqual(old_space, "NONE")

#    def test03_vertical_down(self):
#        "This test checks that the pieces can down without obstructions."""
#        game = HasamiShogiGame()
#        game.make_move("i3", "d3")
#        game.make_move("a1", "i1")
#        filled_space = game.get_square_occupant(game.move_to_index("i1"))
#        game.display_game()
#        self.assertEqual(filled_space, "BLACK")
    
    def test04_move_to_index(self):
        """This test checks and determines if the square is converted correctly to an index."""
        game = HasamiShogiGame()
        square = game.move_to_index("a1")
        self.assertEqual(square, "00")
        square = game.move_to_index("z0")
        self.assertFalse
        square = game.move_to_index("i9")
        self.assertEqual(square, "00")
    

if __name__ == '__main__':
    unittest.main()
