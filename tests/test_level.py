#test_level.py

import unittest
import pygame
from level import Level
from platform import Platform
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.platform_data = [
            {'x': 100, 'y': 400, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20))},
            {'x': 300, 'y': 300, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20)), 'moving': True, 'move_range': 200, 'speed': 2}
        ]
        self.level = Level(
            background_image=pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)),
            platform_data=self.platform_data,
            ground_level=500
        )

    def test_platforms_created(self):
        self.assertEqual(len(self.level.platforms), 3)  # 2 platforms + ground

    def test_ground_added(self):
        ground_platform = self.level.ground_platform
        self.assertIsNotNone(ground_platform)
        self.assertEqual(ground_platform.rect.y, self.level.ground_level)

    def test_level_width(self):
        expected_width = max(p.rect.right for p in self.level.platforms)
        self.assertEqual(self.level.level_width, expected_width)

    def test_update(self):
        moving_platform = [p for p in self.level.platforms if getattr(p, 'moving', False)]
        initial_x = moving_platform[0].rect.x
        self.level.update()
        self.assertNotEqual(moving_platform[0].rect.x, initial_x)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
