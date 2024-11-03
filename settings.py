# settings.py

import os
import pygame

# Screen dimensions and FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Asset paths
ASSET_FOLDER = os.path.join(os.path.dirname(__file__), 'assets')
DUCK_IMAGE = os.path.join(ASSET_FOLDER, 'duck.png')
THE_DUCK_IMAGE = os.path.join(ASSET_FOLDER, 'duck_cutscene.png')
DUCK_IMAGE_1 = os.path.join(ASSET_FOLDER, 'duck1.png')
DUCK_IMAGE_2 = os.path.join(ASSET_FOLDER, 'duck2.png')
DUCK_IMAGE_3 = os.path.join(ASSET_FOLDER, 'duck3.png')
OBSTACLE_IMAGE = os.path.join(ASSET_FOLDER, 'obstacle.png')
GROUND_IMAGE = os.path.join(ASSET_FOLDER, 'ground.png')
BACKGROUND_IMAGES = [
    os.path.join(ASSET_FOLDER, 'background_flower_field.png'),
    os.path.join(ASSET_FOLDER, 'background_city_sewer.png'),
    os.path.join(ASSET_FOLDER, 'background_polluted_river.png')
]
CUTSCENE_BACKGROUNDS = [
    os.path.join(ASSET_FOLDER, 'cutscene_1_bg.jpg'),
    os.path.join(ASSET_FOLDER, 'cutscene_2_bg.png'),
    os.path.join(ASSET_FOLDER, 'cutscene_3_bg.jpg')
]
MENU_BACKGROUND = os.path.join(ASSET_FOLDER, 'menu_background.png')
MENU_MUSIC = os.path.join(ASSET_FOLDER, 'menu.mp3')

# Dialogues
DIALOGUE_FOLDER = os.path.join(os.path.dirname(__file__), 'dialogues')
CUTSCENE_DIALOGUES = [
    os.path.join(DIALOGUE_FOLDER, 'cutscene_dialogues_1.csv'),
    os.path.join(DIALOGUE_FOLDER, 'cutscene_dialogues_1A.csv'),
    os.path.join(DIALOGUE_FOLDER, 'cutscene_dialogues_2.csv'),
    os.path.join(DIALOGUE_FOLDER, 'cutscene_dialogues_2A.csv'),
    os.path.join(DIALOGUE_FOLDER, 'cutscene_dialogues_3.csv'),
    os.path.join(DIALOGUE_FOLDER, 'cutscene_dialogues_3A.csv')
]

# Game physics
GRAVITY = 0.6
JUMP_FORCE = 12

# Controls
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_JUMP = pygame.K_SPACE
