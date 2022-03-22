import pygame


class Wave(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load('./data/shooter/asset/wave.png')
        # self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = - 500
        self.rect.y = 373
        self.game = game

    def remove(self):
        print("suppression de la vague")
        self.game.all_waves.remove(self)

    def spawn(self):
        self.rect.x += self.velocity
        if self.rect.x >= 1400:
            self.remove()
