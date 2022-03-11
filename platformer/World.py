import pygame
from platformer.gameConstants import gameConstants
from platformer.Exit import Exit


class World():
    def __init__(self, data, gameConstants):
        self.tile_list = []
        self.data = data
        self.exit = pygame.sprite.Group()
        self.gameConstants = gameConstants
        self.update_data()
    def draw(self):
        for tile in self.tile_list:
            self.gameConstants.screen.blit(tile[0], tile[1])
            pygame.draw.rect(self.gameConstants.screen, (255, 255, 255), tile[1], 2)

    def set_data(self,data):
        self.tile_list = []
        self.exit.empty()
        self.data = data
        self.update_data()

    def update_data(self):
        # load images
        dirt_img = pygame.image.load('../platformer/img/dirt.png')
        grass_img = pygame.image.load('../platformer/img/grass.png')
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (self.gameConstants.tile_size, self.gameConstants.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.gameConstants.tile_size
                    img_rect.y = row_count * self.gameConstants.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (self.gameConstants.tile_size, self.gameConstants.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.gameConstants.tile_size
                    img_rect.y = row_count * self.gameConstants.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8:
                    exit = Exit(col_count * self.gameConstants.tile_size, row_count * self.gameConstants.tile_size - (self.gameConstants.tile_size // 2),self.gameConstants)
                    self.exit.add(exit)
                col_count += 1
            row_count += 1