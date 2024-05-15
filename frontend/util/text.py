import pygame
from pygame.locals import *
from util.color_constants import *

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        
        self.fontname = options.get('fontname', None)
        self.fontsize = options.get('fontsize', 72)
        self.fontcolor = options.get('fontcolor', BLACK)
        self.set_font()
        self.render()
        
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        
    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        
    def draw(self, surface):
        surface.blit(self.img, self.rect)
