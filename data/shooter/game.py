import pygame
from data.shooter.player import Player
from data.shooter.monster import Vampire, Oiseau
from data.shooter.thunder import Thunder
from data.shooter.nuage import Nuage
from data.shooter.wave import Wave


# classe du jeu
class Game:

    def __init__(self):
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster(Vampire)
        self.spawn_monster(Vampire)
        self.spawn_monster(Oiseau)
        self.all_thunder = pygame.sprite.Group()
        self.all_nuages = pygame.sprite.Group()
        self.all_waves = pygame.sprite.Group()
        # mettre le score a 0
        self.score = 0


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def spawn_nuage(self):
        print("PLUIE D'ECLAIRE!")
        self.all_nuages.add(Nuage(self))

    def spawn_wave(self):
        print("VAGUE EN APPROCHE")
        self.all_waves.add(Wave(self))

    def spawn_thunder(self):
        i = 0
        for i in range(20):
            self.all_thunder.add(Thunder(self))


