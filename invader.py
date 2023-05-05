from turtle import Turtle, colormode
import random

colormode(255)

class Invader:
    def __init__(self):
        self.enemies = []  # Initialize the list of enemy turtles to an empty list
        self.create_invader()   # Call the create_invader() method to create the first enemy turtle
    
    def create_invader(self):
        """
        Create a new enemy turtle with a random color, shape, position, and heading, and add it to the list of enemy turtles.
        """
        random_number = random.randint(1,6)   # Generate a random number from 1 to 6
        if random_number == 1:   # If the random number is 1, create a new enemy turtle
            new_invader = Turtle()   # Create a new Turtle object
            r = random.randint(0, 255)   # Generate a random red component for the color
            g = random.randint(0, 255)   # Generate a random green component for the color
            b = random.randint(0, 255)   # Generate a random blue component for the color
            new_invader.color((r,g,b))   # Set the color of the new turtle
            new_invader.penup()   # Lift the pen up so that the turtle does not draw a line
            new_invader.shape("turtle")   # Set the shape of the turtle to be a turtle
            new_invader.goto(random.randint(-300, 300), random.randint(350, 400))   # Move the turtle to a random position above the screen
            new_invader.setheading(new_invader.towards(0, -200))   # Set the heading of the turtle towards the player turtle
            self.enemies.append(new_invader)   # Add the new enemy turtle to the list of enemy turtles
    
    def move(self):
        """
        Move each enemy turtle in the list forward by 5 units.
        """
        for e in self.enemies:
            e.forward(5)
