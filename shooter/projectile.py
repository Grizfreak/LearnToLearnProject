import pygame

# definir la class qui va gerer les projectile
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('../../AndroidStudioProjects/ClickerGame/LearnToLearnProject/shooter/asset/bulet.png')
        # self.image = pygame.transform.scale(self.image, (50, 50)) changer la taille de l'image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 95
        self.rect.y = player.rect.y + 77

    def remove(self):
        self.player.all_projectiles.remove(self)
        print("suppression du projectile courant")

    def move(self):
        self.rect.x += self.velocity

        # verifier si le projectile rentre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()

        #verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > 1405:
            # supprime le projectile
            self.remove()
