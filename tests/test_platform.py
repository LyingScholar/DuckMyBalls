#test_platform.py

import unittest
import pygame
from platform import Platform

class TestPlatform(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.static_platform = Platform(100, 200, 100, 20, pygame.Surface((100, 20)))
        self.moving_platform = Platform(200, 300, 100, 20, pygame.Surface((100, 20)), moving=True, move_range=100, speed=2)

    def test_static_platform_initialization(self):
        self.assertFalse(self.static_platform.moving)
        self.assertEqual(self.static_platform.rect.x, 100)
        self.assertEqual(self.static_platform.rect.y, 200)

    def test_moving_platform_initialization(self):
        self.assertTrue(self.moving_platform.moving)
        self.assertEqual(self.moving_platform.move_range, 100)
        self.assertEqual(self.moving_platform.speed, 2)

    def test_moving_platform_update(self):
        initial_x = self.moving_platform.rect.x
        self.moving_platform.update()
        self.assertEqual(self.moving_platform.rect.x, initial_x + self.moving_platform.speed)

    def test_moving_platform_direction_change(self):
        self.moving_platform.rect.x = self.moving_platform.start_pos + self.moving_platform.move_range
        self.moving_platform.update()
        self.assertEqual(self.moving_platform.direction, -1)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
