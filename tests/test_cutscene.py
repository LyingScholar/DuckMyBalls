# tests/test_cutscene.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.cutscene import Cutscene
from duck_game.dialogue import Dialogue
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_cutscene_initialization(setup_pygame):
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    char_image = pygame.Surface((50, 50))
    characters = [
        {'image': char_image, 'position': (100, 100), 'size': (50, 50)},
    ]
    dialogue_csv = 'test_dialogue.csv'
    with open(dialogue_csv, 'w') as file:
        file.write('character,text\n')
        file.write('Duck,Hello!\n')
    cutscene = Cutscene(background_image, characters, dialogue_csv)
    assert cutscene.is_active
    assert isinstance(cutscene.dialogue, Dialogue)
    os.remove(dialogue_csv)

def test_cutscene_draw(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    char_image = pygame.Surface((50, 50))
    characters = [
        {'image': char_image, 'position': (100, 100), 'size': (50, 50)},
    ]
    dialogue_csv = 'test_dialogue.csv'
    with open(dialogue_csv, 'w') as file:
        file.write('character,text\n')
        file.write('Duck,Hello!\n')
    cutscene = Cutscene(background_image, characters, dialogue_csv)
    try:
        cutscene.draw(screen)
    except Exception as e:
        assert False, f"Draw method raised an exception: {e}"
    os.remove(dialogue_csv)
