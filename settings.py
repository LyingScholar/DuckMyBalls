# settings.py
import os
import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Asset paths
ASSET_FOLDER = os.path.join(os.path.dirname(__file__), 'assets')
DUCK_IMAGE = os.path.join(ASSET_FOLDER, 'duck.png')
DUCK_IMAGE_1 = os.path.join(ASSET_FOLDER, 'duck1.png')
DUCK_IMAGE_2 = os.path.join(ASSET_FOLDER, 'duck2.png')
DUCK_IMAGE_3 = os.path.join(ASSET_FOLDER, 'duck3.png')

CUTSCENE_1_BG = os.path.join(ASSET_FOLDER, 'cutscene_1_bg.jpg')
CUTSCENE_2_BG = os.path.join(ASSET_FOLDER, 'cutscene_2_bg.png')
CUTSCENE_3_BG = os.path.join(ASSET_FOLDER, 'cutscene_3_bg.jpg')

BACKGROUND_FLOWER_FIELD = os.path.join(ASSET_FOLDER, 'background_flower_field.png')
BACKGROUND_CITY_SEWER = os.path.join(ASSET_FOLDER, 'background_city_sewer.png')
BACKGROUND_POLLUTED_RIVER = os.path.join(ASSET_FOLDER, 'background_polluted_river.png')

GROUND_IMAGE_1 = os.path.join(ASSET_FOLDER, 'ground_1.png')
GROUND_IMAGE_2 = os.path.join(ASSET_FOLDER, 'ground_2.png')
GROUND_IMAGE_3 = os.path.join(ASSET_FOLDER, 'ground_3.png')

DUCK_IMAGE_CUTSCENE = os.path.join(ASSET_FOLDER, 'duck_cutscene.png')

OBSTACLE_IMAGE = os.path.join(ASSET_FOLDER, 'obstacle.png')
OBSTACLE_IMAGE_2 = os.path.join(ASSET_FOLDER, 'obstacle_2.png')


MENU_MUSIC = os.path.join(ASSET_FOLDER, 'menu.mp3')

# Dialogus
CUTSCENE_DIALOGUE_CSV_1 = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues_1.csv')
CUTSCENE_DIALOGUE_CSV_2 = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues_2.csv')
CUTSCENE_DIALOGUE_CSV_3 = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues_3.csv')

CUTSCENE_DIALOGUE_CSV_1A = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues_1A.csv')
CUTSCENE_DIALOGUE_CSV_2A = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues_2A.csv')
CUTSCENE_DIALOGUE_CSV_3A = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues_3A.csv')

# Game settings
GRAVITY = 0.5
JUMP_FORCE = 15
TEXT_SPEED = 0.1  # Lower is faster



# Controls
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_JUMP = pygame.K_SPACE
