# cutscene.py

import pygame
from .settings import *
from .dialogue import Dialogue

class Cutscene:
    def __init__(self, background_image, characters, dialogue_csv):
        bg = pygame.image.load(background_image)
        self.background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.characters = []
        for char in characters:
            img = pygame.image.load(char['image']).convert_alpha()
            img = pygame.transform.scale(img, char.get('size', (100, 100)))
            self.characters.append({'image': img, 'position': char['position']})
        self.dialogue = Dialogue(dialogue_csv)
        self.is_active = True

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        for char in self.characters:
            screen.blit(char['image'], char['position'])
        self.dialogue.draw(screen)

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
