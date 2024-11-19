# tests/test_level.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.level import Level
from duck_game.game_platform import Platform
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600))  # Use actual screen size or minimal size
    yield
    pygame.quit()

def test_level_initialization(setup_pygame):
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    platform_data = [
        {'x': 100, 'y': 400, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20))},
        {'x': 300, 'y': 300, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20)), 'moving': True, 'move_range': 200, 'speed': 2}
    ]
    ground_level = 500
    level = Level(background_image, platform_data, ground_level)
    assert len(level.platforms) == 3  # 2 platforms + ground
    assert level.ground_level == ground_level

def test_level_update(setup_pygame):
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    platform_data = [
        {'x': 100, 'y': 400, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20))},
        {'x': 300, 'y': 300, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20)), 'moving': True, 'move_range': 200, 'speed': 2}
    ]
    ground_level = 500
    level = Level(background_image, platform_data, ground_level)
    moving_platform = [p for p in level.platforms if p.moving][0]
    initial_x = moving_platform.rect.x
    level.update()
    assert moving_platform.rect.x == initial_x + moving_platform.speed * moving_platform.direction


def test_level_no_platforms(setup_pygame):
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    platform_data = []
    ground_level = 500
    level = Level(background_image, platform_data, ground_level)
    assert len(level.platforms) == 1  # Only ground platform


def test_level_max_width(setup_pygame):
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    platform_data = [
        {'x': 0, 'y': 400, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20))},
        {'x': 5000, 'y': 400, 'width': 100, 'height': 20, 'image': pygame.Surface((100, 20))}
    ]
    ground_level = 500
    level = Level(background_image, platform_data, ground_level)
    assert level.level_width >= 5100  # Level width should be at least as wide as the furthest platform
