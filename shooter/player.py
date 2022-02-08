import pygame
import random
from projectile import Projectile

# creer une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('./asset/player(pts4).png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 350

    def update_attack(self, points):
        if self.attack - points > points:
            self.attack -= points
        print("reduction de l'attaque du joueur")
        print(self.attack)

    def damage(self, amount):
        # infliger les degats
        if self.health - amount > amount:
            self.health -= amount
            print("Joueur mort")

    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 10, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 10, self.rect.y - 10, self.health, 5])

    def launch_projectile(self):
        # creer une nouvelle instance le la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity