# Moduł do obsługi postaci gracza
import pygame
import pygame.key
import pygame.rect
from platforms import *
from pygame.sprite import Sprite
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(Sprite):
    def __init__(self, x, y, platforms):
        super().__init__()

        self.width = 100
        self.height = 74
        self.platforms = platforms

        self.health = 100
        self.health_text = str(self.health)
        self.mana = 80
        self.mana_text = str(self.mana)
        stamina = 100
        Endurance = 0 #Wytrzymalosc np. na trucizny
        damage_default = 5  #Podstawowy dmg postaci.
        agility = 0 # Zwinność wpływa na szybkość ruchu, unikanie pułapek.
        intelligence = 0 # Wiedza może wpłynąć na zdolność do rozwiązywania zagadek lub skuteczność zaklęć.
        luck = 0 # not sure jeszcze
        reputation = 0 #moze kiedys dodac reputacje z npc

        self.image = pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-idle-00.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0

#       ATTACK THINGS
        self.attack_frames = [
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-attack1-00.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-attack1-01.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-attack1-02.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-attack1-03.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-attack1-04.png")
        ]
        self.is_attacking = False
        self.last_attack_frame_time = 0
        self.attack_frame_delay = 30

#        JUMP THINGS
        self.jump_frames = [
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-jump-00.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-jump-01.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-jump-02.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-jump-03.png")
        ]
        self.is_jumping = False
        self.jump_frame_delay = 10
        self.last_jump_frame_time = 0
        self.jump_power = -40
        self.jump_gravity = 10
#       RUNNING THINGS
        self.run_frames = [
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-run-00.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-run-01.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-run-02.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-run-03.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-run-04.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-run-05.png")
        ]
        self.is_running = False
        self.run_frame_delay = 100


#       IDLE Things
        self.idle_frames = [
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-idle-00.png"),
            pygame.image.load("assets/player/Adventurer/Individual_Sprites/adventurer-idle-01.png")
        ]
        self.current_frame = 0
        self.is_idle = False
        self.idle_frame_delay = 640
        self.facing_left = False

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.current_frame = 0

    def update_attack(self):
        if self.is_attacking:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_frame_time >= self.attack_frame_delay:
                self.current_frame += 1
            if self.current_frame >= len(self.attack_frames):
                self.is_attacking = False
                self.current_frame = 0
            self.image = pygame.transform.scale(self.attack_frames[self.current_frame], (self.width, self.height))
            self.last_attack_frame_time = current_time
            pygame.time.delay(self.attack_frame_delay)

    def update(self):
        self.check_collision(self.platforms)
        self.health_text = str(self.health)

        keys = pygame.key.get_pressed()

        move_left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        move_right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        jump = keys[pygame.K_SPACE] or keys[pygame.K_w]
        attack = keys[pygame.K_q]

        if move_left:
            self.speed_x = -30 # RUNNING SPEED
            self.is_running = True
            if not self.facing_left:
                self.idle_frames = [pygame.transform.flip(frame, True, False) for frame in self.idle_frames]
                self.run_frames = [pygame.transform.flip(frame, True, False) for frame in self.run_frames]
                self.jump_frames = [pygame.transform.flip(frame, True, False) for frame in self.jump_frames]
                self.attack_frames = [pygame.transform.flip(frame, True, False) for frame in self.attack_frames]
                self.facing_left = True
        elif move_right:
            self.speed_x = 30 # RUNNING SPEED
            self.is_running = True
            if self.facing_left:
                self.idle_frames = [pygame.transform.flip(frame, True, False) for frame in self.idle_frames]
                self.run_frames = [pygame.transform.flip(frame, True, False) for frame in self.run_frames]
                self.jump_frames = [pygame.transform.flip(frame, True, False) for frame in self.jump_frames]
                self.attack_frames = [pygame.transform.flip(frame, True, False) for frame in self.attack_frames]
                self.facing_left = False
        else:
            self.speed_x = 0
            self.is_running = False

#       ATTACK
        if attack:
            self.attack()


        #jumping
        if jump and not self.is_jumping:
            self.is_jumping = True
            self.speed_y = self.jump_power

        self.speed_y += self.jump_gravity
        self.rect.y += self.speed_y

        if self.rect.y >= SCREEN_HEIGHT - self.height:
            self.rect.y = SCREEN_HEIGHT - self.height
            self.is_jumping = False
            self.speed_y = 0

        if self.speed_x == 0:
            self.is_idle = True

        self.rect.x += self.speed_x

        if self.is_running:
            self.current_frame += 1
            if self.current_frame >= len(self.run_frames):
                self.current_frame = 0

            self.image = pygame.transform.scale(self.run_frames[self.current_frame], (self.width, self.height))
            pygame.time.delay(self.run_frame_delay)

        elif self.is_idle:
            self.current_frame += 1
            if self.current_frame >= len(self.idle_frames):
                self.current_frame = 0

            self.image = pygame.transform.scale(self.idle_frames[self.current_frame], (self.width, self.height))
            pygame.time.delay(self.idle_frame_delay)

        if self.is_jumping:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_jump_frame_time >= self.jump_frame_delay:
                self.current_frame += 1
            if self.current_frame >= len(self.jump_frames):
                self.current_frame = 0

            self.image = pygame.transform.scale(self.jump_frames[self.current_frame], (self.width, self.height))
            self.last_jump_frame_time = current_time
            pygame.time.delay(self.jump_frame_delay)

        if self.is_attacking:
            self.update_attack()

    def check_collision(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            for platform in hits:
                if self.speed_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.is_jumping = False
                    self.speed_y = 0
                elif self.speed_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.speed_y = 0
                if self.speed_x > 0:
                    self.rect.right = platform.rect.left
                elif self.speed_x < 0:
                    self.rect.left = platform.rect.right

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                    self.current_frame = 0

