# duck_game/duck.py

import pygame
from duck_game.resource_manager import ResourceManager
from duck_game.settings import *

class Duck(pygame.sprite.Sprite):
    """Represents the player character (duck) in the game."""

    def __init__(self, x, y):
        """Initialize the duck sprite.

        Args:
            x (int): The x-coordinate of the duck's starting position.
            y (int): The y-coordinate of the duck's starting position.
        """
        super().__init__()
        self.image = ResourceManager.load_image(DUCK_IMAGE, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        print("Duck mask count:", self.mask.count())
        
        self.vx = 0
        self.vy = 0
        self.speed = 5
        self.on_ground = False

    def update(self, platforms, level_width = None):
        """Update the duck's position and handle collisions.

        Args:
            platforms (pygame.sprite.Group): The group of platform sprites.
        """
        self.apply_gravity()
        self.move_horizontal()
        self.handle_collisions(platforms, 'horizontal')
        self.move_vertical()
        self.handle_collisions(platforms, 'vertical')
        if level_width is not None:
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > level_width - self.rect.width:
                self.rect.x = level_width - self.rect.width

    def apply_gravity(self):
        """Apply gravity to the duck's vertical velocity."""
        self.vy += GRAVITY
        if self.vy > 20:  # Terminal velocity
            self.vy = 20

    def move_horizontal(self):
        """Move the duck horizontally based on velocity."""
        self.rect.x += self.vx

    def move_vertical(self):
        """Move the duck vertically based on velocity."""
        self.rect.y += self.vy

    def handle_collisions(self, platforms, direction):
        """Handle collisions with platforms.

        Args:
            platforms (pygame.sprite.Group): The group of platform sprites.
            direction (str): The direction of movement ('horizontal' or 'vertical').
        """
        # rect_collisions = pygame.sprite.spritecollide(self, platforms, False)
        # collisions = pygame.sprite.spritecollide(self, platforms, False, pygame.sprite.collide_mask)
        collisions = pygame.sprite.spritecollide(self, platforms, False, pygame.sprite.collide_mask)
        if collisions:
            print(f"Collision detected in {direction} direction with {len(collisions)} platform(s)")
        else:
            print(f"No collision detected in {direction} direction")
        for platform in collisions:
            if direction == 'horizontal':
                if self.vx > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif self.vx < 0:  # Moving left
                    self.rect.left = platform.rect.right
                self.vx = 0
            elif direction == 'vertical':
                if self.vy > 0:  # Falling down
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                elif self.vy < 0:  # Moving up
                    self.rect.top = platform.rect.bottom
                self.vy = 0

    def move(self, direction):
        """Set the horizontal velocity based on input direction.

        Args:
            direction (int): -1 for left, 1 for right.
        """
        self.vx = direction * self.speed

    def stop(self):
        """Stop the duck's horizontal movement."""
        self.vx = 0

    def jump(self):
        """Make the duck jump if it's on the ground."""
        if self.on_ground:
            self.vy = -JUMP_FORCE
            self.on_ground = False

    def draw(self, screen, camera_x):
        """Draw the duck on the screen, adjusted for camera offset.

        Args:
            screen (pygame.Surface): The game screen.
            camera_x (int): The horizontal camera offset.
        """
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))

    def update_image(self, new_image):
        self.image = new_image
        self.mask = pygame.mask.from_surface(self.image)