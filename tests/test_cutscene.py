#test_cutscene.py

import unittest
import pygame
from cutscene import Cutscene
from dialogue import Dialogue
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class TestCutscene(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.characters = [
            {'image': pygame.Surface((50, 50)), 'position': (100, 100), 'size': (50, 50)},
            {'image': pygame.Surface((50, 50)), 'position': (200, 100), 'size': (50, 50)}
        ]
        self.dialogue_csv = 'test_dialogue.csv'
        # Create a test dialogue CSV file
        with open(self.dialogue_csv, 'w') as file:
            file.write('character,text\n')
            file.write('Duck,Hello!\n')
            file.write('Duck,Welcome to the game.\n')
        self.cutscene = Cutscene(self.background_image, self.characters, self.dialogue_csv)
        self.screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def test_cutscene_initialization(self):
        self.assertTrue(self.cutscene.is_active)
        self.assertIsInstance(self.cutscene.dialogue, Dialogue)
        self.assertEqual(len(self.cutscene.characters), 2)

    def test_draw(self):
        try:
            self.cutscene.draw(self.screen)
        except Exception as e:
            self.fail(f'Draw method raised an exception: {e}')

    def tearDown(self):
        import os
        os.remove(self.dialogue_csv)
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
