import pygame.font

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialise scoring attribs"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings for scoring information
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #prepare initial score images
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = ("Current Score: " + "{:,}".format(rounded_score))
        self.score_image = self.font.render(score_str, True,
                self.text_colour, self.settings.bg_colour)

        #display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = ("High Score: " + "{:,}".format(high_score))
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_colour, self.settings.bg_colour)

        #center high score at top of screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def check_high_score(self):
        """Check for new high scores"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)