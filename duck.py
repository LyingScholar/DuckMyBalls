# duck.py
import pygame
from settings import *

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_image = pygame.image.load(DUCK_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vx = 0
        self.vy = 0
        self.speed = 5
        self.acceleration = 0.5
        self.max_speed = 5
        self.on_ground = False
        self.moving_left = False
        self.moving_right = False
        self.jump_pressed = False
        self.can_jump = True

    def move_left(self):
        self.moving_left = True

    def move_right(self):
        self.moving_right = True

    def stop_moving_left(self):
        self.moving_left = False

    def stop_moving_right(self):
        self.moving_right = False

    def stop(self):
        self.vx = 0

    def jump(self):
        if self.on_ground:
            self.vy = -JUMP_FORCE

    def update(self, platforms):
        # Apply gravity
        self.vy += GRAVITY

        # Handle horizontal movement with acceleration and damping
        if self.moving_left:
            self.vx -= self.acceleration
            if self.vx < -self.max_speed:
                self.vx = -self.max_speed
        elif self.moving_right:
            self.vx += self.acceleration
            if self.vx > self.max_speed:
                self.vx = self.max_speed
        else:
            # Apply damping
            self.vx *= 0.8
            if abs(self.vx) < 0.1:
                self.vx = 0

        # Update position
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Collision handling
        self.rect.x += self.vx
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vx > 0:
                    self.rect.right = platform.rect.left
                elif self.vx < 0:
                    self.rect.left = platform.rect.right
                self.vx = 0

        # Vertical movement
        self.rect.y += self.vy
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vy > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                elif self.vy < 0:
                    self.rect.top = platform.rect.bottom
                self.vy = 0

        # Invisible ground at y = 550
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            self.vy = 0
            self.on_ground = True

        # Handle jumping
        if self.jump_pressed and self.can_jump and self.on_ground:
            self.vy = -JUMP_FORCE
            self.can_jump = False  # Prevents continuous jumping
        if not self.jump_pressed:
            self.can_jump = True  # Allows jumping again when button is released

    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
