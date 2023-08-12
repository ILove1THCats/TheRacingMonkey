import pygame
import sys
from pygame.locals import *
from scene import Scene
from chars import Yoshi
from globals import *

class App: 
    """Create a single window app with multiple scenes"""

    def __init__(self):
        """Initialize pygame and the application"""
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
        self.clock = pygame.time.Clock()

        self.running = True

        self.scene = Scene(self)
        self.char = Yoshi(self)
    
    def run(self):
        """Run the main event loop"""
        while self.running:
            self.update()
            self.draw()
        self.close

    def update(self):
        """Update the game"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

        self.scene.update()
        pygame.display.update()
        self.clock.tick(FPS)

    def draw(self):
        """Art processing"""
        self.scene.draw()
        self.char.draw()

    def close(self):
        """Unleash all the resource"""
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = App()
    game.run()
