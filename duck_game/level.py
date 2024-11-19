# level.py

import pygame
# from platform import Platform
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_IMAGE

class Level:
    def __init__(self, background_image, platform_data, ground_level):
        self.platforms = pygame.sprite.Group()
        self.background = pygame.transform.scale(
            pygame.image.load(background_image).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.ground_level = ground_level
        self.create_platforms(platform_data)
        self.add_ground()  # Add invisible ground platform

        # Load the ground image
        self.ground_image = pygame.image.load(GROUND_IMAGE).convert_alpha()
        # Scale the ground image if necessary
        desired_ground_height = 100  # Adjust as needed
        ground_image_width = self.ground_image.get_width()
        self.ground_image = pygame.transform.scale(
            self.ground_image, (ground_image_width, desired_ground_height)
        )

        # Calculate the level width based on the platforms
        self.level_width = self.calculate_level_width()

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
        # Create invisible ground platform for collision
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
        # Determine the width of the level based on the farthest right platform
        max_width = max(p.rect.right for p in self.platforms)
        return max_width

    def update(self):
        self.platforms.update()

    def draw(self, screen, camera_x):
        # Draw background
        screen.blit(self.background, (0, 0))

        # Draw ground image looping across the level
        ground_y = self.ground_level  # Align with ground level
        ground_image_width = self.ground_image.get_width()
        num_tiles = (self.level_width // ground_image_width) + 2  # +2 to cover screen edges

        for i in range(num_tiles):
            ground_x = i * ground_image_width - camera_x
            screen.blit(self.ground_image, (ground_x, ground_y))

        # Draw platforms
        for platform in self.platforms:
            if platform is not self.ground_platform:
                screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))


