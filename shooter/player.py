import pygame
import random
import time
from projectile import Projectile


# creer une classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.isJump = False
        self.timeInAir = 0
        self.isGravityDel = -1
        self.gravitycount = 0
        self.game = game
        self.health = 100
        self.shield = 25
        self.max_health = 100
        self.attack = 15
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('./asset/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 350
        self.gravity = True
        self.num_of_secs = 5

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

    def add_health(self, surface):
        # dessiner la barre de vie supplémentaire
        pygame.draw.rect(surface, (0, 128, 255), [self.rect.x + self.health, self.rect.y - 10, self.health + self.shield, 5] )

    def launch_projectile(self):
        # creer une nouvelle instance le la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def jump(self):
        if self.isJump and self.timeInAir == 0:
            self.rect.y -= 150
            self.timeInAir += 1
        elif self.isJump:
            self.timeInAir += 1
        if self.timeInAir >= 20:
            self.timeInAir = 0
            self.isJump = False
            self.rect.y += 150

    def del_gravity(self):
        print("suppretiopn de la gravité du joueur")
        if self.isGravityDel == -1:
            self.gravity = False
            self.isGravityDel += 1
        #Finished effect
        elif self.isGravityDel == 1:
            self.rect.y = 350
            self.gravity = True
            self.isGravityDel = -1

    def gravitycheck(self):
        if self.isGravityDel == 0 and self.gravitycount >= 450:
            self.isGravityDel==1
            self.rect.y = 350
            self.gravity = True
            self.isGravityDel = -1
            self.gravitycount = 0
        elif self.isGravityDel == 0:
            self.gravitycount += 1
            print(self.gravitycount)

