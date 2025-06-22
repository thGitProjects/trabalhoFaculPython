
import pygame
from Menu import  Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 400))

    def run (self):
        while True:
            menu = Menu(self.window)
            menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()