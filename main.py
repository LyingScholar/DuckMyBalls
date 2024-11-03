# main.py
import pygame
from settings import *
from duck import Duck
from level import FlowerField, CitySewer, PollutedRiver
from game_menu import Menu
from cutscene import Cutscene
from cutscene2 import cutscene2

def main():
    pygame.init()
    pygame.joystick.init()
    pygame.font.init()  # Initialize font module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("P Ducky")
    clock = pygame.time.Clock()

    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick detected: {joystick.get_name()}")
    else:
        print("No joystick detected.")
    # Initialize game components
    menu = Menu()
    cutscene = Cutscene()
    duck = Duck(100, 500)
    levels = [FlowerField(), CitySewer(), PollutedRiver()]
    current_level_index = 0
    current_level = levels[current_level_index]
    dialogue = None

    # Camera offset
    camera_x = 0

    # Game states
    running = True
    playing = False

    # Menu loop
    action = menu.run(screen)
    if action == "exit":
        running = False
    else:
        # Run cutscene before starting the game
        cutscene_action = cutscene.run(screen)
        if cutscene_action == "exit":
            running = False
        else:
            playing = True

    # Main game loop
    while running:
        if playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_LEFT:
                        duck.move_left()
                    if event.key == KEY_RIGHT:
                        duck.move_right()
                    if event.key == KEY_JUMP:
                        duck.jump()
                    if event.key == pygame.K_SPACE and dialogue and dialogue.is_active:
                        dialogue.skip()
                if event.type == pygame.KEYUP:
                    if event.key == KEY_LEFT or event.key == KEY_RIGHT:
                        duck.stop()

                # Handle joystick input
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.joy == joystick.get_id():
                        if event.button == 1:  # Button 1 on controller
                            duck.move_right()
                        if event.button == 0:  # Button 2 on controller
                            duck.jump()
                        if event.button == 3:  # Button 3 on controller
                            duck.move_left()
                        if dialogue and dialogue.is_active:
                            dialogue.skip()
                if event.type == pygame.JOYBUTTONUP:
                    if event.joy == joystick.get_id():
                        if event.button == 0 or event.button == 2:
                            duck.stop()
            if joystick:
            # Check buttons
                buttons = joystick.get_button()
                # Reset movement
                duck.stop()
                if buttons[0]:  # Button 1 pressed
                    duck.move_right()
                if buttons[2]:  # Button 3 pressed
                    duck.move_left()
                if buttons[1]:  # Button 2 pressed
                    duck.jump()
                # Handle dialogue skipping
                if buttons[0] or buttons[1] or buttons[2]:
                    if dialogue and dialogue.is_active:
                        dialogue.skip()


            # Update game objects
            duck.update(current_level.platforms.sprites() + current_level.ground.sprites())
            if dialogue and dialogue.is_active:
                dialogue.update()
            current_level.update(duck)

            # Update camera position
            camera_x = duck.rect.x - SCREEN_WIDTH // 2
            if camera_x < 0:
                camera_x = 0
            elif camera_x > current_level.level_width - SCREEN_WIDTH:
                camera_x = current_level.level_width - SCREEN_WIDTH

            # Prevent duck from moving beyond level boundaries
            if duck.rect.x < 0:
                duck.rect.x = 0
            elif duck.rect.x > current_level.level_width - duck.rect.width:
                duck.rect.x = current_level.level_width - duck.rect.width

            # Drawing
            current_level.draw(screen, camera_x)
            duck.draw(screen, camera_x)
            if dialogue and dialogue.is_active:
                dialogue.draw(screen)
            pygame.display.flip()

            # Check for level completion
            if duck.rect.x >= current_level.level_width - duck.rect.width:
                current_level_index += 1

                if current_level_index < len(levels):
                    current_level = levels[current_level_index]
                    duck.rect.x = 100
                    duck.rect.y = 500
                    dialogue = None  # Reset dialogue for the new level if needed
                    
                    cutscene_action = cutscene2.run(screen)
                    if cutscene_action == "exit":
                        running = False
                    else:
                        playing = True

                else:
                    # End of the game
                    playing = False
                    # Display end scene or credits
            clock.tick(FPS)
        else:
            # Show end scene or return to menu
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
