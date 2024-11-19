# tests/test_main.py

import pytest
import pygame
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from duck_game.duck import Duck
from duck_game.settings import *
from duck_game import main

@pytest.fixture(scope='module')
def setup_pygame():
    pygame.init()
    pygame.display.set_mode((800, 600))
    yield
    pygame.quit()
def test_handle_input_keyboard_left(setup_pygame):
    duck = Duck(100, 100)
    with patch('pygame.key.get_pressed') as mock_get_pressed:
        keys = [0] * 512  # Length of keys array is 512
        SCANCODE_LEFT = 80
        keys[SCANCODE_LEFT] = 1  # Simulate left arrow key pressed
        mock_get_pressed.return_value = keys
        main.handle_input(duck, joystick=None)
        assert duck.vx == -duck.speed

def test_handle_input_keyboard_right(setup_pygame):
    duck = Duck(100, 100)
    with patch('pygame.key.get_pressed') as mock_get_pressed:
        keys = [0] * 512
        SCANCODE_RIGHT = 79
        keys[SCANCODE_RIGHT] = 1  # Simulate right arrow key pressed
        mock_get_pressed.return_value = keys
        main.handle_input(duck, joystick=None)
        assert duck.vx == duck.speed

def test_handle_input_keyboard_no_input(setup_pygame):
    duck = Duck(100, 100)
    with patch('pygame.key.get_pressed', return_value=[0] * 512):
        main.handle_input(duck, joystick=None)
        assert duck.vx == 0

def test_handle_input_keyboard_both_keys(setup_pygame):
    duck = Duck(100, 100)
    with patch('pygame.key.get_pressed') as mock_get_pressed:
        keys = [0] * 512
        SCANCODE_LEFT = 80
        SCANCODE_RIGHT = 79
        keys[SCANCODE_LEFT] = 1
        keys[SCANCODE_RIGHT] = 1
        mock_get_pressed.return_value = keys
        main.handle_input(duck, joystick=None)
        # Decide on behavior when both keys are pressed; left takes precedence
        assert duck.vx == -duck.speed


        


def test_handle_input_joystick_left_2(setup_pygame):
    duck = Duck(100, 100)
    joystick = MagicMock()
    joystick.get_init.return_value = True
    joystick.get_button.side_effect = lambda x: 1 if x == 1 else 0  # Button 1 pressed
    with patch('pygame.joystick.get_init', return_value=True):
        main.handle_input(duck, joystick)
        assert duck.vx == -duck.speed

def test_handle_input_joystick_right_2(setup_pygame):
    duck = Duck(100, 100)
    joystick = MagicMock()
    joystick.get_init.return_value = True
    joystick.get_button.side_effect = lambda x: 1 if x == 0 else 0  # Button 0 pressed
    with patch('pygame.joystick.get_init', return_value=True):
        main.handle_input(duck, joystick)
        assert duck.vx == duck.speed

def test_handle_input_joystick_no_input_2(setup_pygame):
    duck = Duck(100, 100)
    joystick = MagicMock()
    joystick.get_init.return_value = True
    joystick.get_button.return_value = 0
    with patch('pygame.joystick.get_init', return_value=True):
        main.handle_input(duck, joystick)
        assert duck.vx == 0

def test_handle_input_joystick_both_buttons_2(setup_pygame):
    duck = Duck(100, 100)
    joystick = MagicMock()
    joystick.get_init.return_value = True
    joystick.get_button.side_effect = lambda x: 1 if x in [0, 1] else 0  # Both buttons pressed
    with patch('pygame.joystick.get_init', return_value=True):
        main.handle_input(duck, joystick)
        # Left takes precedence
        assert duck.vx == -duck.speed
