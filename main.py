# main.py
import pygame
from settings import *
from duck import Duck
from dialogue import Dialogue
from level import FlowerField, CitySewer, PollutedRiver
from game_menu import Menu
from cutscene import Cutscene

def main():
    pygame.init()
    pygame.font.init()  # Initialize font module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Duck my balls")
    clock = pygame.time.Clock()

    duck = Duck(100, 500)
    levels = [FlowerField(), CitySewer(), PollutedRiver()]
    current_level_index = 0
    current_level = levels[current_level_index]
    dialogue = Dialogue(DIALOGUE_CSV)
    menu = Menu()
    cutscene = Cutscene()


    camera_x = 0

    
    # Game states
    running = True
    playing = False

    # Menu loop
    action = menu.run(screen)
    if action == "exit":
        running = False
    else:
        # Run cutscene b4 game
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
                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_LEFT:
                        duck.move_left()
                    if event.key == KEY_RIGHT:
                        duck.move_right()
                    if event.key == KEY_JUMP:
                        duck.jump()
                    if event.key == pygame.K_SPACE and dialogue.is_active:
                        dialogue.skip()
                if event.type == pygame.KEYUP:
                    if event.key == KEY_LEFT or event.key == KEY_RIGHT:
                        duck.stop()

            # Updater
            duck.update(current_level.platforms.sprites() + current_level.ground.sprites())
            if dialogue.is_active:
                dialogue.update()
            current_level.update(duck)

            # Update camera
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

            # Drawing, ignore if unsure
            current_level.draw(screen, camera_x)
            duck.draw(screen, camera_x)
            if dialogue.is_active:
                dialogue.draw(screen)
            pygame.display.flip()

            # Check for level completion
            if duck.rect.x >= current_level.level_width - duck.rect.width:
                current_level_index += 1
                if current_level_index < len(levels):
                    current_level = levels[current_level_index]
                    duck.rect.x = 100
                    duck.rect.y = 500
                    dialogue = Dialogue()  # Load new dialogues
                else:
                    # gg
                    playing = False
                    # Displaycredits
            clock.tick(FPS)
        else:
            # Show end scene or return to menu
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
