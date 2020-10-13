class GameStats:
    """Track stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Initial statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #start Alien Invasion in active state
        self.game_active = False

    def reset_stats(self):
        """Intialise statistics that can change during game"""
        self.armour_left = self.settings.armour_limit