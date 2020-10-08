import pygame

class Armour:
    """a class to manage the defence vehicle"""

    def __init__(self, ai_game):
        """Initialise the armour and set its start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the image of the armour and get its rect
        self.image = pygame.image.load('images/armour.png')
        self.rect = self.image.get_rect()

        #start each new armour at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw armour at its current location"""
        self.screen.blit(self.image, self.rect)