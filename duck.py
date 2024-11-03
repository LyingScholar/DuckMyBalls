# duck.py

import pygame
from settings import *

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image = pygame.image.load(DUCK_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vx = 0
        self.vy = 0
        self.speed = 5
        self.on_ground = False
        self.jump_pressed = False

    def update(self, platforms):
        self.apply_gravity()
        self.move_horizontal()
        self.handle_collisions(platforms, 'horizontal')
        self.move_vertical()
        self.handle_collisions(platforms, 'vertical')

    def apply_gravity(self):
        self.vy += GRAVITY
        if self.vy > 20:  # Terminal velocity
            self.vy = 20

    def move_horizontal(self):
        self.rect.x += self.vx

    def move_vertical(self):
        self.rect.y += self.vy

    def handle_collisions(self, platforms, direction):
        collisions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collisions:
            if direction == 'horizontal':
                if self.vx > 0:
                    self.rect.right = platform.rect.left
                elif self.vx < 0:
                    self.rect.left = platform.rect.right
                self.vx = 0
            elif direction == 'vertical':
                if self.vy > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.vy = 0
                elif self.vy < 0:
                    self.rect.top = platform.rect.bottom
                    self.vy = 0

    def move(self, direction):
        self.vx = direction * self.speed

    def stop(self):
        self.vx = 0

    def jump(self):
        if self.on_ground:
            self.vy = -JUMP_FORCE
            self.on_ground = False

    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
