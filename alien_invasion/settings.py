class Settings():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (255, 255, 255)
        self.ship_speed = 0.5
        self.ship_limit = 3
        self.bullet_speed = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 0.1
        self.fleet_drop_speed = 40
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
