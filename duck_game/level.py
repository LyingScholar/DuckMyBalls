# duck_game/level.py

import pygame
from duck_game.game_platform import Platform
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_IMAGE
from duck_game.resource_manager import ResourceManager

class Level:
    def __init__(self, background_image, platform_data, ground_level):
        self.platforms = pygame.sprite.Group()
        if isinstance(background_image, pygame.Surface):
            self.background = background_image
        else:
            self.background = ResourceManager.load_image(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ground_level = ground_level
        self.create_platforms(platform_data)
        self.add_ground()
        self.ground_image = ResourceManager.load_image(GROUND_IMAGE)
        self.level_width = self.calculate_level_width()
        self.level_height = SCREEN_HEIGHT  # Assuming level height is screen height

    def create_platforms(self, platform_data):
        for plat in platform_data:
            platform = Platform(
                x=plat['x'],
                y=plat['y'],
                width=plat['width'],
                height=plat['height'],
                image=plat['image'],
                moving=plat.get('moving', False),
                move_range=plat.get('move_range', 0),
                speed=plat.get('speed', 0)
            )
            self.platforms.add(platform)

    def add_ground(self):
        ground_width = self.calculate_level_width()
        ground_height = SCREEN_HEIGHT - self.ground_level
        ground_image = pygame.Surface((int(ground_width), int(ground_height)), pygame.SRCALPHA)
        ground = Platform(
            x=0,
            y=self.ground_level,
            width=ground_width,
            height=ground_height,
            image=ground_image
        )
        self.platforms.add(ground)
        self.ground_platform = ground

    def calculate_level_width(self):
        if self.platforms:
            max_width = max(p.rect.right for p in self.platforms)
            return max_width
        else:
            return SCREEN_WIDTH

    def update(self):
        self.platforms.update()

    def draw(self, screen, camera_x):
        screen.blit(self.background, (0, 0))
        for platform in self.platforms:
            if platform is not self.ground_platform:
                screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))
        # Draw ground
        num_tiles = (self.level_width // self.ground_image.get_width()) + 1
        for i in range(num_tiles):
            ground_x = i * self.ground_image.get_width() - camera_x
            screen.blit(self.ground_image, (ground_x, self.ground_level))
