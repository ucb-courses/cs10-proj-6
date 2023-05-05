from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        # Initialize the player turtle with a turtle shape, a blue color, and a size of 2x2
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(2,2)
        self.setheading(90)        
        self.goto(0, -200)
        self.color("blue")
        
        # Initialize the list of missiles to an empty list
        self.missiles = [] 

    def turn_left(self):
        # Rotate the player turtle 5 degrees to the left
        self.setheading(self.heading() + 5)
        

    def turn_right(self):
        # Rotate the player turtle 5 degrees to the right
        self.setheading(self.heading() - 5)
        

    def create_missile (self):
        # Create a new missile object with a red color, the same heading as the player turtle, and a position just
        # above the player turtle's position. Append the new missile object to the missiles list.
        new_missile = Turtle()
        new_missile.penup()
        new_missile.goto(0, -200)
        new_missile.color("red")
        new_missile.setheading(self.heading())
        self.missiles.append(new_missile)
        
    def fire(self):
        # Move each missile object in the missiles list forward by 10 units. This is equivalent to "firing" the missiles.
        for m in self.missiles:
            m.forward(10)
