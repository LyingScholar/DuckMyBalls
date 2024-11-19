#test_camera.py
import unittest
from camera import Camera
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class TestCamera(unittest.TestCase):
    def setUp(self):
        self.level_width = 2000
        self.level_height = 1000
        self.camera = Camera(self.level_width, self.level_height)
        self.target_rect = pygame.Rect(500, 500, 50, 50)

    def test_camera_initialization(self):
        self.assertEqual(self.camera.offset_x, 0)
        self.assertEqual(self.camera.offset_y, 0)

    def test_camera_update(self):
        self.camera.update(self.target_rect)
        expected_offset_x = self.target_rect.centerx - SCREEN_WIDTH // 2
        expected_offset_y = self.target_rect.centery - SCREEN_HEIGHT // 2
        self.assertEqual(self.camera.offset_x, expected_offset_x)
        self.assertEqual(self.camera.offset_y, expected_offset_y)

    def test_camera_bounds(self):
        self.target_rect.centerx = 0
        self.target_rect.centery = 0
        self.camera.update(self.target_rect)
        self.assertEqual(self.camera.offset_x, 0)
        self.assertEqual(self.camera.offset_y, 0)

        self.target_rect.centerx = self.level_width
        self.target_rect.centery = self.level_height
        self.camera.update(self.target_rect)
        max_offset_x = self.level_width - SCREEN_WIDTH
        max_offset_y = self.level_height - SCREEN_HEIGHT
        self.assertEqual(self.camera.offset_x, max_offset_x)
        self.assertEqual(self.camera.offset_y, max_offset_y)

if __name__ == '__main__':
    unittest.main()
