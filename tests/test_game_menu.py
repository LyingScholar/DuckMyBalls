# tests/test_game_menu.py

import pytest
import pygame
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.game_menu import Menu
from duck_game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600))  # Use actual screen size or minimal size
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


def test_menu_navigation_up(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    initial_option = menu.selected_option
    # Mock pygame.event.get to simulate KEYDOWN event for K_UP
    with patch('pygame.event.get', return_value=[
        pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP}),
        pygame.event.Event(pygame.QUIT)
    ]):
        with patch.object(menu, 'display_menu'):
            result = menu.run(screen)
    expected_option = (initial_option - 1) % len(menu.options)
    assert menu.selected_option == expected_option

def test_menu_navigation_down(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    initial_option = menu.selected_option
    # Mock pygame.event.get to simulate KEYDOWN event for K_DOWN
    with patch('pygame.event.get', return_value=[
        pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN}),
        pygame.event.Event(pygame.QUIT)
    ]):
        with patch.object(menu, 'display_menu'):
            result = menu.run(screen)
    expected_option = (initial_option + 1) % len(menu.options)
    assert menu.selected_option == expected_option



def test_menu_execute_option_instructions(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    menu.selected_option = 1  # Instructions
    with patch.object(menu, 'show_instructions') as mock_show_instructions:
        result = menu.execute_option(screen)
    mock_show_instructions.assert_called_once()
    assert result is None

def test_menu_execute_option_credits(setup_pygame):
    screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    joystick = None
    menu = Menu(joystick)
    menu.selected_option = 2  # Credits
    with patch.object(menu, 'show_credits') as mock_show_credits:
        result = menu.execute_option(screen)
    mock_show_credits.assert_called_once()
    assert result is None
