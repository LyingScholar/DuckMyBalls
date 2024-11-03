# main.py
import pygame
from settings import *
from duck import Duck
from level import FlowerField, CitySewer, PollutedRiver
from game_menu import Menu
from cutscene1 import Cutscene1
from cutscene2 import Cutscene2
from cutscene3 import Cutscene3

def main():
    pygame.init()
    pygame.joystick.init()
    pygame.font.init()  # Initialize font module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("P Ducky")
    clock = pygame.time.Clock()

    # Initialize joystick
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick detected: {joystick.get_name()}")
        num_buttons = joystick.get_numbuttons()
        print(f"Number of buttons: {num_buttons}")
        for i in range(num_buttons):
            print(f"Button {i}")
    else:
        print("No joystick detected.")

    # Initialize game components
    menu = Menu()
    duck = Duck(100, 500)
    levels = [FlowerField(), CitySewer(), PollutedRiver()]
    cutscenes = [Cutscene1(), Cutscene2(),Cutscene3]

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
                cutscene_action = cutscenes[0].run(screen)
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
                        duck.jump_pressed = True
                    if event.key == pygame.K_SPACE and dialogue and dialogue.is_active:
                        dialogue.skip()
                if event.type == pygame.KEYUP:
                    if event.key == KEY_LEFT or event.key == KEY_RIGHT:
                        duck.stop()
                    if event.key == KEY_JUMP:
                        duck.jump_pressed = False

                # Handle joystick button events for debugging
                if event.type == pygame.JOYBUTTONDOWN:
                    print(f"Joystick button {event.button} down")
                if event.type == pygame.JOYBUTTONUP:
                    print(f"Joystick button {event.button} up")

            # Poll joystick input
            if joystick:
                num_buttons = joystick.get_numbuttons()
                buttons = [joystick.get_button(i) for i in range(num_buttons)]
                # Reset horizontal movement
                duck.stop()
                if buttons[1]:  # Adjust indices based on your testing
                    duck.move_right()
                if buttons[3]:
                    duck.move_left()
                # Update jump_pressed state
                duck.jump_pressed = buttons[0]  # Assuming button 0 is the jump button
                # Handle dialogue skipping
                if any(buttons):
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
                # Level completed
                # Run post-level cutscenes
                if current_level_index < len(cutscenes):
                    # Play the cutscene of the previous duck
                    cutscene_action = cutscenes[current_level_index].run(screen)
                    if cutscene_action == "exit":
                        running = False
                        return
                    # Immediately proceed to the next cutscene (if any)
                    if current_level_index + 1 < len(cutscenes):
                        cutscene_action = cutscenes[current_level_index + 1].run(screen)
                        if cutscene_action == "exit":
                            running = False
                            return

                # Prepare for next level
                current_level_index += 1
                if current_level_index < len(levels):
                    current_level = levels[current_level_index]
                    duck.rect.x = 100
                    duck.rect.y = 500
                    dialogue = None  # Reset dialogue for the new level if needed
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
