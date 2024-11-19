# tests/test_game_menu.py

import pytest
import pygame
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.game_menu import Menu
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_menu_initialization(setup_pygame):
    joystick = None
    menu = Menu(joystick)
    assert menu.options == ["Start Game", "Instructions", "Credits", "Exit"]
    assert menu.selected_option == 0

def test_display_menu(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    try:
        menu.display_menu(screen)
    except Exception as e:
        assert False, f"display_menu raised an exception: {e}"

def test_execute_option_start(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    menu.selected_option = 0  # Start Game
    result = menu.execute_option(screen)
    assert result == "start"

def test_execute_option_exit(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    menu.selected_option = 3  # Exit
    result = menu.execute_option(screen)
    assert result == "exit"
