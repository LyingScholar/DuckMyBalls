# duck_game/camera.py

from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self, level_width, level_height):
        self.offset_x = 0
        self.offset_y = 0
        self.level_width = level_width
        self.level_height = level_height

    def update(self, target_rect):
        """Update camera position based on the target (e.g., duck)."""
        self.offset_x = target_rect.centerx - SCREEN_WIDTH // 2
        self.offset_y = target_rect.centery - SCREEN_HEIGHT // 2
        # Clamp the camera to the level boundaries
        self.offset_x = max(0, min(self.offset_x, self.level_width - SCREEN_WIDTH))
        self.offset_y = max(0, min(self.offset_y, self.level_height - SCREEN_HEIGHT))
