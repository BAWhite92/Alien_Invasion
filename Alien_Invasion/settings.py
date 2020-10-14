class Settings:
    """A class for all settings within Alien Invasion game"""

    def __init__(self):
        """initialise the game's static settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (96, 96, 96)

        #armour settings
        self.armour_limit = 2

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (247, 255, 0)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 20

        #how quickly the game speeds up
        self.speedup_scale = 1.25
        #how quickly the alien points values increase
        self.score_scale = 1.2

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout game"""
        self.armour_speed = 1.2
        self.bullet_speed = 2.0
        self.alien_speed = 1.0
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and aliens points value"""
        self.armour_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
