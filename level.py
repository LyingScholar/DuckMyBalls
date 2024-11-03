# level.py
import pygame
from settings import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=20, image=OBSTACLE_IMAGE, moving=False, move_range=0, speed=0):
        super().__init__()
        original_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)  # Create a mask from the image's alpha channel
        self.moving = moving
        self.move_range = move_range
        self.speed = speed
        self.initial_x = x
        self.direction = 1

    def update(self):
        if self.moving:
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.initial_x) >= self.move_range:
                self.direction *= -1  # Change direction


class Level:
    def __init__(self, background_image, platforms):
        original_bg = pygame.image.load(background_image).convert()
        self.background = pygame.transform.scale(original_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.platforms = pygame.sprite.Group()
        for plat in platforms:
            self.platforms.add(Platform(**plat))
        self.level_width = max(platform.rect.right for platform in self.platforms)

    def update(self, duck):
        # Update platforms if needed
        for platform in self.platforms:
            platform.update()

    def draw(self, screen, camera_x):
        # Draw background
        screen.blit(self.background, (0, 0))
        # # Draw ground
        # for ground_piece in self.ground:
        #     screen.blit(ground_piece.image, (ground_piece.rect.x - camera_x, ground_piece.rect.y))
        # Draw platforms
        for platform in self.platforms:
            screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))

class FlowerField(Level):
    def __init__(self):
        platforms = [
            # Starting area
            {'x': 200, 'y': 450, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 400, 'y': 400, 'width': 300, 'height': 100, 'image': OBSTACLE_IMAGE_2, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 600, 'y': 350, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # First moving platform over a gap
            {'x': 800, 'y': 300, 'width': 300, 'height': 100, 'image': OBSTACLE_IMAGE_2, 'moving': True, 'move_range': 200, 'speed': 2},
            # Ascending platforms
            {'x': 1100, 'y': 250, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 1300, 'y': 200, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # Small platforms requiring precise jumps
            {'x': 1500, 'y': 250, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 1600, 'y': 300, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 1700, 'y': 350, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # Descending platforms
            {'x': 1800, 'y': 400, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 1900, 'y': 450, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 2000, 'y': 500, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 2300, 'y': 400, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 2500, 'y': 350, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': True, 'move_range': 300, 'speed': 2},
            # High platforms requiring a high jump
            {'x': 2900, 'y': 300, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 3100, 'y': 250, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # Descending platforms
            {'x': 3500, 'y': 250, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 3700, 'y': 300, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 3900, 'y': 350, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # More platforms...
            {'x': 4200, 'y': 400, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 4400, 'y': 450, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 4600, 'y': 500, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
        ]

        # Append additional platforms using dictionaries
        x = 4800
        while x < 7000:
            platforms.append({
                'x': x,
                'y': 550 - (x % 400),
                'width': 100,
                'height': 100,
                'image': OBSTACLE_IMAGE,
                'moving': False,
                'move_range': 0,
                'speed': 0
            })
            x += 200

        super().__init__(BACKGROUND_FLOWER_FIELD, platforms)

        # Calculate level width dynamically
        self.level_width = max(plat['x'] + plat.get('width', 100) for plat in platforms)

class CitySewer(Level):
    def __init__(self):
        platforms = [
            # Starting area
            {'x': 200, 'y': 450, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # Slippery platforms (if you implement slippery mechanics)
            {'x': 400, 'y': 400, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # Platforms over toxic water (hazard???)
            {'x': 600, 'y': 350, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 800, 'y': 350, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            # Moving platform to higher level
            {'x': 1000, 'y': 300, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': True, 'move_range': 150, 'speed': 2},
            # Vertical shafts
            {'x': 1200, 'y': 250, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 1200, 'y': 450, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
            {'x': 1400, 'y': 500, 'width': 100, 'height': 100, 'image': OBSTACLE_IMAGE, 'moving': False, 'move_range': 0, 'speed': 0},
        ]

        # Extend the level
        x = 1600
        while x < 10000:
            platforms.append({
                'x': x,
                'y': 550 - (x % 500),
                'width': 100,
                'height': 100,
                'image': OBSTACLE_IMAGE,
                'moving': False,
                'move_range': 0,
                'speed': 0
            })
            x += 250

        super().__init__(BACKGROUND_CITY_SEWER, platforms)
        self.level_width = 10000


class PollutedRiver(Level):
    def __init__(self):
        platforms = [
            {'x': 200, 'y': 500, 'width': 100, 'height': 20},
            {'x': 500, 'y': 450, 'width': 100, 'height': 20},
            {'x': 800, 'y': 400, 'width': 100, 'height': 20},
            {'x': 1100, 'y': 350, 'width': 100, 'height': 20},
            {'x': 1400, 'y': 300, 'width': 100, 'height': 20},
            {'x': 1700, 'y': 250, 'width': 100, 'height': 20},
            {'x': 2200, 'y': 500, 'width': 100, 'height': 20},
            {'x': 2500, 'y': 450, 'width': 100, 'height': 20},
            {'x': 2800, 'y': 400, 'width': 100, 'height': 20},
            {'x': 3100, 'y': 350, 'width': 100, 'height': 20},
            {'x': 3400, 'y': 300, 'width': 100, 'height': 20},
            {'x': 3700, 'y': 250, 'width': 100, 'height': 20},
        ]

        super().__init__(BACKGROUND_POLLUTED_RIVER, platforms)
        self.level_width = 4000
