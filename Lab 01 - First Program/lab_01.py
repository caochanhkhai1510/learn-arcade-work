# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade


# Constants
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Race Betting Game"
RADIUS = 100

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.SKY_BLUE)
# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()