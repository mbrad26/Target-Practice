class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (0, 200, 255)

        self.target_speed = .1
        self.ship_speed = 1.5
        self.bullet_speed = 1.5

        self.change_direction = 1
        self.bullets_allowed = 2

        self.start_game = False
        self.draw_button = True

        self.game_score = 0
        self.missed = 5