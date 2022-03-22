import pygame
import random
from shooter.animation import AnimateSprite


class Monster(AnimateSprite):

    def __init__(self, game, name):
        super().__init__(name)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1, 2)
        self.rect = self.image.get_rect()
        self.rect.x = 1300 + random.randint(0, 300)
        self.rect.y = 375
        self.is_good = False

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # verifier si son nvx nombres de hp <= 0
        if self.health <= 0:
            self.rect.x = 1300 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            self.game.player.update_attack(1)
            # ajout du score
            self.game.score += 10

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        # dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 30 , self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 30 , self.rect.y - 10, self.health, 5])


    def forward(self):
        if not self.is_good:
            # le deplacement se fait que si il n'y a pas de joueur
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.x -= self.velocity
            # si le monstre est en colision avec le joueur
            else:
                # infliger des degats
                self.game.player.damage(self.attack)
            if self.rect.x <= 0:
                self.rect.x = 1300 + random.randint(0, 300)
                self.rect.y = 375
            if self.game.check_collision(self, self.game.all_waves):
                print("monstre se prends la wave en pleine face")
                self.rect.x += 3
        else:
            # le deplacement se fait que si il n'y a pas de joueur
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.x += self.velocity
            # si le monstre est en colision avec le joueur
            else:
                # infliger des degats
                self.game.player.damage(self.attack)
            if self.rect.x >= 1500:
                self.rect.x = 1300 + random.randint(0, 300)
                self.rect.y = 375
                self.is_good = False


# definir une class pour le premier monstre
class Vampire(Monster):

    def __init__(self, game):
        super().__init__(game, "monster")

# definir une class pour le deuxieme monstre
class Oiseau(Monster):

    def __init__(self, game):
        super().__init__(game, "oiseau")
        self.rect.y = 250

    def forward(self):
        if not self.is_good:
            if self.game.check_collision(self, self.game.all_players):
                # infliger des degats
                self.game.player.damage(self.attack)
            else:
                self.rect.x -= self.velocity

            if self.rect.x <= - 250:
                self.rect.x = 1300 + random.randint(0, 300)
                self.rect.y = 200

        else:
            # le deplacement se fait que si il n'y a pas de joueur
            if not self.game.check_collision(self, self.game.all_players):
                self.rect.x += self.velocity
                print(">>>")
            # si le monstre est en colision avec le joueur
            else:
                # infliger des degats
                self.game.player.damage(self.attack)
            if self.rect.x >= 1500:
                self.rect.x = 1300 + random.randint(0, 300)
                self.rect.y = 200
                self.is_good = False

    def damage(self, amount):
        # infliger les degats
        self.health -= amount + 99

        # verifier si son nvx nombres de hp <= 0
        if self.health <= 0:
            self.rect.x = 1300 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health
            self.game.player.update_attack(1)
            # ajout du score
            self.game.score += 10