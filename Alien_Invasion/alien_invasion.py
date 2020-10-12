import sys
import pygame
from settings import Settings
from armour import Armour 
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialise the game and create  game resources"""
        pygame.init()

        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height

        #can change to windowed mode, to be placed in options menu later
        #self.screen = pygame.display.set_mode(
        #   (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("AlienInvasion")

        self.armour = Armour(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.armour.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """respond to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            #move the armour to the right
            self.armour.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move armour to left
            self.armour.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.armour.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.armour.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """updatate position of bullets and get rid of old bullets"""
        #update bullet positions.
        self.bullets.update()
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        #check for bullet collisions, removing aliens and bullets that collide
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """create a fleet of aliens"""
        #make an alien and find the number of aliens in a row
        #spacing between aliens = width of one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen
        armour_height = self.armour.rect.height
        available_space_y = (self.settings.screen_height - 
            (5 * alien_height) - armour_height)
        number_rows = available_space_y // (2 * alien_height)

        #create full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond appropriately to aliens reaching edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop entire fleet and change direction of the fleet"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """check for reaching edges and update positions of aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """Update image on screen, flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.armour.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #make most recent drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()