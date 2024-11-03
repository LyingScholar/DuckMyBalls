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
        
        # Dialogue box settings
        self.box_width = 700
        self.box_height = 150
        self.box_color = (0, 0, 0)  # Black box for Undertale style
        self.text_color = (255, 255, 255)  # White text

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
            # Calculate position of dialogue box (centered at the bottom)
            screen_width, screen_height = screen.get_size()
            box_x = (screen_width - self.box_width) // 2
            box_y = screen_height - self.box_height - 50  # 50 pixels from the bottom
            
            # Draw the dialogue box
            pygame.draw.rect(screen, self.box_color, (box_x, box_y, self.box_width, self.box_height))
            pygame.draw.rect(screen, self.text_color, (box_x, box_y, self.box_width, self.box_height), 3)  # White outline

            # Prepare and center the text inside the box
            text = f"{self.current_line['character']}: {self.displaying_text}"
            text_surface = self.font.render(text, True, self.text_color)
            text_rect = text_surface.get_rect(center=(screen_width // 2, box_y + self.box_height // 2))
            screen.blit(text_surface, text_rect)

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
