import time
import turtle
from player import Player
from invader import Invader
from scoreboard import Scoreboard

# Set up the main game window
ws = turtle.Screen()
ws.title("SP23 CS10  - Project 6: Space Invaders")
bgcolor = 'wheat'
ws.bgcolor(bgcolor)
ws.setup(width=600, height=600)
ws.tracer(0)

# Set up a turtle object to display text and UI elements
tp = turtle.Turtle()
tp.penup()
tp.shape('square')
tp.speed('fastest')

# Main game loop
def play_game():
    try:    
        font_size = 18
        upper_left_pos = -200
        tp.clear()
        tp.goto((0, 200))
        
        # Create the player, invader, and scoreboard objects
        player = Player()
        invader = Invader()
        scoreboard = Scoreboard()

        # Set up event listeners for player controls and exiting the game
        ws.listen()
        ws.onkey(player.turn_left, "Left")
        ws.onkey(player.turn_right, "Right")
        ws.onkey(player.create_missile, "space")
        ws.onkey(ws.bye, "Escape")

        # Main game loop
        game_is_on = True
        while game_is_on:
            time.sleep(0.1)
            player.fire()
            invader.create_invader()
            invader.move()
            ws.update()
            
            # End the game if the player goes out of bounds
            if abs(player.xcor()) > 290 or abs(player.ycor()) > 290:
                game_is_on = False

            # Check for collisions between missiles and invaders
            for i in invader.enemies:
                for m in player.missiles:
                    if m.distance(i) < 20:
                        player.missiles.remove(m)
                        invader.enemies.remove(i)
                        m.hideturtle()
                        i.hideturtle()

                    # Remove missiles that have traveled too far
                    if m.distance(player)>600:
                        player.missiles.remove(m)
                        m.hideturtle()
                        scoreboard.increase_score()
                        
                # End the game if an invader gets too close to the player
                if i.distance(player) < 10:
                    game_is_on = False    
        
        ws.update()
        game_over()
    except Exception as er:
        pass

# Display the game over screen
def game_over():
    tp.clear()
    tp.goto((0, 0))
    tp.write('GAME OVER!', move=False, align="center", font=("Arial", 32, "normal"))
    tp.goto((0, -50))
    tp.write('Press (b) to return to main menu.', move=False, align="center", font=("Arial", 15, "italic"))
    turtle.listen()
    turtle.onkey(display_main_menu, 'b')
    ws.mainloop()
    tp.hideturtle()

# view the instruction manual    
def view_tutorial():
    tp.clear()
    align_str = 'left'
    font_setting = ("Cambria", 15, "normal")
    x_p = -200
    tp.goto((x_p, 200))
    tp.write('(key) - function', move=False, align=align_str, font=("Cambria", 15, "bold"))
    tp.goto((x_p, 150))
    tp.write('(space) - to make firing turtle fires missiles. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, 100))
    tp.write('(left) - left-arrow to move firing turtle toward left. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, 50))
    tp.write('(right) - right-arrow to move firing turtle toward right. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, 0))
    tp.write('Note:', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -50))
    tp.write('Press (b) to go back to the main menu. ', move=False, align=align_str, font=("Cambria", 16, "italic"))
    turtle.listen() 
    turtle.onkey(display_main_menu, 'b')
    ws.mainloop()

# Exit the game
def quit_game():
    try: 
        ws.bye()
    except Exception as err:
        pass

# Display the initial menu with options to start or quit the game
def display_main_menu(): 

    font_size = 18
    upper_left_pos = -200
    tp.clear()
    tp.goto((0, 200))
    tp.goto((0, 50))
    tp.write('Press (s) to start.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.goto((0, 0))
    tp.write('Press (t) to view tutorial.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.goto((0, -50))
    tp.write('Press (q) to quit.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.hideturtle()
    
    turtle.onkey(play_game, 's')
    turtle.onkey(view_tutorial, 't')
    turtle.onkey(quit_game, 'q')
    turtle.listen()
    ws.mainloop()
