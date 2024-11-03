import pygame

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Check if any joysticks are connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)  # Assuming the first joystick
    joystick.init()
    print(f"Controller: {joystick.get_name} connected.")
else:
    print("No controller detected.")
    pygame.quit()
    exit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect button presses
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")

        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")

        # Detect axis movement (like joysticks)
        elif event.type == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value  # Ranges from -1 to 1
            print(f"Axis {axis} moved to {value}")

    # Update screen if necessary
    # pygame.display.flip()

# Quit Pygame
pygame.quit()
