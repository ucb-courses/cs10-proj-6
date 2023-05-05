from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the scoreboard turtle with a hidden turtle shape and a pen up. Set the initial score to 0,
        # and call the write_score() method to write the initial score on the screen.
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.score = 0    
        self.write_score()    
        
    def write_score(self):
        # Clear the screen, write the current score on the screen using a custom font and font size,
        # and return the string representation of the current score.
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font=("Courier",25, "bold"))
        return "Score: " + str(self.score)
        
    def increase_score(self):
        # Increase the score by 1 and call the write_score() method to update the score on the screen.
        self.score += 1
        self.write_score()
        
    def game_over(self):
        # Move the scoreboard turtle to the center of the screen and write "Game Over!" using a custom font and font size.
        # Return the string "Game Over!".
        self.goto(0,0)
        self.write("Game Over!", align = "center", font=("Courier",30, "bold"))
        return "Game Over!"
