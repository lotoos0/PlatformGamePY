import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_HALEAH_FAT, BLACK

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, transparent_color=(0, 0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.transparent_color = transparent_color
        self.is_hovered = False
        self.is_clicked = False

        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surface.fill(transparent_color)

    def draw(self, screen):
        if self.is_hovered:
            pygame.draw.rect(self.surface, self.hover_color, (0, 0, self.width, self.height))
        else:
            pygame.draw.rect(self.surface, self.color, (0, 0, self.width, self.height))

        font = pygame.font.Font(FONT_HALEAH_FAT, 36)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width // 2, self.height // 2)
        self.surface.blit(text_surface, text_rect)

        screen.blit(self.surface, (self.x, self.y))

    def check_hover(self, mouse_pos):
        x, y = mouse_pos
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.is_hovered = True
        else:
            self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                self.is_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_clicked = False
