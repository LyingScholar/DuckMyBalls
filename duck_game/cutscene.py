# duck_game/cutscene.py

import pygame
from duck_game.settings import *
from duck_game.dialogue import Dialogue
from duck_game.resource_manager import ResourceManager

class Cutscene:
    def __init__(self, background_image, characters, dialogue_csv):
        bg = ResourceManager.load_image(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = bg
        self.characters = []
        for char in characters:
            img = ResourceManager.load_image(char['image'], char.get('size', (100, 100)))
            self.characters.append({'image': img, 'position': char['position']})
        self.dialogue = Dialogue(dialogue_csv)
        self.is_active = True

    def run(self, screen, joystick):
        clock = pygame.time.Clock()
        while self.is_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_active = False
                    return "exit"
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.dialogue.skip()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dialogue.skip()
            self.dialogue.update()
            self.draw(screen)
            pygame.display.flip()
            if not self.dialogue.is_active:
                self.is_active = False
            clock.tick(FPS)
        return "continue"

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        for char in self.characters:
            screen.blit(char['image'], char['position'])
        self.dialogue.draw(screen)
