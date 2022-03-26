import pygame


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y,gameConstants):
        pygame.sprite.Sprite.__init__(self)
        self.gameConstants = gameConstants
        img = pygame.image.load('./data/platformer/img/exit.png')
        self.image = pygame.transform.scale(img, (self.gameConstants.tile_size, int(self.gameConstants.tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y