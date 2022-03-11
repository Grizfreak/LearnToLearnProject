import os.path

import pygame
from platformer.GravityState import GravityState


class gameConstants():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.actualLevel = 0
        self.screen_width = 1000
        self.screen_height = 1000
        self.gravity = GravityState.BOTTOM

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Platformer')

        # define game variables
        self.tile_size = 50

        # load images
        self.sun_img = pygame.image.load('../platformer/img/sun.png')
        self.bg_img = pygame.image.load('../platformer/img/sky.png')

        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
        self.FONT = pygame.font.Font(None, 32)
