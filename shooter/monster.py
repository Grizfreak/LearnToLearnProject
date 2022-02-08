import pygame


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 3
        self.image = pygame.image.load('./asset/monter(pts4).png')
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 375

    def forward(self):
        # le deplacement se fait que si il n'y a pas de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity