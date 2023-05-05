import unittest
from scoreboard import Scoreboard

class TestScoreboard(unittest.TestCase):
    
    def setUp(self):
        # Create a new instance of the Scoreboard class before each test
        self.scoreboard = Scoreboard()
        
    def test_initial_score(self):
        # Test whether the initial score is set to 0 when a new Scoreboard object is created
        self.assertEqual(self.scoreboard.score, 0)
        
    def test_increase_score(self):
        # Test whether increase_score() correctly increases the score by 1 each time it is called
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 1)
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 2)
        
    def test_write_score(self):
        # Test whether write_score() correctly returns the expected string representation of the score
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.write_score(), "Score: 1")
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.write_score(), "Score: 2")
        
    def test_game_over(self):
        # Test whether game_over() correctly returns the string "Game Over!"
        self.assertEqual(self.scoreboard.game_over(), "Game Over!")
        
if __name__ == '__main__':
    unittest.main()
