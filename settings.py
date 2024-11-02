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
SEAGULL_IMAGE = os.path.join(ASSET_FOLDER, 'seagull.png')

BACKGROUND_FLOWER_FIELD = os.path.join(ASSET_FOLDER, 'background_flower_field.png')
BACKGROUND_CITY_SEWER = os.path.join(ASSET_FOLDER, 'background_city_sewer.png')
BACKGROUND_POLLUTED_RIVER = os.path.join(ASSET_FOLDER, 'background_polluted_river.png')
GROUND_IMAGE = os.path.join(ASSET_FOLDER, 'ground.png')


OBSTACLE_IMAGE = os.path.join(ASSET_FOLDER, 'obstacle.png')
SPIKE_IMAGE = os.path.join(ASSET_FOLDER, 'spike.png')

# Dialogus
DIALOGUE_CSV = os.path.join(os.path.dirname(__file__), 'dialogues.csv')
CUTSCENE_DIALOGUE_CSV = os.path.join(os.path.dirname(__file__), 'cutscene_dialogues.csv')


# Game settings
GRAVITY = 0.5
JUMP_FORCE = 15
TEXT_SPEED = 0.1  # Lower is faster



# Controls
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_JUMP = pygame.K_SPACE
