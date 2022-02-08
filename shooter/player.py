import pygame
from projectile import Projectile

# creer une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('./asset/player(pts4).png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 350

    def launch_projectile(self):
        # creer une nouvelle instance le la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity