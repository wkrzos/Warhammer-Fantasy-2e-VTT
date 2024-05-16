import sys
import os
import pygame

import frontend.util as util
from frontend.util.color_constants import *
from frontend.util.text import Text

""" ##############################
# Testing imports
print(__name__)

try:
    # Trying to find module in the parent package
    from . import color_constants
    print("debug1")
except ImportError:
    print('Relative import failed')

try:
    # Trying to find module on sys.path
    import frontend.util.color_constants
    print("debug2")
except ModuleNotFoundError:
    print('Absolute import failed')
    
try:
    from util.color_constants import *
    print("debug3")
except ModuleNotFoundError:
    print('Absolute import failed')
    
try:
    from frontend.util.color_constants import *
    print("debug4")
except ModuleNotFoundError:
    print('Absolute import failed')
############################## """

def draw_character_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 50, 700, 100), 2)
    Text('CHARACTER', (55, 55), fontsize=30).draw(surface)

def draw_personal_details_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 160, 700, 150), 2)
    Text('PERSONAL DETAILS', (55, 165), fontsize=30).draw(surface)

def draw_character_profile_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 320, 700, 150), 2)
    Text('CHARACTER PROFILE', (55, 325), fontsize=30).draw(surface)

def draw_weapons_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 480, 700, 100), 2)
    Text('WEAPONS', (55, 485), fontsize=30).draw(surface)

def draw_armour_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 590, 700, 100), 2)
    Text('ARMOUR', (55, 595), fontsize=30).draw(surface)

def draw_experience_points_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 700, 300, 100), 2)
    Text('EXPERIENCE POINTS', (55, 705), fontsize=30).draw(surface)

def draw_combat_movement_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(370, 700, 380, 100), 2)
    Text('COMBAT MOVEMENT', (375, 705), fontsize=30).draw(surface)

def draw_action_summary_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 810, 700, 150), 2)
    Text('ACTION SUMMARY', (55, 815), fontsize=30).draw(surface)

def draw_armour_points_section(surface, font):
    pygame.draw.rect(surface, BLACK, pygame.Rect(50, 970, 700, 200), 2)
    Text('ARMOUR POINTS', (55, 975), fontsize=30).draw(surface)
    # TODO: Add drawing for the human figure and points (this can be done using lines and circles)

pygame.init()

width, height = 800, 1200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Character Sheet')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    window.fill(WHITE)
    
    draw_character_section(window, None)
    draw_personal_details_section(window, None)
    draw_character_profile_section(window, None)
    draw_weapons_section(window, None)
    draw_armour_section(window, None)
    draw_experience_points_section(window, None)
    draw_combat_movement_section(window, None)
    draw_action_summary_section(window, None)
    draw_armour_points_section(window, None)

    pygame.display.flip()
    
pygame.quit()
sys.exit()