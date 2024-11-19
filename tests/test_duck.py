# tests/test_duck.py

import pytest
import pygame
import os
import sys

# Add the parent directory to sys.path so that duck_game can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.duck import Duck
from duck_game.platform import Platform
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITY, JUMP_FORCE

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def duck(setup_pygame):
    duck = Duck(100, 100)
    return duck

@pytest.fixture
def platforms():
    platform = Platform(100, 150, 100, 20, pygame.Surface((100, 20)))
    return pygame.sprite.Group(platform)

def test_initial_position(duck):
    assert duck.rect.x == 100
    assert duck.rect.y == 100

def test_move_left(duck):
    duck.move(-1)
    assert duck.vx == -duck.speed

def test_move_right(duck):
    duck.move(1)
    assert duck.vx == duck.speed

def test_stop(duck):
    duck.move(1)
    duck.stop()
    assert duck.vx == 0

def test_jump(duck):
    duck.on_ground = True
    duck.jump()
    assert duck.vy == -JUMP_FORCE
    assert not duck.on_ground

def test_apply_gravity(duck):
    initial_vy = duck.vy
    duck.apply_gravity()
    assert duck.vy == initial_vy + GRAVITY

def test_collision_with_platform(duck, platforms):
    duck.rect.y = 140  # Position just above the platform
    duck.vy = 5  # Simulate falling
    duck.update(platforms)
    assert duck.on_ground
    assert duck.rect.bottom == platforms.sprites()[0].rect.top
    assert duck.vy == 0

def test_fall_off_screen(duck):
    duck.rect.y = SCREEN_HEIGHT + 100
    assert duck.rect.y > SCREEN_HEIGHT