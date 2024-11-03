# game_menu.py

import pygame
import os
from settings import *

class Menu:
    def __init__(self, joystick):
        self.background = pygame.transform.scale(
            pygame.image.load(MENU_BACKGROUND).convert(),
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.title_font = pygame.font.SysFont("Comic Sans", 72)
        self.font = pygame.font.SysFont("Impact", 35)
        self.options = ["Start Game", "Instructions", "Credits", "Exit"]
        self.selected_option = 0
        self.music_volume = 1.0
        self.sfx_volume = 1.0
        self.title = self.title_font.render("Duckenomenon", True, (255, 255, 0))

        # Joystick passed from main
        self.joystick = joystick

    def display_menu(self, screen):
        screen.blit(self.background, (0, 0))
        title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(self.title, title_rect)
        for idx, option in enumerate(self.options):
            color = (255, 255, 255) if idx == self.selected_option else (180, 180, 180)
            text_surface = self.font.render(option, True, color)
            rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + idx * 90))
            screen.blit(text_surface, rect)
        pygame.display.flip()

    def run(self, screen):
        clock = pygame.time.Clock()
        while True:
            self.display_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # Move up
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.button == 2:  # Move down
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.button == 5:  # Select
                        result = self.execute_option(screen)
                        if result == "exit" or result == "start":
                            return result
                    elif event.button == 3:  # Exit
                        return "exit"
            clock.tick(FPS)

    def execute_option(self, screen):
        if self.options[self.selected_option] == "Start Game":
            return "start"
        elif self.options[self.selected_option] == "Instructions":
            result = self.show_instructions(screen)
            if result == "exit":
                return "exit"
        elif self.options[self.selected_option] == "Credits":
            result = self.show_credits(screen)
            if result == "exit":
                return "exit"
        elif self.options[self.selected_option] == "Exit":
            return "exit"


    def show_instructions(self, screen):
        instructions = [
            "Instructions:",
            "- Use controller buttons to move.",
            "- Button 0 to jump.",
            "- Reach the end of each level.",
            "- Press button 2 to return."
        ]
        result = self.display_text_screen(screen, instructions)
        if result == "exit":
            return "exit"

    def show_credits(self, screen):
        credits = [
            "Credits:",
            "Game Developer: Zane",
            "Graphics Designer: Jennie Wiley",
            "Music: Jennie Wiley",
            "Special Thanks: Noah and Lu",
            "Press button 2 to return."
        ]
        result = self.display_text_screen(screen, credits)
        if result == "exit":
            return "exit"

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
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0 or event.button == 2:
                        return
            pygame.time.Clock().tick(FPS)
