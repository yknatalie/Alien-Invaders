class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.ship_speed = 0.5
        self.ship_limit = 10
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 0.01
        self.fleet_drop_speed = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = -1
