import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create a new instance of the Player class before each test
        self.player = Player()

    def test_turn_left(self):
        # Test whether turn_left() correctly changes the heading of the player turtle to the left
        initial_heading = self.player.heading()
        self.player.turn_left()
        new_heading = self.player.heading()
        self.assertGreater(new_heading, initial_heading)

    def test_turn_right(self):
        # Test whether turn_right() correctly changes the heading of the player turtle to the right
        initial_heading = self.player.heading()
        self.player.turn_right()
        new_heading = self.player.heading()
        self.assertLess(new_heading, initial_heading)

    def test_create_missile(self):
        # Test whether create_missile() correctly creates a new missile object with the expected position and heading,
        # and adds it to the missiles list
        initial_num_missiles = len(self.player.missiles)
        self.player.create_missile()
        new_num_missiles = len(self.player.missiles)
        self.assertEqual(new_num_missiles, initial_num_missiles + 1)
        new_missile = self.player.missiles[-1]
        self.assertEqual(new_missile.position(), (0, -200))
        self.assertEqual(new_missile.heading(), self.player.heading())

    def test_fire(self):
        # Test whether fire() correctly moves each missile object in the missiles list forward by 10 units,
        # and whether the positions of the missiles have changed relative to their initial positions
        initial_missile_positions = [m.position() for m in self.player.missiles]
        self.player.create_missile()
        self.player.fire()
        new_missile_positions = [m.position() for m in self.player.missiles]
        self.assertNotEqual(new_missile_positions, initial_missile_positions)
        self.assertEqual(len(new_missile_positions), len(initial_missile_positions) + 1)
        for i, pos in enumerate(new_missile_positions[:-1]):
            self.assertEqual(pos[0], initial_missile_positions[i][0])
            self.assertGreater(pos[1], initial_missile_positions[i][1])

if __name__ == '__main__':
    unittest.main()
