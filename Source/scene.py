import pygame
from globals import *

class Scene:

    screen_image = { }

    def __init__(self, app, image = pygame.image.load) -> None:
        #Append a new screen and make it the current scene
        self.app = app

    def update(self):
        #Start the game
        pass

    def draw(self):
        self.app.screen.fill('lightblue')