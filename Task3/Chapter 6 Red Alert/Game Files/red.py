# -*- coding: utf-8 -*-

import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint
import time

#Declare constants
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
type_dict = {
    "snowflake":"-snowflake",
             "star":"-star"
}
FINAL_LEVEL = int(input("What is the level you would like to go to?: "))
lvl_of_difficulty = {
    "Easy": 30,
    "Medium":15,
    "Hard": 8,
    "Really Hard": 3
}
lvl_selection = input("What Level of Difficulty would you Like to Play?:")
START_SPEED = lvl_of_difficulty[lvl_selection]
COLORS = ["green", "blue", "purple", "red"]
CHAR_SEL = input("What color would you like your character to be?: ")
TYPE_SEL = input("Would you like a snowflake or a star?: ")
type_sel = type_dict[TYPE_SEL]
COLORS.remove(CHAR_SEL)

#Declare global variables
game_over = False
game_complete = False
current_level = 1

#Keep track of the stars on the screen
stars = []
animations = []

#Draw the stars
def draw():
    global stars, current_level, game_over, game_complete, ply_agn
    screen.clear()
    screen.blit("space", (0,0)) #add a background image to the game window
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON! You Made it to Level {}".format(FINAL_LEVEL), "Try Again? You were on the {} difficulty this time".format(lvl_selection))
    else:
        for star in stars:
            star.draw()

def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars):
    #return[]
    colors_to_create = [CHAR_SEL]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(colors_to_create):
    #return[]
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + type_sel)
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    #pass
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars(stars_to_animate):
    #pass
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)
        
def handle_game_over():
    global game_over 
    game_over = True


def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if CHAR_SEL in star.image:
                red_star_click()
            else:
                handle_game_over()


def red_star_click():
    global current_level, stars, animations, game_complete 
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        stars = []
        animations = []
        
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
            
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTER_X, CENTER_Y+30),
                     color=FONT_COLOR)


pgzrun.go()