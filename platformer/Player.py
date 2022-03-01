import pygame
from gameConstants import *
from platformer.GravityState import GravityState
from Library_Interpreter.Platformer_Librairies.Gravity_Library import Gravity_Library
from Library_Interpreter.Dictionnary import Dictionnary

world_data2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Player:
    def __init__(self, x, y, gameConstants):
        self.images_right = []
        self.images_left = []
        self.images_right_BOTTOM = []
        self.images_left_BOTTOM = []
        self.images_right_TOP = []
        self.images_left_TOP = []
        self.images_right_LEFT = []
        self.images_left_LEFT = []
        self.images_right_RIGHT = []
        self.images_left_RIGHT = []
        self.index = 0
        self.counter = 0
        self.gameConstants = gameConstants
        self.dictionary = Dictionnary([Gravity_Library(self)])
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_right_BOTTOM.append(img_right)
            self.images_left.append(img_left)
            self.images_left_BOTTOM.append(img_left)
            self.images_right_TOP.append(pygame.transform.flip(img_right,False,True))
            self.images_left_TOP.append(pygame.transform.flip(img_left,False,True))
            self.images_left_LEFT.append(pygame.transform.rotate(img_left,270))
            self.images_right_LEFT.append(pygame.transform.rotate(img_right,270))
            self.images_left_RIGHT.append(pygame.transform.rotate(img_left,90))
            self.images_right_RIGHT.append(pygame.transform.rotate(img_right,90))
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.vel_x = 0
        self.jumped = False
        self.direction = 0

    def update(self, world):
        dx = 0
        dy = 0
        walk_cooldown = 5

        # get keypresses
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.gameConstants.gravity = GravityState.LEFT
        if key[pygame.K_RIGHT]:
            self.gameConstants.gravity = GravityState.RIGHT
        if key[pygame.K_UP]:
            self.gameConstants.gravity = GravityState.TOP
        if key[pygame.K_DOWN]:
            self.gameConstants.gravity = GravityState.BOTTOM

        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            self.vel_y = -15
            # state gravity case TODO
            self.vel_x = -15
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_q]:
            # print('entered')
            # TODO change for all gravities
            if self.gameConstants.gravity == GravityState.BOTTOM:
                dx -= 5
            elif self.gameConstants.gravity == GravityState.TOP:
                dx -= 5
            elif self.gameConstants.gravity == GravityState.LEFT:
                print('entered')
                print(dy)
                dy -= 5
                print(dy)
            elif self.gameConstants.gravity == GravityState.RIGHT:
                dy += 5
            self.counter += 1
            self.direction = -1

        if key[pygame.K_d]:
            # TODO change for all gravities
            if self.gameConstants.gravity == GravityState.BOTTOM:
                dx += 5
            elif self.gameConstants.gravity == GravityState.TOP:
                dx += 5
            elif self.gameConstants.gravity == GravityState.LEFT:
                dy += 5
            elif self.gameConstants.gravity == GravityState.RIGHT:
                dy -= 5
            self.counter += 1
            self.direction = 1

        if key[pygame.K_q] == False and key[pygame.K_d] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        if self.gameConstants.gravity == GravityState.BOTTOM:
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y
        elif self.gameConstants.gravity == GravityState.LEFT:
            self.vel_x += 1
            if self.vel_x > 10:
                self.vel_x = 10
            dx -= self.vel_x
        elif self.gameConstants.gravity == GravityState.TOP:
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy -= self.vel_y
        elif self.gameConstants.gravity == GravityState.RIGHT:
            self.vel_x += 1
            if self.vel_x > 10:
                self.vel_x = 10
            dx += self.vel_x

        # check for collision
        self.in_air = True
        for tile in world.tile_list:
            if self.gameConstants.gravity == GravityState.BOTTOM:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                        self.vel_x = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.vel_x = 0
                        self.in_air = False

            elif self.gameConstants.gravity == GravityState.TOP:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y >= 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                        self.vel_x = 0
                        self.in_air = False
                    # check if above the ground i.e. falling
                    elif self.vel_y < 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.vel_x = 0


            elif self.gameConstants.gravity == GravityState.LEFT:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_x < 0:
                        dx = tile[1].left - self.rect.right
                        self.vel_y = 0
                        self.vel_x = 0
                    # check if above the ground i.e. falling
                    elif self.vel_x >= 0:
                        dx = tile[1].right - self.rect.left
                        self.vel_y = 0
                        self.vel_x = 0
                        self.in_air = False

                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    dy = 0
            elif self.gameConstants.gravity == GravityState.RIGHT:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_x >= 0:
                        dx = tile[1].left - self.rect.right
                        self.vel_y = 0
                        self.vel_x = 0
                        self.in_air = False
                    # check if above the ground i.e. falling
                    elif self.vel_x < 0:
                        dx = tile[1].right - self.rect.left
                        self.vel_y = 0
                        self.vel_x = 0

                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    dy = 0

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > self.gameConstants.screen_height:
            self.rect.bottom = self.gameConstants.screen_height
            dy = 0

        # draw player onto screen
        self.draw()

        # check for collision with exit
        if pygame.sprite.spritecollide(self, world.exit, False):
            print('célafin')
            world.set_data(world_data2)
            return
            #TODO finish a level

    def draw(self):
        self.gameConstants.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.gameConstants.screen, (255, 255, 255), self.rect, 2)

    def changeSprite(self):
        if self.gameConstants.gravity == GravityState.BOTTOM:
            self.images_left = self.images_left_BOTTOM
            self.images_right = self.images_right_BOTTOM
        elif self.gameConstants.gravity == GravityState.TOP:
            self.images_left = self.images_left_TOP
            self.images_right = self.images_right_TOP
        elif self.gameConstants.gravity == GravityState.LEFT:
            self.images_left = self.images_left_LEFT
            self.images_right = self.images_right_LEFT
        elif self.gameConstants.gravity == GravityState.RIGHT:
            self.images_left = self.images_left_RIGHT
            self.images_right = self.images_right_RIGHT
