# tests/test_platform.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.game_platform import Platform

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_static_platform_initialization(setup_pygame):
    image = pygame.Surface((100, 20))
    platform = Platform(100, 200, 100, 20, image)
    assert not platform.moving
    assert platform.rect.x == 100
    assert platform.rect.y == 200

def test_moving_platform_initialization(setup_pygame):
    image = pygame.Surface((100, 20))
    platform = Platform(200, 300, 100, 20, image, moving=True, move_range=100, speed=2)
    assert platform.moving
    assert platform.move_range == 100
    assert platform.speed == 2

def test_moving_platform_update(setup_pygame):
    image = pygame.Surface((100, 20))
    platform = Platform(200, 300, 100, 20, image, moving=True, move_range=100, speed=2)
    initial_x = platform.rect.x
    platform.update()
    assert platform.rect.x == initial_x + platform.speed * platform.direction

def test_moving_platform_direction_change(setup_pygame):
    image = pygame.Surface((100, 20))
    platform = Platform(200, 300, 100, 20, image, moving=True, move_range=100, speed=2)
    platform.rect.x = platform.start_pos + platform.move_range
    platform.update()
    assert platform.direction == -1
