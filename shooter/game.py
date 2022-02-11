import pygame
from player import Player
from monster import Monster
from thunder import Thunder
from nuage import Nuage

# classe du jeu
class Game:

    def __init__(self):
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()
        self.all_thunder = pygame.sprite.Group()
        self.all_nuages = pygame.sprite.Group()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def spawn_nuage(self):
        print("PLUIE D'ECLAIRE!")
        self.all_nuages.add(Nuage(self))

    def spawn_thunder(self):
        i = 0
        for i in range(20):
            self.all_thunder.add(Thunder(self))


