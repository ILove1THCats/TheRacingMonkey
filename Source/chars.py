import pygame
from scene import Scene
from globals import *

class Yoshi:
    def __init__(self, app):
        self.app = app
        self.image = pygame.image.load("img\F1LX4AjWYAAXwHF.jpg")

    def update(self):
        pass

    def draw(self):
        self.app.screen.blit(self.image, (100,0))

