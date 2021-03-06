class Settings:
    """ Class for storage all game settings """

    def __init__(self):
        """ Static settings initialisation """
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 30)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 4

        # alien settings
        self.fleet_drop_speed = 10

        # New speed in new level
        self.speedup_scale = 1.1
        # Scaling price for alien in new level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Dynamic settings initialization """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5
        # fleet_direction = 1 means moving right, -1 moving left
        self.fleet_direction = 1
        # Points for one alien
        self.alien_points = 50

    def increase_speed(self):
        """ Increasing speed settings and points by alien """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

