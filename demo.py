import pygame
from pygame.locals import *

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))

# 设置相机位置和朝向
camera_pos = [0, 0, -5]
camera_dir = [0, 0, 1]

# 定义一个立方体的顶点坐标和连接关系
cube_vertices = [
	[-1, -1, -1],
	[-1, -1, 1],
	[-1, 1, -1],
	[-1, 1, 1],
	[1, -1, -1],
	[1, -1, 1],
	[1, 1, -1],
	[1, 1, 1]
]
cube_edges = [
	(0, 1), (0, 2), (0, 4), (1, 3),
	(1, 5), (2, 3), (2, 6), (3, 7),
	(4, 5), (4, 6), (5, 7), (6, 7)
]

# 游戏循环
running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	# 清空屏幕
	screen.fill((0, 0, 0))

	# 更新相机位置
	camera_pos[2] += 0.01  # 向前移动

	# 绘制立方体
	for edge in cube_edges:
		points = []
		for vertex in edge:
			# 计算顶点在屏幕上的坐标
			x = cube_vertices[vertex][0] - camera_pos[0]
			y = cube_vertices[vertex][1] - camera_pos[1]
			z = cube_vertices[vertex][2] - camera_pos[2]
			# 将 3D 坐标转换为屏幕坐标
			x = int(x / z * 300 + window_width / 2)
			y = int(y / z * 300 + window_height / 2)
			points.append((x, y))
		pygame.draw.line(screen, (255, 255, 255), points[0], points[1], 2)

	pygame.display.flip()

# 退出 Pygame
pygame.quit()
