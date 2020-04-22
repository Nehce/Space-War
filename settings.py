class Settings:
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 8
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 5
        # fleet_direction 为1表示向右，-1表示向左
        self.fleet_direction = 1

        # 加快节奏
        self.speedup_scale = 1.1
        # 提高奖励点数
        self.score_scale = 1.5

        self. initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 5
        self.ship_speed_factor = 8
        # fleet_direction 为1表示向右，-1表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
