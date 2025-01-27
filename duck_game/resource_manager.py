# duck_game/resource_manager.py
import pygame

class ResourceManager:
    _images = {}

    @classmethod
    def load_image(cls, path, size=None):
        if isinstance(path, pygame.Surface):
            image = path
            if size:
                image = pygame.transform.scale(image, size)
            return image
        key = (path, size)
        if key not in cls._images:
            try:
                image = pygame.image.load(path).convert_alpha()  # Use convert_alpha()
            except pygame.error as e:
                print(f"Error loading image {path}: {e}")
                raise
            if size:
                image = pygame.transform.scale(image, size)
            cls._images[key] = image
        return cls._images[key]
