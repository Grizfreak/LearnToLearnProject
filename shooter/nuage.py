import pygame


class Nuage(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('../shooter/asset/nuage.png')
        self.rect = self.image.get_rect()
        self.rect.x = -300
        self.rect.y = 20
        self.game = game

    def remove(self):
        print("suppression du nuage")
        self.game.all_nuages.remove(self)

    def spawn(self):
        if not self.rect.x == 445:
            self.rect.x += self.velocity
        else:
            self.game.spawn_thunder()
            self.rect.x += self.velocity
        if self.rect.x >= 1400:
            self.remove()


