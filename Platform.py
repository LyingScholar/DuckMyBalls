import pygame
from settings import OBSTACLE_IMAGE

# level.py (add to Platform class)
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=100, image=OBSTACLE_IMAGE, moving=False, move_range=0, speed=0):
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
