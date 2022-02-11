import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 2)
        self.image = pygame.image.load('./asset/monter(pts4).png')
        self.rect = self.image.get_rect()
        self.rect.x = 1300 + random.randint(0, 300)
        self.rect.y = 375

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nvx nombres de hp <= 0
        if self.health <= 0:
            self.rect.x = 1300 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            self.game.player.update_attack(1)

    def update_health_bar(self, surface):

        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 30 , self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 30 , self.rect.y - 10, self.health, 5])


    def forward(self):
        # le deplacement se fait que si il n'y a pas de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en colision avec le joueur
        else:
            # infliger des degats
            self.game.player.damage(self.attack)