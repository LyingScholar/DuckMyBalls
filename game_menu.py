# game_menu.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 64)
        self.selected_option = 0
        self.options = ["Start Game", "Audio", "Exit"]
        self.audio_on = True

    def display_menu(self, screen):
        screen.fill((0, 0, 0))
        for idx, option in enumerate(self.options):
            color = (255, 255, 255) if idx == self.selected_option else (100, 100, 100)
            text_surface = self.font.render(option, True, color)
            x = SCREEN_WIDTH / 2 - text_surface.get_width() / 2
            y = SCREEN_HEIGHT / 2 - text_surface.get_height() / 2 + idx * 70
            screen.blit(text_surface, (x, y))
        pygame.display.flip()

    def run(self, screen):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.display_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:
                            return "start"
                        elif self.selected_option == 1:
                            self.audio_on = not self.audio_on
                        elif self.selected_option == 2:
                            return "exit"
            clock.tick(15)
