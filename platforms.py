# Moduł do obsługi platform
import pygame
from pygame.sprite import Sprite


class Platform(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/Seasonal_Tilesets/AutumnForest/Background/Bottom_leaf_piles_sm.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

