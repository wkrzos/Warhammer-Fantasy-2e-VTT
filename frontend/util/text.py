import pygame
from pygame.locals import *

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        
        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()
        
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        
    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        
    def draw(self):
        App.screen.blit(self.img, self.rect)