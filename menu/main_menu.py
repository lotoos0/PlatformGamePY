import pygame
import pygame.mixer
import sys
from game import Game
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, FONT_HALEAH_FAT, TRANSPARENT, SILVER, GAME_VERSION
from menu.button import Button

pygame.init()

pygame.mixer.music.load('assets/sounds/8bit_Nostalgia.mp3')
pygame.mixer.music.play(-1)

background_images = [
    pygame.image.load('assets/images/Seasonal_Tilesets/AutumnForest/Background/_Complete_static_BG.png'),
    pygame.image.load(('assets/images/Seasonal_Tilesets/Grassland/Background/_Complete_static_BG.png')),
    pygame.image.load(('assets/images/Seasonal_Tilesets/Tropics/Background/_Complete_static_BG.png')),
    pygame.image.load(('assets/images/Seasonal_Tilesets/Winter_World/Background/_Complete_static_BG.png'))
]
current_background = 0  # current background.. :P
change_background_event = pygame.USEREVENT + 1

# BTN MAIN MENU
play_button = Button(SCREEN_WIDTH // 2 - 100, 200, 200, 50, "Play", TRANSPARENT, (SILVER))
level_button = Button(SCREEN_WIDTH // 2 - 100, 250, 200, 50, "Pick Level", TRANSPARENT, (SILVER))
settings_button = Button(SCREEN_WIDTH // 2 - 100, 300, 200, 50, "Settings", TRANSPARENT, (SILVER))
exit_button = Button(SCREEN_WIDTH // 2 - 100, 350, 200, 50, "Exit Game", TRANSPARENT, (SILVER))

# BTN SETTINGS MENU
video_button = Button(SCREEN_WIDTH // 2 - 100, 200, 200, 50, "Video", TRANSPARENT, (SILVER))
audio_button = Button(SCREEN_WIDTH // 2 - 100, 250, 200, 50, "Audio", TRANSPARENT, (SILVER))
keyboard_button = Button(SCREEN_WIDTH // 2 - 100, 300, 200, 50, "Keyboard", TRANSPARENT, (SILVER))
game_button = Button(SCREEN_WIDTH // 2 - 100, 350, 200, 50, "Game", TRANSPARENT, (SILVER))

menu_main_buttons = [play_button, level_button, settings_button, exit_button]
menu_settings_buttons = [video_button, audio_button, keyboard_button, game_button]

def change_background():
    global current_background
    current_background = (current_background + 1) % len(background_images)

def draw_background(screen, background_images):
    background = pygame.transform.scale(background_images[current_background], (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0, 0))

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mrok MENU")

    clock = pygame.time.Clock()
    pygame.time.set_timer(change_background_event, 15000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == change_background_event:
                change_background()

            for button in menu_main_buttons:
                button.handle_event(event)

            if play_button.is_clicked:
                pygame.mixer.music.stop()
                game_state = Game()
                game_state.run()
                play_button.is_clicked = False

            if level_button.is_clicked:
                print("Pick level CLICK!")
                level_button.is_clicked = False

            if settings_button.is_clicked:
                print("SETTINGS CLICK!")
                settings_button.is_clicked = False
                settings_menu(screen, background_images, event)

            if exit_button.is_clicked:
                pygame.quit()
                sys.exit()

        draw_background(screen, background_images)
        for button in menu_main_buttons:
            button.draw(screen)
            button.check_hover(pygame.mouse.get_pos())

        font = pygame.font.Font(FONT_HALEAH_FAT, 56)
        text = font.render("Main Menu", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100))

        version_font = pygame.font.Font(FONT_HALEAH_FAT, 24)
        version_text = version_font.render(GAME_VERSION, True, BLACK)
        screen.blit(version_text, (SCREEN_WIDTH - version_text.get_width() - 10, SCREEN_HEIGHT - version_text.get_height() - 10))

        pygame.display.flip()
        clock.tick(60)


def settings_menu(screen, background_images, event):
    pygame.display.set_caption("Mrok Settings Menu")

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_background(screen, background_images)

        for button in menu_settings_buttons:
            button.handle_event(event)
            button.draw(screen)
            button.check_hover(pygame.mouse.get_pos())

