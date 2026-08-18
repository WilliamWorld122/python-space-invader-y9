import pygame, random
# Making the Alien
class Alien(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        # Loading image
        path = f"Graphics/alien_{type}.png"
        self.image = pygame.image.load(path)
        # Alien's collision rect
        self.rect = self.image.get_rect(topleft = (x, y))
    def update(self,direction):
        # Movement 
        self.rect.x += direction
# Making the mystery ship
class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width, offset):
        super().__init__()
        # Initialising it
        self.screen_width = screen_width
        self.offset = offset
        self.image = pygame.image.load("Graphics/mystery.png")
        x = random.choice([self.offset /2, screen_width + self.offset - self.image.get_width()])
        # Speed changes by hitting sides
        if x == self.offset / 2:
            self.speed = 3
        else: 
            self.speed = -3

        self.rect = self.image.get_rect(topleft  = (x, 90))
    def update(self):
        # collisions and movement
        self.rect.x += self.speed
        if self.rect.right > self.screen_width + self.offset /2:
            self.kill()
        elif self.rect.left < self.offset /2:
            self.kill()