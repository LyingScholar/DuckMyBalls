# main.py

import pygame
from settings import *
from duck import Duck
from level import Level
from game_menu import Menu
from cutscene import Cutscene

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(MENU_MUSIC)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("P Ducky")
    clock = pygame.time.Clock()

    menu = Menu()
    result = menu.run(screen)
    if result == "exit":
        pygame.quit()
        return
    elif result != "start":
        # If the menu didn't return 'start', exit the game
        pygame.quit()
        return

    levels = [create_level(idx) for idx in range(3)]
    cutscenes = [create_cutscene(idx) for idx in range(3)]
    duck = Duck(100, 500)
    current_level_idx = 0

    while current_level_idx < len(levels):
        duck.rect.x = 100  # Reset duck position
        duck.rect.y = 500
        level = levels[current_level_idx]
        cutscene = cutscenes[current_level_idx]
        result = cutscene.run(screen)
        if result == "exit":
            break
        if not play_level(screen, duck, level, clock):
            break
        current_level_idx += 1

    pygame.quit()

def play_level(screen, duck, level, clock):
    camera_x = 0
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == KEY_LEFT:
                    duck.move(-1)
                elif event.key == KEY_RIGHT:
                    duck.move(1)
                elif event.key == KEY_JUMP:
                    duck.jump()
                elif event.key == pygame.K_ESCAPE:
                    # Return to main menu on ESC
                    return False
            elif event.type == pygame.KEYUP:
                if event.key in (KEY_LEFT, KEY_RIGHT):
                    duck.stop()

        duck.update(level.platforms)
        level.update()
        camera_x = max(0, min(duck.rect.x - SCREEN_WIDTH // 2, level.level_width - SCREEN_WIDTH))
        level.draw(screen, camera_x)
        duck.draw(screen, camera_x)
        pygame.display.flip()

        # Check if duck fell below the ground
        if duck.rect.y > SCREEN_HEIGHT:
            # Reset duck position
            duck.rect.x = 100
            duck.rect.y = 500

        if duck.rect.x >= level.level_width - duck.rect.width:
            return True
    return False

def create_level(index):
    platform_data = [
        # Level 1: Flower Field
        [
            {'x': 300, 'y': 500, 'width': 100, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 500, 'y': 450, 'width': 100, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 700, 'y': 400, 'width': 100, 'height': 20, 'image': OBSTACLE_IMAGE, 'moving': True, 'move_range': 200, 'speed': 2},
            {'x': 1000, 'y': 350, 'width': 100, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 1200, 'y': 300, 'width': 100, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 1400, 'y': 250, 'width': 100, 'height': 20, 'image': OBSTACLE_IMAGE},
        ],
        # Level 2: City Sewer
        [
            {'x': 300, 'y': 500, 'width': 150, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 600, 'y': 450, 'width': 150, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 900, 'y': 400, 'width': 150, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 1200, 'y': 350, 'width': 150, 'height': 20, 'image': OBSTACLE_IMAGE, 'moving': True, 'move_range': 300, 'speed': 3},
            {'x': 1600, 'y': 300, 'width': 150, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 1900, 'y': 250, 'width': 150, 'height': 20, 'image': OBSTACLE_IMAGE},
        ],
        # Level 3: Polluted River
        [
            {'x': 300, 'y': 500, 'width': 200, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 700, 'y': 450, 'width': 200, 'height': 20, 'image': OBSTACLE_IMAGE, 'moving': True, 'move_range': 400, 'speed': 4},
            {'x': 1100, 'y': 400, 'width': 200, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 1500, 'y': 350, 'width': 200, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 1900, 'y': 300, 'width': 200, 'height': 20, 'image': OBSTACLE_IMAGE},
            {'x': 2300, 'y': 250, 'width': 200, 'height': 20, 'image': OBSTACLE_IMAGE},
        ]
    ]
    ground_level = 550  # Y-coordinate of the ground
    return Level(BACKGROUND_IMAGES[index], platform_data[index], ground_level)

def create_cutscene(index):
    characters = [
        [{'image': DUCK_IMAGE, 'position': (350, 400), 'size': (100, 100)}],
        [{'image': DUCK_IMAGE, 'position': (350, 400), 'size': (100, 100)}],
        [{'image': DUCK_IMAGE, 'position': (350, 400), 'size': (100, 100)}]
    ]
    return Cutscene(CUTSCENE_BACKGROUNDS[index], characters[index], CUTSCENE_DIALOGUES[index])

if __name__ == "__main__":
    main()
