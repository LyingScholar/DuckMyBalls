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
    pygame.joystick.init()  # Initialize joystick module

    # Initialize joystick
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick detected: {joystick.get_name()}")
    else:
        print("No joystick detected.")
        return  # Exit if no joystick is connected

    pygame.mixer.music.load(MENU_MUSIC)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("P Ducky")
    clock = pygame.time.Clock()

    menu = Menu(joystick)  # Pass joystick to menu
    result = menu.run(screen)
    if result == "exit":
        pygame.quit()
        return
    elif result != "start":
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
        result = cutscene.run(screen, joystick)
        if result == "exit":
            break
        if not play_level(screen, duck, level, clock, joystick):
            break
        current_level_idx += 1

    pygame.quit()

def play_level(screen, duck, level, clock, joystick):
    camera_x = 0
    running = True
    while running:
        clock.tick(FPS)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            # Joystick input
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 5:  # Button 5 - Jump
                    duck.jump()
                elif event.button == 1:  # Button 1 - Move Left
                    duck.move(-1)
                elif event.button == 0:  # Button 0 - Move Right
                    duck.move(1)
                elif event.button == 8 or event.button == 9:  # Button 9 0r 8 - Exit
                    return False
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 1 or event.button == 5:
                    # Stop movement when left or right button is released
                    duck.stop()

        # Continuous joystick input (for holding down buttons)
        if joystick:
            # For continuous movement, check if the buttons are pressed
            if joystick.get_button(1):  # Button 1 - Move Left
                duck.move(-1)
            elif joystick.get_button(0):  # Button 5 - Move Right
                duck.move(1)
            else:
                # Only stop if neither left nor right is pressed
                duck.stop()
            # Jump is handled in JOYBUTTONDOWN to prevent continuous jumping

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
        [{'image': DUCK_IMAGE_1, 'position': (200, 200), 'size': (200, 200)}],
        [{'image': DUCK_IMAGE_2, 'position': (200, 200), 'size': (100, 100)}],
        [{'image': DUCK_IMAGE_3, 'position': (200, 200), 'size': (100, 100)}],
    ]
    # Assume THE_DUCK_IMAGE is defined in settings.py for the final duck image
    final_duck = {'image': THE_DUCK_IMAGE, 'position': (390, 100), 'size': (400, 400)}
    return Cutscene(CUTSCENE_BACKGROUNDS[index], [characters[index][0], final_duck], CUTSCENE_DIALOGUES[index])

if __name__ == "__main__":
    main()
