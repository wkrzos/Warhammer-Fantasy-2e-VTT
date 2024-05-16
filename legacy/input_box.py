import pygame
from pygame.locals import *
from frontend.util.color_constants import *

class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        """
        Initialize an InputBox.

        Args:
            x (int): The x-coordinate of the top-left corner of the input box.
            y (int): The y-coordinate of the top-left corner of the input box.
            w (int): The width of the input box.
            h (int): The height of the input box.
            font (pygame.font.Font): The font used for rendering the text.
            text (str): The default text in the input box. Defaults to an empty string.
        """
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        Handle events for the input box.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = BLUE if self.active else BLACK
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        """
        Update the input box. Resize the box if the text is too long.
        """
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, surface):
        """
        Draw the input box on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the input box on.
        """
        # Blit the text.
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(surface, self.color, self.rect, 2)
