# level.py

import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, moving=False, move_range=0, speed=0):
        super().__init__()
        img = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(img, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.moving = moving
        self.move_range = move_range
        self.speed = speed
        self.initial_x = x
        self.direction = 1

    def update(self):
        if self.moving:
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.initial_x) >= self.move_range:
                self.direction *= -1

class Level:
    def __init__(self, background_image, platform_data, ground_level):
        bg = pygame.image.load(background_image).convert()
        self.background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.platforms = pygame.sprite.Group()
        for data in platform_data:
            self.platforms.add(Platform(**data))
        self.ground_level = ground_level
        self.add_ground()
        self.level_width = max(p.rect.right for p in self.platforms)

    def add_ground(self):
        # Add ground platform across the level width
        ground = Platform(
            x=0,
            y=self.ground_level,
            width=self.level_width,
            height=SCREEN_HEIGHT - self.ground_level,
            image=GROUND_IMAGE
        )
        self.platforms.add(ground)

    def update(self):
        self.platforms.update()

    def draw(self, screen, camera_x):
        screen.blit(self.background, (0, 0))
        for platform in self.platforms:
            screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))
