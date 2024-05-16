import pygame
from pygame.locals import *
from frontend.util.color_constants import *

class Dropdown:
    def __init__(self, x, y, w, h, font, options, default_text='Select'):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('black')
        self.font = font
        self.options = options
        self.text = default_text
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = False
        self.selected = False
        self.dropdown_rects = [pygame.Rect(x, y + h * (i + 1), w, h) for i in range(len(options))]
        self.option_surfaces = [self.font.render(option, True, self.color) for option in options]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
                self.selected = False

            if self.active:
                for i, rect in enumerate(self.dropdown_rects):
                    if rect.collidepoint(event.pos):
                        self.text = self.options[i]
                        self.txt_surface = self.font.render(self.text, True, self.color)
                        self.active = False
                        self.selected = True
                        break
        self.color = BLUE if self.active else BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

        if self.active:
            for i, rect in enumerate(self.dropdown_rects):
                pygame.draw.rect(surface, self.color, rect, 2)
                surface.blit(self.option_surfaces[i], (rect.x + 5, rect.y + 5))
