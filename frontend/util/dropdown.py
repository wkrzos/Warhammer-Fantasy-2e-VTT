import pygame
from pygame.locals import *
from frontend.util.color_constants import *

class Dropdown:
    def __init__(self, x, y, w, h, font, options, default_text='Select'):
        """
        Initialize a Dropdown menu.

        Args:
            x (int): The x-coordinate of the top-left corner of the dropdown.
            y (int): The y-coordinate of the top-left corner of the dropdown.
            w (int): The width of the dropdown.
            h (int): The height of the dropdown.
            font (pygame.font.Font): The font used for rendering the text.
            options (list): A list of options to display in the dropdown.
            default_text (str): The default text to display when no option is selected. Defaults to 'Select'.
        """
        # Rectangle representing the dropdown area
        self.rect = pygame.Rect(x, y, w, h)
        # Color of the dropdown border and text
        self.color = pygame.Color('black')
        # Font used to render the text
        self.font = font
        # Options available in the dropdown
        self.options = options
        # The text currently displayed in the dropdown
        self.text = default_text
        # Rendered surface of the current text
        self.txt_surface = self.font.render(self.text, True, self.color)
        # Dropdown active state (True if expanded, False otherwise)
        self.active = False
        # Dropdown selection state (True if an option is selected, False otherwise)
        self.selected = False
        # Rectangles representing each option in the dropdown
        self.dropdown_rects = [pygame.Rect(x, y + h * (i + 1), w, h) for i in range(len(options))]
        # Rendered surfaces of each option
        self.option_surfaces = [self.font.render(option, True, self.color) for option in options]

    def handle_event(self, event):
        """
        Handle events for the dropdown.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Toggle the active state when the dropdown rectangle is clicked
                self.active = not self.active
            else:
                # Close the dropdown if clicked outside of it
                self.active = False
                self.selected = False

            if self.active:
                for i, rect in enumerate(self.dropdown_rects):
                    if rect.collidepoint(event.pos):
                        # Update the selected text and close the dropdown when an option is clicked
                        self.text = self.options[i]
                        self.txt_surface = self.font.render(self.text, True, self.color)
                        self.active = False
                        self.selected = True
                        break
        # Update the color based on the active state
        self.color = BLUE if self.active else BLACK

    def draw(self, surface):
        """
        Draw the dropdown on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the dropdown on.
        """
        # Draw the main dropdown rectangle
        pygame.draw.rect(surface, self.color, self.rect, 2)
        # Draw the current text
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

        if self.active:
            # Draw each option if the dropdown is active
            for i, rect in enumerate(self.dropdown_rects):
                pygame.draw.rect(surface, self.color, rect, 2)
                surface.blit(self.option_surfaces[i], (rect.x + 5, rect.y + 5))
