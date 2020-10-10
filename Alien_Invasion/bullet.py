import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the armour"""
    def __init__(self, ai_game):
        """create bullet object at the armour's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        #create a bullet rect at (0,0) and then set correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.armour.rect.midtop

        #store the bullet's position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen"""
        #update decimal pos of bullet
        self.y -= self.settings.bullet_speed
        #update the rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)