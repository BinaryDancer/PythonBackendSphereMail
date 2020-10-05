import unittest

from XOgame import XOGame
from XOExceptions import BadInput


class TestXOgame(unittest.TestCase):
    def setUp(self):
        self.game = XOGame()

    def test_validate(self):
        with self.assertRaises(BadInput):
            self.game.validate('test')

        with self.assertRaises(BadInput):
            self.game.validate(10)

        with self.assertRaises(BadInput):
            self.game.validate(-1)

        x, y = XOGame.get_coordinate(9)
        self.game.put_figure(x, y)
        with self.assertRaises(BadInput):
            self.game.validate(9)

        self.assertEqual(self.game.validate(5), (1, 1))

    def test_put_figure(self):
        self.assertEqual(self.game._playground[0][0], 1)
        x, y = XOGame.get_coordinate(1)
        self.game.put_figure(x, y)
        self.assertEqual(self.game._playground[0][0], -1)

    def test_change_turn(self):
        self.assertEqual(self.game._player, -1)
        self.game.change_turn()
        self.assertEqual(self.game._player, 0)
        self.game.change_turn()
        self.assertEqual(self.game._player, -1)

    def test_have_winner(self):
        self.assertFalse(self.game.have_winner())
        x, y = XOGame.get_coordinate(1)
        self.game.put_figure(x, y)
        x, y = XOGame.get_coordinate(2)
        self.game.put_figure(x, y)
        x, y = XOGame.get_coordinate(3)
        self.game.put_figure(x, y)
        self.assertEqual(self.game.have_winner(), -1)


if __name__ == '__main__':
    unittest.main()
