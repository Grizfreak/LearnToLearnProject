import pygame
import random

# definir une class qui va s'occuper des annimations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les chopse a faire a la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'./asset/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)

    # fonction pour animer le sprite
    def animate(self):
        self.current_image += random.randint(0,1)
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]

# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images
    images = []
    # recuperer le chemin du dossier
    path = f"./asset/{sprite_name}/{sprite_name}"
    # boucler sur chaque image
    for num in range(1, 20):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

# definir un dico contenant les images charger de chaque sprite
animations = {
    'monster': load_animation_images('monster'),
    'oiseau': load_animation_images('oiseau')
}