import pygame
from game import Game
from Library_Interpreter.Dictionnary import Dictionnary
from Library_Interpreter.Interpreter import Interpreter
from Library_Interpreter.Summon_Library import Summon_Library
from shooter.InputBox import InputBox

pygame.init()

# definir une clock
clock = pygame.time.Clock()
clock_gravity = pygame.time.Clock()
FPS = 90
SLOW_MOTION = 10

#définir l'interpréteur de commandes
dico = Dictionnary([Summon_Library()])
interpreter = Interpreter(dico)
input_box = InputBox(150, 0, 140, 32, interpreter)

# generer la fenetre de notre jeu
pygame.display.set_caption("pts4")
screen = pygame.display.set_mode((1400, 650))

# importer l'arriere plan du jeu
background = pygame.image.load('./asset/back.png')

# charger le jeu
game = Game()

#définir les constantes de saut
is_jumping = False
jumping_time = 0

running = True

# boucle tant que running est true
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, 0))
    input_box.draw(screen)
    input_box.update()
    if input_box.active:
        clock.tick(SLOW_MOTION)

    # afficher le score
    font = pygame.font.SysFont("monospace", 16)
    score_text = font.render(f"Score : {game.score}", 1, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # actualiser la bar de vie du joueur
    game.player.update_health_bar(screen)

    # recuperer les projectile du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les monstre du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # appliquer l'ensemble des images du groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images du groupe de monstre
    game.all_monsters.draw(screen)

    # appliquer l'ensemble des nuages
    game.all_nuages.draw(screen)

    for nuage in game.all_nuages:
        nuage.spawn()

    # appliquer l'ensemble des eclaires
    game.all_thunder.draw(screen)

    for thunder in game.all_thunder:
        thunder.fall()

    # appliquer l'ensemble de la wave
    game.all_waves.draw(screen)

    for wave in game.all_waves:
        wave.spawn()

    # verifier si le joueur veut aller a gauche ou droite
    if game.pressed.get(pygame.K_d) and game.player.rect.x < screen.get_width() - 100 and not input_box.active:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > -15 and not input_box.active:
        game.player.move_left()
    elif game.pressed.get(pygame.K_z) and game.player.rect.y > 0 and game.player.gravity==False:
        game.player.move_up()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y < 350 and game.player.gravity==False:
        game.player.move_down()

    #verifier le saut du joueur
    if game.pressed.get(pygame.K_SPACE) and not input_box.active:
        game.player.isJump = True

    game.player.jump()
    game.player.gravitycheck()
    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        #event de boîte de dialogue
        input_box.handle_event(event)
        # que l event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game quit")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_e:
                game.spawn_nuage()

            if event.key == pygame.K_f:
                game.spawn_wave()

            if event.key == pygame.K_a:
                game.player.del_gravity()

            if event.key == pygame.K_p:
                print("inversement de la direction des monstres")
                for monster in game.all_monsters:
                    monster.is_good = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # detecter si le click est presser
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                game.player.launch_projectile()
    # fixer le nombre de fps sur la clock
    clock.tick(FPS)