import pygame
from gameConstants import *
class World():
    def __init__(self, data,gameConstants):
        self.tile_list = []
        self.gameConstants = gameConstants
        #load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (gameConstants.tile_size, gameConstants.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gameConstants.tile_size
                    img_rect.y = row_count * gameConstants.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (gameConstants.tile_size, gameConstants.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * gameConstants.tile_size
                    img_rect.y = row_count * gameConstants.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            self.gameConstants.screen.blit(tile[0], tile[1])
            pygame.draw.rect(self.gameConstants.screen, (255, 255, 255), tile[1], 2)

