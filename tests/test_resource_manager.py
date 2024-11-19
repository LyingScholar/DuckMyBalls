# tests/test_resource_manager.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.resource_manager import ResourceManager

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600))  # Use actual screen size or minimal size
    yield
    pygame.quit()

def test_load_image(setup_pygame):
    image_path = 'test_image.png'
    # Create a test image
    test_image = pygame.Surface((100, 100))
    pygame.image.save(test_image, image_path)
    try:
        image = ResourceManager.load_image(image_path)
        assert isinstance(image, pygame.Surface)
    finally:
        os.remove(image_path)
