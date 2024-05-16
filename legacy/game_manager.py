import pygame
from pygame.locals import *

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
