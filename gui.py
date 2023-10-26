import pygame

class Gui:
    def __init__(self):
        self.bars_image = pygame.image.load("assets/images/Pixel_UI/04.png")
        self.healbar = None
        self.staminabar = None
        self.manabar = None

    def cut_bars(self):
        width, height = 42, 5

        self.healbar = self.bars_image.subsurface(pygame.Rect(62, 10, width, height))
        self.staminabar = self.bars_image.subsurface(pygame.Rect(62, 26, width, height))
        self.manabar = self.bars_image.subsurface(pygame.Rect(62, 42, width, height))

    def draw_bars(self, screen, x_healbar, y_healbar, x_staminabar, y_staminabar, x_manabar, y_manabar):

        screen.blit(self.healbar, (x_healbar, y_healbar))
        screen.blit(self.staminabar, (x_staminabar, y_staminabar))
        screen.blit(self.manabar, (x_manabar, y_manabar))
