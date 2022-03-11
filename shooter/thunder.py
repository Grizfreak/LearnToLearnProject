import pygame
import random


# classe pour gerer la pluie d'éclaire
class Thunder(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.velocity = random.randint(10, 20)
        # definir l'image
        self.image = pygame.image.load('../shooter/asset/thunder.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(250, 1300)
        self.rect.y = - random.randint(0, 400)
        self.game = game

    def remove(self):
        print('suppression de l eclaire')
        self.game.all_thunder.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        # detection du sol
        if self.rect.y >= 650:
            self.remove()

        # detection du monstre
        for monster in self.game.check_collision(self, self.game.all_monsters):
            # retirer l'éclaire
            self.remove()
            # appliquer les dégats
            monster.damage(100)
            print("monstre foudroyé !")
