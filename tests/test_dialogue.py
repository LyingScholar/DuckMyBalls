# tests/test_dialogue.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.dialogue import Dialogue

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_dialogue_initialization(setup_pygame):
    dialogue_csv = 'test_dialogue.csv'
    with open(dialogue_csv, 'w') as file:
        file.write('character,text\n')
        file.write('Duck,Hello!\n')
        file.write('Duck,Welcome to the game.\n')
    dialogue = Dialogue(dialogue_csv)
    assert len(dialogue.lines) == 2
    os.remove(dialogue_csv)

def test_dialogue_update(setup_pygame):
    dialogue_csv = 'test_dialogue.csv'
    with open(dialogue_csv, 'w') as file:
        file.write('character,text\n')
        file.write('Duck,Hello!\n')
    dialogue = Dialogue(dialogue_csv)
    dialogue.update()
    assert dialogue.display_text == 'Duck: Hello!'
    os.remove(dialogue_csv)

def test_dialogue_skip(setup_pygame):
    dialogue_csv = 'test_dialogue.csv'
    with open(dialogue_csv, 'w') as file:
        file.write('character,text\n')
        file.write('Duck,Hello!\n')
        file.write('Duck,Welcome to the game.\n')
    dialogue = Dialogue(dialogue_csv)
    dialogue.update()
    dialogue.skip()
    dialogue.update()
    assert dialogue.display_text == 'Duck: Welcome to the game.'
    os.remove(dialogue_csv)
