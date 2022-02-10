import pygame
from player import Player
from monster import Monster
from thunder import Thunder

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

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def spawn_thunder(self):
        print("PLUIE D'ECLAIRE!")
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
        self.all_thunder.add(Thunder(self))
