# dialogue.py
import pygame
import csv
from settings import TEXT_SPEED

class Dialogue:
    def __init__(self, csv_file):
        self.dialogue_queue = self.load_dialogue(csv_file)
        self.current_line = None
        self.displaying_text = ""
        self.index = 0
        self.font = pygame.font.Font(None, 32)
        self.is_active = True
        self.line_completed = False  # Indicates if the current line has finished displaying

    def load_dialogue(self, csv_file):
        dialogue_queue = []
        with open(csv_file, "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dialogue_queue.append({
                    "character": row["character"],
                    "text": row["text"],
                })
        return dialogue_queue

    def update(self):
        if self.current_line is None:
            if self.dialogue_queue:
                self.current_line = self.dialogue_queue.pop(0)
                self.displaying_text = ""
                self.index = 0
                self.line_completed = False
            else:
                self.is_active = False  # No more dialogue lines
        else:
            if not self.line_completed:
                # Display text letter by letter
                if self.index < len(self.current_line["text"]):
                    self.displaying_text += self.current_line["text"][self.index]
                    self.index += 1
                else:
                    # Line has finished displaying
                    self.line_completed = True

    def draw(self, screen):
        if self.current_line:
            text = f"{self.current_line['character']}: {self.displaying_text}"
            text_surface = self.font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (50, 500))  # Adjust position as needed

    def skip(self):
        if self.current_line:
            if not self.line_completed:
                # Finish displaying the current line
                self.displaying_text = self.current_line["text"]
                self.index = len(self.current_line["text"])
                self.line_completed = True
            else:
                # Proceed to the next line
                self.current_line = None
