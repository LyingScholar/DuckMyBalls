# tests/test_camera.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.camera import Camera
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_camera_initialization(setup_pygame):
    level_width = 2000
    level_height = 1000
    camera = Camera(level_width, level_height)
    assert camera.offset_x == 0
    assert camera.offset_y == 0
    assert camera.level_width == level_width
    assert camera.level_height == level_height

def test_camera_update(setup_pygame):
    level_width = 2000
    level_height = 1000
    camera = Camera(level_width, level_height)
    target_rect = pygame.Rect(500, 500, 50, 50)
    camera.update(target_rect)
    expected_offset_x = target_rect.centerx - SCREEN_WIDTH // 2
    expected_offset_y = target_rect.centery - SCREEN_HEIGHT // 2
    expected_offset_x = max(0, min(expected_offset_x, level_width - SCREEN_WIDTH))
    expected_offset_y = max(0, min(expected_offset_y, level_height - SCREEN_HEIGHT))
    assert camera.offset_x == expected_offset_x
    assert camera.offset_y == expected_offset_y
