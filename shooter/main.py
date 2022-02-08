import pygame
from game import Game
pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("pts4")
screen = pygame.display.set_mode((1400, 650))

# importer l'arriere plan du jeu
background = pygame.image.load('../../AndroidStudioProjects/ClickerGame/LearnToLearnProject/shooter/asset/back.png')

# charger le jeu
game = Game()


running = True

# boucle tant que running est true
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, 0))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectile du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les monstre du jeu
    for monster in game.all_monsters:
        monster.forward()

    # appliquer l'ensemble des images du groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images du groupe de monstre
    game.all_monsters.draw(screen)

    # verifier si le joueur veut aller a gauche ou droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x < screen.get_width() - 100:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > -15:
        game.player.move_left()

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que l event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game quit")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # detecter si le click est presser
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                game.player.launch_projectile()