import sys
import os
import pygame
from frontend.util.text import Text
from frontend.util.input_box import InputBox
from frontend.util.color_constants import *

class CharacterSheet:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 1200
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Character Sheet')
        self.input_boxes = {
            'name': InputBox(150, 85, 200, 25),
            'race': InputBox(150, 115, 200, 25),
            'current_career': InputBox(550, 85, 150, 25),
            'previous_careers': InputBox(550, 115, 150, 25)
        }
        self.clock = pygame.time.Clock()
        self.running = True

    def draw_label(self, surface, text, pos, font_size=20):
        Text(text, pos, fontsize=font_size).draw(surface)
    
    def draw_input_field(self, surface, rect):
        pygame.draw.rect(surface, BLACK, rect, 2)

    def draw_character_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 50, 700, 100), 2)
        Text('CHARACTER', (55, 55), fontsize=30).draw(surface)
        
        self.draw_label(surface, 'Name:', (55, 90), font_size=20)
        self.input_boxes['name'].draw(surface)
        
        self.draw_label(surface, 'Race:', (55, 120), font_size=20)
        self.draw_input_field(surface, pygame.Rect(150, 115, 200, 25))
        
        self.draw_label(surface, 'Current Career:', (400, 90), font_size=20)
        self.draw_input_field(surface, pygame.Rect(550, 85, 150, 25))
        
        self.draw_label(surface, 'Previous Careers:', (400, 120), font_size=20)
        self.draw_input_field(surface, pygame.Rect(550, 115, 150, 25))
    
    def draw_personal_details_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 160, 700, 150), 2)
        Text('PERSONAL DETAILS', (55, 165), fontsize=30).draw(surface)

    def draw_character_profile_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 320, 700, 150), 2)
        Text('CHARACTER PROFILE', (55, 325), fontsize=30).draw(surface)

    def draw_weapons_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 480, 700, 100), 2)
        Text('WEAPONS', (55, 485), fontsize=30).draw(surface)

    def draw_armour_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 590, 700, 100), 2)
        Text('ARMOUR', (55, 595), fontsize=30).draw(surface)

    def draw_experience_points_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 700, 300, 100), 2)
        Text('EXPERIENCE POINTS', (55, 705), fontsize=30).draw(surface)

    def draw_combat_movement_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(370, 700, 380, 100), 2)
        Text('COMBAT MOVEMENT', (375, 705), fontsize=30).draw(surface)

    def draw_action_summary_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 810, 700, 150), 2)
        Text('ACTION SUMMARY', (55, 815), fontsize=30).draw(surface)

    def draw_armour_points_section(self, surface):
        pygame.draw.rect(surface, BLACK, pygame.Rect(50, 970, 700, 200), 2)
        Text('ARMOUR POINTS', (55, 975), fontsize=30).draw(surface)
        # TODO: Add drawing for the human figure and points (this can be done using lines and circles)
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for box in self.input_boxes.values():
                    box.handle_event(event)
            
            self.window.fill(WHITE)
            self.draw_character_section(self.window)
            self.draw_personal_details_section(self.window)
            self.draw_character_profile_section(self.window)
            self.draw_weapons_section(self.window)
            self.draw_armour_section(self.window)
            self.draw_experience_points_section(self.window)
            self.draw_combat_movement_section(self.window)
            self.draw_action_summary_section(self.window)
            self.draw_armour_points_section(self.window)
            
            for box in self.input_boxes.values():
                box.update()
            
            pygame.display.flip()
            self.clock.tick(30)
        
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    character_sheet = CharacterSheet()
    character_sheet.run()
