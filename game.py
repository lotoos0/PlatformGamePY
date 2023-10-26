import pygame
import pygame.mixer
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from platforms import Platform
from gui import Gui



class Game:
    x_healbar, y_healbar = 50, 50
    x_staminabar, y_staminabar = 50, 100
    x_manabar, y_manabar = 50, 150

    def __init__(self):
        self.gui = Gui()
        self.gui.cut_bars()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mrok - Game")

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.player = Player(100, 700, self.platforms)
        self.all_sprites.add(self.player)

        platform1 = Platform(200, 100)
        self.all_sprites.add(platform1)
        self.platforms.add(platform1)

        self.clock = pygame.time.Clock()
        self.is_running = True

        # Inicjalizacja zasobów gry, gracza, przeciwników itp.

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

            # Obsługa innych zdarzeń, takich jak ruch gracza, kolizje itp.

    def update(self):
        for sprite in self.all_sprites:
            sprite.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)

        self.gui.draw_bars(self.screen, self.x_healbar, self.y_healbar, self.x_staminabar, self.y_staminabar, self.x_manabar, self.y_manabar)
    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.player.check_collision(self.platforms)
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
