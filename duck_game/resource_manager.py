#resource_manager.py
import pygame
from .settings import *

class ResourceManager:
    _images = {}

    @classmethod
    def load_image(cls, path, size=None):
        """Load and cache images to avoid redundant loading."""
        key = (path, size)
        if key not in cls._images:
            image = pygame.image.load(path).convert_alpha()
            if size:
                image = pygame.transform.scale(image, size)
            cls._images[key] = image
        return cls._images[key]
