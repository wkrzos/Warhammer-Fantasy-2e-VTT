import pygame
import sys
from fpdf import FPDF

pygame.init()

# Screen dimensions and settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Warhammer Fantasy Character Sheet")
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()
input_box_color_active = pygame.Color('lightskyblue3')
input_box_color_inactive = pygame.Color('gray15')
font_color = pygame.Color('white')

# Text input class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = input_box_color_inactive
        self.text = text
        self.txt_surface = font.render(text, True, font_color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = input_box_color_active if self.active else input_box_color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, font_color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def export_to_pdf(text_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for key, value in text_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    pdf.output("character_sheet.pdf")

def main():
    input_boxes = [InputBox(100, 100, 140, 32, 'Strength'),
                   InputBox(100, 150, 140, 32, 'Intelligence'),
                   InputBox(100, 200, 140, 32, 'Dexterity'),
                   InputBox(100, 250, 140, 32, 'Constitution'),
                   InputBox(100, 300, 140, 32, 'Charisma'),
                   InputBox(100, 350, 140, 32, 'Wisdom')]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    # Gather data for export
    text_data = {box.text.split()[0]: box.text.split()[1] if len(box.text.split()) > 1 else "" for box in input_boxes}
    export_to_pdf(text_data)

if __name__ == '__main__':
    main()
