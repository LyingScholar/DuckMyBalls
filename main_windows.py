# main_emulator.py

import pygame
from settings import *
import main  # Import the original main module

def emulate_joystick_events():
    # Map keyboard keys to joystick buttons
    key_to_button = {
        pygame.K_SPACE: 5,    # Jump
        pygame.K_LEFT: 1,     # Move Left
        pygame.K_RIGHT: 0,    # Move Right
        pygame.K_ESCAPE: 2,   # Exit or Back
        pygame.K_UP: 1,       # Menu Navigate Up
        pygame.K_DOWN: 7,     # Menu Navigate Down
        pygame.K_RETURN: 0,   # Select
        # Add additional mappings if needed
        pygame.K_a: 3,        # Decrease Volume
        pygame.K_d: 4,        # Increase Volume
    }

    # Create a fake joystick class
    class FakeJoystick:
        def __init__(self):
            self.buttons = [0] * 12  # Assume 12 buttons

        def get_button(self, button_id):
            return self.buttons[button_id]

        def get_name(self):
            return "Emulated Joystick"

        def init(self):
            pass

    # Replace pygame's joystick functions with our fake joystick
    pygame.joystick.get_count = lambda: 1
    pygame.joystick.Joystick = lambda x: fake_joystick

    # Initialize Pygame and joystick
    pygame.init()
    pygame.joystick.init()
    fake_joystick = FakeJoystick()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick detected: {joystick.get_name()}")

    # Store the original pygame.event.get function
    original_pygame_event_get = pygame.event.get

    # Define event_get_wrapper to inject joystick events
    def event_get_wrapper():
        events = original_pygame_event_get()
        new_events = []

        for event in events:
            # Handle quit event
            if event.type == pygame.QUIT:
                new_events.append(event)
                continue
    
            # Handle keyboard events
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key = event.key
                if key in key_to_button:
                    # Create a corresponding joystick event
                    button = key_to_button[key]
                    joy_event_type = pygame.JOYBUTTONDOWN if event.type == pygame.KEYDOWN else pygame.JOYBUTTONUP
                    joy_event = pygame.event.Event(joy_event_type, {'joy': 0, 'button': button})
                    new_events.append(joy_event)

                    # Update joystick button state
                    fake_joystick.buttons[button] = 1 if event.type == pygame.KEYDOWN else 0
                else:
                    # Keep other keyboard events (if any)
                    new_events.append(event)
            else:
                # Keep other events
                new_events.append(event)
        return new_events

    # Monkey-patch pygame.event.get
    pygame.event.get = event_get_wrapper

    # Run the original main function
    main.main()

if __name__ == "__main__":
    emulate_joystick_events()
