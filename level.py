# level.py
import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=20, image=OBSTACLE_IMAGE, moving=False, move_range=0, speed=0):
        super().__init__()
        original_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(original_image, (width, height))
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
                self.direction *= -1  # Change direction

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, image=GROUND_IMAGE):
        super().__init__()
        original_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(original_image, (width, SCREEN_HEIGHT - y))
        self.rect = self.image.get_rect(topleft=(x, y))

class Level:
    def __init__(self, background_image, platforms):
        original_bg = pygame.image.load(background_image).convert()
        self.background = pygame.transform.scale(original_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.platforms = pygame.sprite.Group()
        for plat in platforms:
            if len(plat) == 8:
                x, y, width, height, image, moving, move_range, speed = plat
                self.platforms.add(Platform(x, y, width, height, image, moving, move_range, speed))
            else:
                x, y, width, height = plat
                self.platforms.add(Platform(x, y, width, height))
        self.ground = pygame.sprite.Group()
        self.level_width = 0

    def update(self, duck):
        # Update platforms if needed
        for platform in self.platforms:
            platform.update()

    def draw(self, screen, camera_x):
        # Draw background
        screen.blit(self.background, (0, 0))
        # Draw ground
        for ground_piece in self.ground:
            screen.blit(ground_piece.image, (ground_piece.rect.x - camera_x, ground_piece.rect.y))
        # Draw platforms
        for platform in self.platforms:
            screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))

class FlowerField(Level):
    def __init__(self):

            # (x, y, width, height, image, moving, move_range, speed)
        platforms = [
            # Starting area
            (200, 450, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (400, 400, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (600, 350, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # First moving platform over a gap
            (800, 300, 100, 20, OBSTACLE_IMAGE, True, 200, 2),
            # Ascending platforms
            (1100, 250, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (1300, 200, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Small platforms requiring precise jumps
            (1500, 250, 50, 20, OBSTACLE_IMAGE, False, 0, 0),
            (1600, 300, 50, 20, OBSTACLE_IMAGE, False, 0, 0),
            (1700, 350, 50, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Descending platforms
            (1900, 400, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (2100, 450, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Overhead platform with spikes underneath
            (2300, 400, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (2300, 550, 100, 50, SPIKE_IMAGE, False, 0, 0),
            # Moving platform over spikes
            (2500, 350, 100, 20, OBSTACLE_IMAGE, True, 300, 2),
            (2500, 550, 100, 50, SPIKE_IMAGE, False, 0, 0),
            # High platforms requiring a high jump
            (2900, 300, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (3100, 250, 100, 20, OBSTACLE_IMAGE, False, 0, 0),


            # Gap with collectible item
            # (3300, 200, 30, 30, COLLECTIBLE_IMAGE, False, 0, 0),
            
            
            # descending platforms
            (3500, 250, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (3700, 300, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (3900, 350, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Long stretch with enemies (if implemented)



            (4200, 400, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (4400, 450, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (4600, 500, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
        ]


        x = 4800
        while x < 7000:
            platforms.append((x, 550 - (x % 400), 100, 20, OBSTACLE_IMAGE, False, 0, 0))
            x += 200

        super().__init__(BACKGROUND_FLOWER_FIELD, platforms)
        # Create looping ground
        ground_length = 7000  # Adjusted for longer level
        for x in range(0, ground_length, 800):
            ground_piece = Ground(x, 550, 800)
            self.ground.add(ground_piece)
        self.level_width = ground_length

class CitySewer(Level):
    def __init__(self):
        platforms = [
            # Starting area
            (200, 450, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Slippery platforms (if you implement slippery mechanics)
            (400, 400, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Platforms over toxic water (hazard)
            (600, 350, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (800, 350, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Moving platform to higher level
            (1000, 300, 100, 20, OBSTACLE_IMAGE, True, 150, 2),
            # Vertical shafts
            (1200, 250, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (1200, 450, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            # Hazardous areas
            (1400, 500, 100, 20, OBSTACLE_IMAGE, False, 0, 0),
            (1400, 550, 100, 50, SPIKE_IMAGE, False, 0, 0),
            # Extend up to x = 10000
            # ...
        ]

        # Extend the level
        x = 1600
        while x < 10000:
            platforms.append((x, 550 - (x % 500), 100, 20, OBSTACLE_IMAGE, False, 0, 0))
            x += 250

        super().__init__(BACKGROUND_CITY_SEWER, platforms)
        # Create looping ground
        ground_length = 10000
        for x in range(0, ground_length, 800):
            ground_piece = Ground(x, 550, 800)
            self.ground.add(ground_piece)
        self.level_width = ground_length

class PollutedRiver(Level):
    def __init__(self):
        platforms = [
            (200, 500, 100, 20),
            (500, 450, 100, 20),
            (800, 400, 100, 20),
            (1100, 350, 100, 20),
            (1400, 300, 100, 20),
            (1700, 250, 100, 20),
        ]
        super().__init__(BACKGROUND_POLLUTED_RIVER, platforms)
        # Create looping ground
        ground_length = 1000
        for x in range(0, ground_length, 800):
            ground_piece = Ground(x, 550, 800)
            self.ground.add(ground_piece)
        self.level_width = ground_length
