import pygame


pygame.init()

pygame.display.set_caption("pts4_menu")
screen = pygame.display.set_mode((750, 650))
pygame.display.flip()
running = True

while running:

    font = pygame.font.SysFont("monospace", 20, True)
    text = font.render("MENU", True, (255, 255, 255))
    screen.blit(text, (350, 100))
    # boutons
    button_shooter = pygame.image.load('./asset/bouton_shooter(pts4).png')
    button_plat = pygame.image.load('./asset/vouton_platformeur(pts4).png')
    button_shooter = pygame.transform.scale(button_shooter,(100, 100))
    button_plat = pygame.transform.scale(button_plat,(100, 100))
    button_shooter_rect = button_shooter.get_rect()
    button_plat_rect = button_plat.get_rect()
    button_shooter_rect.x = 150
    button_shooter_rect.y = 150
    button_plat_rect.x = 450
    button_plat_rect.y = 150
    screen.blit(button_shooter,button_shooter_rect)
    screen.blit(button_plat,button_plat_rect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_shooter_rect.collidepoint(event.pos):
                print('click')
            if button_plat_rect.collidepoint(event.pos):
                print('click')
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game quit")