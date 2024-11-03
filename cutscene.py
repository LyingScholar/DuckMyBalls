# cutscene.py

import pygame
from settings import *
from dialogue import Dialogue

class Cutscene:
    def __init__(self, background_image, characters, dialogue_csv):
        bg = pygame.image.load(background_image)
        self.background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.characters = characters
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
            img = pygame.image.load(char['image']).convert_alpha()
            img = pygame.transform.scale(img, char.get('size', (100, 100)))
            screen.blit(img, char['position'])
        self.dialogue.draw(screen)
