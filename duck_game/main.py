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
        print("No joystick detected. Using keyboard input.")
        joystick = None

    pygame.mixer.music.load(MENU_MUSIC)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Top Text")
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
        duck.rect.x = 100  # Reset duck
        duck.rect.y = 500
        level = levels[current_level_idx]
        cutscene = cutscenes[current_level_idx]
        result = cutscene.run(screen, joystick)
        if result == "exit":
            break
        if not play_level(screen, duck, level, clock, joystick):
            break
        current_level_idx += 1

    # credits
    end_screen(screen)
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
                if event.button == 5:  # 5 - Jomp
                    duck.jump()
                elif event.button == 1:  # 1 - Left
                    duck.move(-1)
                elif event.button == 0:  # 0 - Right
                    duck.move(1)
                elif event.button == 8 or event.button == 9:  # 8 or 9 - Exit
                    return False
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 1 or event.button == 0:
                    # Stop movement when left or right button is released
                    duck.stop()

        # Continuous joystick input (for holding down buttons)
        if joystick:
            # For continuous movement, check if the buttons are pressed
            if joystick.get_button(1):  # Button 1 - Move Left
                duck.move(-1)
            elif joystick.get_button(0):  # Button 0 - Move Right
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
    ground_level = 550  # Y-coordinate of the ground

    if index == 0:
        # Level 1: Flower Field)
        platform_data = []
        x_positions = [300 + i * 300 for i in range(18)]  # 18 platforms, spacing of 300
        y_positions = [500 - (i % 6) * 50 for i in range(18)]  # Vary y positions
        for i in range(16):
            platform = {
                'x': x_positions[i],
                'y': y_positions[i],
                'width': 100,
                'height': 100,
                'image': OBSTACLE_IMAGE
            }
            if i % 5 == 2:
                # Every 5th platform is moving
                platform['moving'] = True
                platform['move_range'] = 200
                platform['speed'] = 2
            platform_data.append(platform)
        for i in range(5):
            platformie = {'x': 17*300 + 70*i,
                    'y': 500 - 70*i,
                    'width': 100,
                    'height': 100,
                    'image': OBSTACLE_IMAGE}
            platform_data.append(platformie)
            flower = {'x': 17*300 + 70*5,
                    'y': 150,
                    'width': 10,
                    'height': 10,
                    'image': FLOWER}

    elif index == 1:
        # Level 2: City Sewer
        platform_data = []
        x_positions = [300 + i * 400 for i in range(24)]  # 24 platforms, spacing of 400
        y_positions = [500 - (i % 8) * 50 for i in range(24)]  # Vary y positions
        for i in range(24):
            platform = {
                'x': x_positions[i],
                'y': y_positions[i],
                'width': 150,
                'height': 100,
                'image': OBSTACLE_IMAGE
            }
            if i % 6 == 3:
                # Every 6th platform is moving
                platform['moving'] = True
                platform['move_range'] = 300
                platform['speed'] = 3
            platform_data.append(platform)

    elif index == 2:
        # Level 3: Polluted River
        platform_data = []
        x_positions = [300 + i * 500 for i in range(18)]  # 18 platforms, spacing of 500
        y_positions = [500 - (i % 6) * 50 for i in range(18)]  # Vary y positions
        for i in range(18):
            platform = {
                'x': x_positions[i],
                'y': y_positions[i],
                'width': 200,
                'height': 100,
                'image': OBSTACLE_IMAGE
            }
            if i % 4 == 2:
                # Every 4th platform is moving
                platform['moving'] = True
                platform['move_range'] = 400
                platform['speed'] = 4
            platform_data.append(platform)
    else:
        platform_data = []

    return Level(BACKGROUND_IMAGES[index], platform_data, ground_level)

def create_cutscene(index):
    characters = [
        [{'image': DUCK_IMAGE_1, 'position': (200, 200), 'size': (200, 200)}],
        [{'image': DUCK_IMAGE_2, 'position': (200, 200), 'size': (100, 100)}],
        [{'image': DUCK_IMAGE_3, 'position': (200, 200), 'size': (100, 100)}],
    ]
    # Assume THE_DUCK_IMAGE is defined in settings.py for the final duck image
    final_duck = {'image': THE_DUCK_IMAGE, 'position': (390, 100), 'size': (400, 400)}
    return Cutscene(CUTSCENE_BACKGROUNDS[index], [characters[index][0], final_duck], CUTSCENE_DIALOGUES[index])

def end_screen(screen):
    clock = pygame.time.Clock()
    font_title = pygame.font.Font(None, 72)
    font_text = pygame.font.Font(None, 48)
    title = font_title.render("Thank You for Playing!", True, (255, 255, 0))
    credits = [
        "Game Developer: Zane",
        "Graphics Designer: Jennie Wiley",
        "Music: Jennie Wiley",
        "Special Thanks: Noah and Lu",
        "Press any button to exit."
    ]
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)))
        for idx, line in enumerate(credits):
            text_surface = font_text.render(line, True, (255, 255, 255))
            rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + idx * 50))
            screen.blit(text_surface, rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
                running = False
        clock.tick(FPS)

def handle_input(duck, joystick):
    keys = pygame.key.get_pressed()
    if joystick:
        # Joystick input
        if joystick.get_button(1):  # Move Left
            duck.move(-1)
        elif joystick.get_button(0):  # Move Right
            duck.move(1)
        else:
            duck.stop()
        if joystick.get_button(5):  # Jump
            duck.jump()
    else:
        # Keyboard input
        if keys[pygame.K_LEFT]:
            duck.move(-1)
        elif keys[pygame.K_RIGHT]:
            duck.move(1)
        else:
            duck.stop()
        if keys[pygame.K_SPACE]:
            duck.jump()

            
if __name__ == "__main__":
    main()
