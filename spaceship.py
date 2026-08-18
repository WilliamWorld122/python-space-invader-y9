import pygame
from laser import Laser
# The spaceship character
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height, offset):
        # Building spaceship
        super().__init__()
        self.offset = offset
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = self.image.get_rect(midbottom = (self.screen_width / 2, self.screen_height))
        self.speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300
        # Sound of the laser
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")
    def get_user_input(self):
        # movement by keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center,5,self.screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()
    def update(self):
        # Update everything
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()
    def constrain_movement(self):
        # Limit spaceship movement
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < self.offset:
            self.rect.left = self.offset
    def recharge_laser(self):
        # Laser delay
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
    def reset(self):
        # Reset player
        self.rect = self.image.get_rect(midbottom = (self.screen_width / 2, self.screen_height))
        self.lasers_group.empty()