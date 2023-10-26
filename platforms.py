# Moduł do obsługi platform
import pygame
from pygame.sprite import Sprite


class ClassicPlatform(Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.platform_image = pygame.image.load("assets/images/Platforms/blue_back_teleport_platform.png")

        self.image = self.platform_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class GravityPlatform(Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("assets/images/Platforms/violet_platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collide_with_player(self, player):
        if self.rect.colliderect(player.rect):
            if player.vel.y > 0:
                player.pos.y = self.rect.top - player.rect.height
                player.vel.y = 0


            return True
        return False