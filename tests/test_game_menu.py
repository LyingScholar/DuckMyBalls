#test_game_menu.py


import unittest
import pygame
from game_menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.Surface((800, 600))
        self.joystick = None  # For testing without joystick
        self.menu = Menu(self.joystick)

    def test_menu_initialization(self):
        self.assertEqual(self.menu.options, ["Start Game", "Instructions", "Credits", "Exit"])
        self.assertEqual(self.menu.selected_option, 0)

    def test_display_menu(self):
        try:
            self.menu.display_menu(self.screen)
        except Exception as e:
            self.fail(f'display_menu raised an exception: {e}')

    def test_execute_option(self):
        self.menu.selected_option = 0  # Start Game
        result = self.menu.execute_option(self.screen)
        self.assertEqual(result, "start")

        self.menu.selected_option = 3  # Exit
        result = self.menu.execute_option(self.screen)
        self.assertEqual(result, "exit")

    def test_show_instructions(self):
        try:
            self.menu.show_instructions(self.screen)
        except Exception as e:
            self.fail(f'show_instructions raised an exception: {e}')

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()

