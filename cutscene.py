# cutscene.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, DUCK_IMAGE, SEAGULL_IMAGE, CUTSCENE_DIALOGUE_CSV
from dialogue import Dialogue

class Cutscene:
    def __init__(self):
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0, 0, 0))  # Black background
        self.duck_image = pygame.transform.scale(pygame.image.load(DUCK_IMAGE).convert_alpha(), (50, 50))
        self.seagull_image = pygame.transform.scale(pygame.image.load(SEAGULL_IMAGE).convert_alpha(), (50, 50))
        self.dialogue = Dialogue(CUTSCENE_DIALOGUE_CSV)
        self.font = pygame.font.Font(None, 32)
        self.is_active = True

    def run(self, screen):
        clock = pygame.time.Clock()
        while self.is_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_active = False
                    return "exit"
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.dialogue.skip()
            self.dialogue.update()
            self.draw(screen)
            pygame.display.flip()
            if not self.dialogue.is_active:
                self.is_active = False
            clock.tick(60)
        return "continue"

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        # Draw characters
        screen.blit(self.seagull_image, (100, 400))
        screen.blit(self.duck_image, (200, 400))
        # Draw dialogue
        self.dialogue.draw(screen)
