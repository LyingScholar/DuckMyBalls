#test_dialogue.py

import unittest
import pygame
from dialogue import Dialogue

class TestDialogue(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.dialogue_csv = 'test_dialogue.csv'
        with open(self.dialogue_csv, 'w') as file:
            file.write('character,text\n')
            file.write('Duck,Hello!\n')
            file.write('Duck,Welcome to the game.\n')
        self.dialogue = Dialogue(self.dialogue_csv)
        self.screen = pygame.Surface((800, 600))

    def test_load_dialogue(self):
        self.assertEqual(len(self.dialogue.lines), 2)

    def test_update(self):
        self.dialogue.update()
        self.assertEqual(self.dialogue.display_text, 'Duck: Hello!')

    def test_skip(self):
        self.dialogue.update()
        self.dialogue.skip()
        self.dialogue.update()
        self.assertEqual(self.dialogue.display_text, 'Duck: Welcome to the game.')

    def test_draw(self):
        try:
            self.dialogue.update()
            self.dialogue.draw(self.screen)
        except Exception as e:
            self.fail(f'Draw method raised an exception: {e}')

    def tearDown(self):
        import os
        os.remove(self.dialogue_csv)
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
