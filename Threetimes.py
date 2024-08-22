"""
Basic "Hello, World!" program in Pygame Zero

This program is designed to demonstrate the basic capabilities
of Pygame Zero. It will:
- Create a game window
- Fill the background with white
- Draw some basic shapes in different colors
- Draw some text in a specified size and color
"""

x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

# Import pgzrun allows the program to run in Python IDLE
import pgzrun
import pygame

import math

# Set the width and height of your output window, in pixels
WIDTH = 1000
HEIGHT = 800

keys_pressed = set()
player_position_x = WIDTH /2
player_position_y = HEIGHT /2
enemy_position_x = 25
enemy_position_y = 75

def on_key_down(key):
    # move cirkel
    global keys_pressed
    keys_pressed.add(key)
        
def on_key_up(key):
    global keys_pressed
    keys_pressed.remove(key)

def update():
    global player_position_x
    global player_position_y

    global enemy_position_x
    global enemy_position_y

    if keys.A in keys_pressed: 
        player_position_x -= 2

    if keys.D in keys_pressed:
        player_position_x += 2
 
    if keys.W in keys_pressed:
        player_position_y -= 2

    if keys.S in keys_pressed:
        player_position_y += 2

    (enemy_move_delta_x, enemy_move_delta_y) = enemy_move_delta(player_position_x, player_position_y)
    enemy_position_x = enemy_position_x + enemy_move_delta_x
    enemy_position_y = enemy_position_y + enemy_move_delta_y

def draw():
    """Draw is called once per frame to render everything on the screen"""

    # Clear the screen first
    screen.clear()


    # Set the background color to white
    screen.fill("brown")

    # Draw a blue circle with a radius of 50 in the center of the screen
    screen.draw.filled_circle((player_position_x, player_position_y), 50, "darkgreen")

    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('1', False, (0, 0, 0)) 
    screen.blit(text_surface, (0,0))

    # Draw a blue circle with a radius of 50 in the center of the screen
    screen.draw.filled_circle((enemy_position_x, enemy_position_y), 50, "red")

def enemy_move_delta(player_position_x, player_position_y):
    speed = 2

    distance_to_player_x = player_position_x - enemy_position_x
    distance_to_player_y = player_position_y - enemy_position_y
    distance_to_player = math.sqrt((distance_to_player_x**2) + (distance_to_player_y**2))

    cos = distance_to_player_x / distance_to_player
    sin = distance_to_player_y / distance_to_player
    
    new_distance_to_player_x = speed * cos
    new_distance_to_player_y = speed * sin

    return (new_distance_to_player_x, new_distance_to_player_y)

# Run the program
pgzrun.go()