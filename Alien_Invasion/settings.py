class Settings:
    """A class for all settings within Alien Invasion game"""

    def __init__(self):
        """initialise game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (96, 96, 96)

        #armour settings
        self.armour_speed = 2.5

        #bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (247, 255, 0)
        self.bullets_allowed = 8

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 15
        #fleet_direction fo 1 represents right; -1 represents left
        self.fleet_direction = 1