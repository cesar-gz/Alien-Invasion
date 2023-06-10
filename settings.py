class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 850
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 2.5
        self.ship_limit = 5

        # Bullet settings
        self.bullet_speed = 1.0
        #self.bullet_width = 3000
        self.bullet_width = 3
        self.bullet_height = 15
        # self.bullet_color = (60, 60, 60) original
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 25

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 2
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.0

        # How quickly the alien point values increase
        self.score_scale = 3.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.2
        self.bullet_speed = 1.1
        self.alien_speed = .9
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 550

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
