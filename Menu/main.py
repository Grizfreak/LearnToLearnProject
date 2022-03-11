import pygame
from Library_Interpreter.Dictionnary import Dictionnary
from Library_Interpreter.Interpreter import Interpreter
from Library_Interpreter.Shooter_Librairies.Gravity_Library import Gravity_Library
from Library_Interpreter.Shooter_Librairies.Summon_Library import Summon_Library
from platformer.Player import Player
from platformer.World_data import World_data
from platformer.gameConstants import gameConstants
from platformer.World import World
from platformer.P_InputBox import P_InputBox
from shooter.S_InputBox import S_InputBox
from shooter.game import Game

import os
x, y = 360, 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(x,y)
pygame.init()

pygame.display.set_caption("pts4_menu")
screen = pygame.display.set_mode((750, 650))
pygame.display.flip()


def main_menu():
    while True:
        screen = pygame.display.set_mode((750, 650))
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("monospace", 20, True)
        text = font.render("MENU", True, (255, 255, 255))
        screen.blit(text, (350, 100))
        # boutons
        button_shooter = pygame.image.load('./asset/bouton_shooter(pts4).png')
        button_plat = pygame.image.load('./asset/vouton_platformeur(pts4).png')
        button_shooter = pygame.transform.scale(button_shooter, (100, 100))
        button_plat = pygame.transform.scale(button_plat, (100, 100))
        button_shooter_rect = button_shooter.get_rect()
        button_plat_rect = button_plat.get_rect()
        button_shooter_rect.x = 150
        button_shooter_rect.y = 150
        button_plat_rect.x = 450
        button_plat_rect.y = 150
        screen.blit(button_shooter, button_shooter_rect)
        screen.blit(button_plat, button_plat_rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shooter_rect.collidepoint(event.pos):
                    print('click shooter')
                    shooter_game()
                if button_plat_rect.collidepoint(event.pos):
                    print('click platformer')
                    platformer_game()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("game quit")
        pygame.display.update()


def shooter_game():
    clock = pygame.time.Clock()
    clock_gravity = pygame.time.Clock()
    FPS = 90
    SLOW_MOTION = 10

    # generer la fenetre de notre jeu
    pygame.display.set_caption("pts4")
    screen = pygame.display.set_mode((1400, 650))

    # importer l'arriere plan du jeu
    background = pygame.image.load('../shooter/asset/back.png')

    # charger le jeu
    game = Game()

    # définir l'interpréteur de commandes
    dico = Dictionnary([Summon_Library(game), Gravity_Library(game)])
    interpreter = Interpreter(dico)
    input_box = S_InputBox(150, 0, 140, 32, interpreter)

    # définir les constantes de saut
    is_jumping = False
    jumping_time = 0

    running = True

    # boucle tant que running est true
    while running:
        screen.fill((0, 0, 0))
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
        elif game.pressed.get(pygame.K_z) and game.player.rect.y > 0 and game.player.gravity == False:
            game.player.move_up()
        elif game.pressed.get(pygame.K_s) and game.player.rect.y < 350 and game.player.gravity == False:
            game.player.move_down()

        # verifier le saut du joueur
        if game.pressed.get(pygame.K_SPACE) and not input_box.active:
            game.player.isJump = True

        game.player.jump()
        game.player.gravitycheck()
        # mettre a jour l'ecran
        pygame.display.flip()

        # si le joueur ferme la fenetre
        for event in pygame.event.get():
            # event de boîte de dialogue
            input_box.handle_event(event)
            # que l event est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
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
        # fixer le nombre de fps sur la clock
        pygame.display.update()
        clock.tick(FPS)


def platformer_game():
    gameconstants = gameConstants()
    player = Player(100, gameconstants.screen_height - 130, gameconstants)
    interpreter = Interpreter(player.dictionary)
    input_box = P_InputBox(400, 900, 140, 32, gameconstants, interpreter)
    world = World(World_data().world_data_arr[1], gameconstants)
    #gameconstants.actualLevel

    run = True
    while run:

        gameconstants.clock.tick(gameconstants.fps)
        gameconstants.screen.blit(gameconstants.bg_img, (0, 0))
        gameconstants.screen.blit(gameconstants.sun_img, (100, 100))
        world.draw()
        input_box.draw(gameconstants.screen)
        world.exit.draw(gameconstants.screen)
        if not input_box.active:
            player.update(world)
        else:
            player.draw()

        if player.hasFinished:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.K_ESCAPE:
                run = False
            input_box.handle_event(event)

        input_box.update()
        pygame.display.update()


main_menu()
