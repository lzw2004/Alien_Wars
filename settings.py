class Settings:
	"""储存《外星人入侵》中所有设置的类"""

	def __init__(self):
		"""初始化游戏设置"""
		# 屏幕设置
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# 飞船设置
		self.ship_speed = 1.5
		self.ship_limit = 3

		# 子弹设置
		self.bullet_speed = 3.0  # 子弹的速度
		self.bullet_width = 3 # 子弹的宽  3
		self.bullet_height = 15  # 子弹的高
		self.bullets_allowed = 10  # 限制子弹数量
		self.bullet_color = (60, 60, 60)  # 子弹的颜色

		# 外星人设置
		self.alien_speed = 1.0  # 外星人移动速度
		self.fleet_drop_speed = 10
		# fleet_direction 表示向右移，为-1表示向左移
		self.fleet_direction = 1

		# 加快游戏节奏
		self.speedup_scale = 1
		# 外星人分数的提高速度
		self.score_scale = 1.5

		self.initialize_dunamic_steeings()

	def initialize_dunamic_steeings(self):
		"""初始化随游戏进行然变化的设置"""
		self.ship_speed = 1.5	
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# fleet_direction 为1表示向右，为-1表示向左
		self.fleet_direction = 1

		# 记分
		self.alien_points = 50

	def increase_speed(self):
		"""提高速度设置和外星人分数"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)