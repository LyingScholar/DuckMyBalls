# duck_game/game_menu.py

import pygame
import os
from duck_game.settings import *
from duck_game.resource_manager import ResourceManager

class Menu:
    def __init__(self, joystick):
        self.background = ResourceManager.load_image(MENU_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title_font = pygame.font.SysFont("Comic Sans MS", 72)
        self.font = pygame.font.SysFont("Impact", 35)
        self.options = ["Start Game", "Instructions", "Credits", "Exit"]
        self.selected_option = 0
        self.title = self.title_font.render("Duckenomenon", True, (255, 255, 0))
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        result = self.execute_option(screen)
                        if result in ["exit", "start"]:
                            return result
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # Move up
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.button == 2:  # Move down
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.button == 5:  # Select
                        result = self.execute_option(screen)
                        if result in ["exit", "start"]:
                            return result
                    elif event.button == 3:  # Exit
                        return "exit"
            clock.tick(FPS)

    def execute_option(self, screen):
        if self.options[self.selected_option] == "Start Game":
            return "start"
        elif self.options[self.selected_option] == "Instructions":
            self.show_instructions(screen)
        elif self.options[self.selected_option] == "Credits":
            self.show_credits(screen)
        elif self.options[self.selected_option] == "Exit":
            return "exit"

    def show_instructions(self, screen):
        instructions = [
            "Instructions:",
            "- Use arrow keys or controller to move.",
            "- Press Space or Button 5 to jump.",
            "- Reach the end of each level.",
            "- Press Esc or Button 3 to exit."
        ]
        self.display_text_screen(screen, instructions)

    def show_credits(self, screen):
        credits = [
            "Credits:",
            "Game Developer: Zane",
            "Graphics Designer: Jennie Wiley",
            "Music: Jennie Wiley",
            "Special Thanks: Noah and Lu",
            "Press any key to return."
        ]
        self.display_text_screen(screen, credits)

    def display_text_screen(self, screen, lines):
        running = True
        clock = pygame.time.Clock()
        while running:
            screen.fill((0, 0, 0))
            for idx, line in enumerate(lines):
                text_surface = self.font.render(line, True, (255, 255, 255))
                rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + idx * 50))
                screen.blit(text_surface, rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
                    running = False
            clock.tick(FPS)
