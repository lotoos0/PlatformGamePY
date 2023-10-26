import pygame
from menu.main_menu import *
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mrok")

if __name__ == "__main__":
    main_menu()


pygame.quit()
