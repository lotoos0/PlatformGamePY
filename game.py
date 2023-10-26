import pygame
import pygame.mixer
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_HALEAH_FAT
from player import Player
from platforms import Platform


class Game:
    def __init__(self):

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def update(self):
        for sprite in self.all_sprites:
            sprite.update()

    def draw(self):
        self.screen.fill((0, 0, 1))
        self.all_sprites.draw(self.screen)

        health_plus_image = pygame.image.load("assets/images/Pixel_UI/healbar/heal_plus.png")
        text_font = pygame.font.Font(FONT_HALEAH_FAT, 24)
        text_color = (255, 255, 255)
        health_text = text_font.render(f"+ {self.player.health_text}", True, text_color)

        hp_plus_x, hp_plus_y = SCREEN_WIDTH - 100, 20
        hp_text_x, hp_text_y = SCREEN_WIDTH - 60, 20

        #pygame.draw.rect(self.screen, (255, 0, 0), (plus_x, plus_y, 100, 30), 2)
        self.screen.blit(health_plus_image, (hp_plus_x + 2, hp_plus_y + 2))
        self.screen.blit(health_text, (hp_text_x + 2, hp_text_y + 2))

        mana_plus_image = pygame.image.load("assets/images/Pixel_UI/manabar/mana_plus.png")
        text_font = pygame.font.Font(FONT_HALEAH_FAT, 24)
        text_color = (255, 255, 255)
        mana_text = text_font.render(f"+ {self.player.mana_text}", True, text_color)

        mana_plus_x, mana_plus_y = SCREEN_WIDTH - 200, 20
        mana_text_x, mana_text_y = SCREEN_WIDTH - 160, 20

        self.screen.blit(mana_plus_image, (mana_plus_x + 2, mana_plus_y + 2))
        self.screen.blit(mana_text, (mana_text_x + 2, mana_text_y + 2))




        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.player.check_collision(self.platforms)
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
