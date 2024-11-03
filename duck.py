import pygame
from settings import DUCK_IMAGE, GRAVITY, JUMP_FORCE

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_image = pygame.image.load(DUCK_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(original_image, (70, 70))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.vx = 0
        self.vy = 0
        self.on_ground = False
        self.jump_pressed = False
        self.can_jump = True

    def update(self, platforms):
        # Apply gravity
        if not self.on_ground:
            self.vy += GRAVITY


        # Apply horizontal movement
        self.rect.x += self.vx
        self.collide(platforms, 'x')


        # Apply vertical movement
        self.rect.y += self.vy
        self.on_ground = False
        self.collide(platforms, 'y')
        
        # Handle jumping mechanics
        if self.jump_pressed and self.can_jump and self.on_ground:
            self.vy = -JUMP_FORCE
            self.can_jump = False
        if not self.jump_pressed:
            self.can_jump = True

    def collide(self, platforms, direction):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                # Calculate the offset for mask collision checking
                offset_x = platform.rect.x - self.rect.x
                offset_y = platform.rect.y - self.rect.y

                # Check pixel-perfect collision using masks
                if self.mask.overlap(platform.mask, (offset_x, offset_y)):
                    if direction == 'x':
                        if self.vx > 0:  # Moving right
                            self.rect.right = platform.rect.left
                        elif self.vx < 0:  # Moving left
                            self.rect.left = platform.rect.right
                        self.vx = 0
                    elif direction == 'y':
                        if self.vy > 0:  # Falling down
                            self.rect.bottom = platform.rect.top
                            self.on_ground = True
                            self.vy = 0
                        elif self.vy < 0:  # Jumping up
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
