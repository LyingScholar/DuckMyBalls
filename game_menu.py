# game_menu.py

import pygame
import os
from settings import *

class Menu:
    def __init__(self):
        self.background = pygame.transform.scale(
            pygame.image.load(MENU_BACKGROUND).convert(),
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.title_font = pygame.font.Font(None, 72)
        self.font = pygame.font.Font(None, 48)
        self.options = ["Start Game", "Audio Settings", "Instructions", "Credits", "Exit"]
        self.selected_option = 0
        self.music_volume = 1.0
        self.sfx_volume = 1.0
        self.title = self.title_font.render("P Ducky Adventure", True, (255, 255, 0))

    def display_menu(self, screen):
        screen.blit(self.background, (0, 0))
        title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(self.title, title_rect)
        for idx, option in enumerate(self.options):
            color = (255, 255, 255) if idx == self.selected_option else (180, 180, 180)
            text_surface = self.font.render(option, True, color)
            rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + idx * 60))
            screen.blit(text_surface, rect)
        pygame.display.flip()

    def run(self, screen):
        clock = pygame.time.Clock()
        while True:
            self.display_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.execute_option(screen)
            clock.tick(FPS)

    def execute_option(self, screen):
        if self.options[self.selected_option] == "Start Game":
            return "start"
        elif self.options[self.selected_option] == "Audio Settings":
            self.audio_settings(screen)
        elif self.options[self.selected_option] == "Instructions":
            self.show_instructions(screen)
        elif self.options[self.selected_option] == "Credits":
            self.show_credits(screen)
        elif self.options[self.selected_option] == "Exit":
            return "exit"

    def audio_settings(self, screen):
        options = ["Music Volume", "Sound Effects Volume", "Back"]
        selected = 0
        while True:
            screen.fill((0, 0, 0))
            for idx, opt in enumerate(options):
                color = (255, 255, 255) if idx == selected else (180, 180, 180)
                if idx == 0:
                    text = f"{opt}: {int(self.music_volume * 100)}%"
                elif idx == 1:
                    text = f"{opt}: {int(self.sfx_volume * 100)}%"
                else:
                    text = opt
                text_surface = self.font.render(text, True, color)
                rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + idx * 60))
                screen.blit(text_surface, rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_LEFT:
                        if selected == 0:
                            self.music_volume = max(0.0, self.music_volume - 0.1)
                            pygame.mixer.music.set_volume(self.music_volume)
                        elif selected == 1:
                            self.sfx_volume = max(0.0, self.sfx_volume - 0.1)
                    elif event.key == pygame.K_RIGHT:
                        if selected == 0:
                            self.music_volume = min(1.0, self.music_volume + 0.1)
                            pygame.mixer.music.set_volume(self.music_volume)
                        elif selected == 1:
                            self.sfx_volume = min(1.0, self.sfx_volume + 0.1)
                    elif event.key == pygame.K_RETURN and selected == 2:
                        return

    def show_instructions(self, screen):
        instructions = [
            "Instructions:",
            "- Use arrow keys to move.",
            "- Press 'Space' to jump.",
            "- Reach the end of each level.",
            "- Press 'Esc' to return."
        ]
        self.display_text_screen(screen, instructions)

    def show_credits(self, screen):
        credits = [
            "Credits:",
            "Game Developer: Zane",
            "Graphics Designer: Jennie Wiley",
            "Music: Jennie Wiley",
            "Special Thanks: Noah and Lu",
            "Press 'Esc' to return."
        ]
        self.display_text_screen(screen, credits)

    def display_text_screen(self, screen, lines):
        while True:
            screen.fill((0, 0, 0))
            for idx, line in enumerate(lines):
                text_surface = self.font.render(line, True, (255, 255, 255))
                rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + idx * 50))
                screen.blit(text_surface, rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            pygame.time.Clock().tick(FPS)
