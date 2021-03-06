import pygame
from pygame.sprite import Sprite

class Armour(Sprite):
    """a class to manage the defence vehicle"""

    def __init__(self, ai_game):
        """Initialise the armour and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the image of the armour and get its rect
        self.image = pygame.image.load('images/armour.png')
        self.rect = self.image.get_rect()

        #start each new armour at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #movement flags
        self.moving_right = False
        self.moving_left =  False

        #store a decimal value for the armour's horizontal pos
        self.x = float(self.rect.x)

    def update(self):
        """update armour position based on movement flags using x value 
                NOT rect"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.armour_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.armour_speed

        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw armour at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_armour(self):
        """center armour on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)