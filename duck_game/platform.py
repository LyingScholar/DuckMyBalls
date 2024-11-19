
# platform.py
import pygame



class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, moving=False, move_range=0, speed=0):
        super().__init__()
        if isinstance(image, pygame.Surface):
            self.image = image  # Use the provided Surface directly
        else:
            img = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(img, (int(width), int(height)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.moving = moving
        self.move_range = move_range
        self.speed = speed
        self.direction = 1  # 1 for right/down, -1 for left/up
        self.start_pos = x if moving else None

    def update(self):
        if self.moving:
            # Update the platform's position
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.start_pos) >= self.move_range:
                self.direction *= -1
