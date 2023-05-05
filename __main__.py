import sys
import os

# Add the current file's directory to the system path to ensure imports work correctly
sys.path.append(os.path.dirname(__file__))

def main():
    # Check if the Python version is 3.7 or higher
    if sys.version_info[0] < 3 or sys.version_info[1] < 7:
        print("Program requires python 3.7+")
        exit(1)
    
    # Try to import the turtle module, and exit if it fails
    try:
        import turtle
    except Exception as e:
        print(e)
        print("Failed to import turtle")
        exit(1)

    # Try to import the view module, which contains the game's main menu
    try:
        import view
    except Exception as e:
        print(e)
        print("Can not import view.py")
        exit(1)

    # Call the display_main_menu function from the view module to start the game
    view.display_main_menu()
    

# Check if the script is being run as the main module and call the main function
if __name__ == "__main__":
    main()
