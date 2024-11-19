# duck_game/dialogue.py

import pygame
import csv
from duck_game.settings import *

class Dialogue:
    def __init__(self, csv_file):
        self.lines = self.load_dialogue(csv_file)
        self.current_line = None
        self.display_text = ""
        self.font = pygame.font.Font(None, 32)
        self.is_active = True

    def load_dialogue(self, csv_file):
        dialogue = []
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    dialogue.append(f"{row['character']}: {row['text']}")
        except FileNotFoundError:
            print(f"Dialogue file {csv_file} not found.")
            self.is_active = False
        return dialogue

    def update(self):
        if not self.current_line and self.lines:
            self.current_line = self.lines.pop(0)
            self.display_text = ""
        if self.current_line:
            self.display_text = self.current_line
        else:
            self.is_active = False

    def draw(self, screen):
        if self.current_line:
            box_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 100)
            pygame.draw.rect(screen, (0, 0, 0), box_rect)
            pygame.draw.rect(screen, (255, 255, 255), box_rect, 2)
            text_surface = self.font.render(self.display_text, True, (255, 255, 255))
            screen.blit(text_surface, (60, SCREEN_HEIGHT - 140))

    def skip(self):
        self.current_line = None
