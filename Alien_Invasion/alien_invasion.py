import sys
import pygame
from settings import Settings
from armour import Armour 

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialise the game and create  game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("AlienInvasion")

        self.armour = Armour(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.armour.update()
            self._update_screen()


    def _check_events(self):
        """respond to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the armour to the right
                    self.armour.moving_right = True
                elif event.key == pygame.K_LEFT:
                    #move armour to left
                    self.armour.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.armour.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.armour.moving_left = False

    def _update_screen(self):
        """Update image on screen, flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.armour.blitme()

        #make most recent drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()