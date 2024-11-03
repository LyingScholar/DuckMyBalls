# duck.py
import pygame
from settings import DUCK_IMAGE, GRAVITY, JUMP_FORCE

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_image = pygame.image.load(DUCK_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(original_image, (50, 50))  # Adjust size as needed
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.jump_pressed = False

    def update(self, platforms):
        # Apply gravity
        self.vy += GRAVITY
        # Apply horizontal movement
        self.rect.x += self.vx
        self.collide(platforms, 'x')
        # Apply vertical movement
        self.rect.y += self.vy
        self.on_ground = False
        self.collide(platforms, 'y')
        if self.jump_pressed and self.can_jump and self.on_ground:
            self.vy = -JUMP_FORCE
            self.can_jump = False
        if not self.jump_pressed:
            self.can_jump = True

    def collide(self, platforms, direction):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if direction == 'x':
                    if self.vx > 0:
                        self.rect.right = platform.rect.left
                    elif self.vx < 0:
                        self.rect.left = platform.rect.right
                    self.vx = 0
                elif direction == 'y':
                    if self.vy > 0:
                        self.rect.bottom = platform.rect.top
                        self.on_ground = True
                    elif self.vy < 0:
                        self.rect.top = platform.rect.bottom
                    self.vy = 0

    def move_left(self):
        self.vx = -5

    def move_right(self):
        self.vx = 5

    def stop(self):
        self.vx = 0

    def jump(self):
        if self.on_ground:
            self.vy = -JUMP_FORCE

    def draw(self, screen, camera_x):
        # Adjust position based on camera
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
