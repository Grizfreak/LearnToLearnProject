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
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game quit")