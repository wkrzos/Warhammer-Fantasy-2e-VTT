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

class App:
    
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640, 240), flags)
        pygame.display.set_caption("Bardzo Fajen VTT")
        
        self.shortcuts = {
            K_q: self.quit,
            K_r: self.restart,
        }
        
        App.running = True
        
    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                elif event.type == KEYDOWN:
                    self.do_shortcut(event)
                    
        pygame.quit()
        
    def do_shortcut(self, event):
        k = event.key
        if k in self.shortcuts:
            self.shortcuts[k]()
        
    def quit(self):
        print("QUIT")
        App.running = False
        
    def restart(self):
        print("RESTART")
        # TODO: Restart logic here
        
if __name__ == "__main__":
    App().run()
