import pygame
import random

# 初始化 Pygame
pygame.init()

# 視窗大小
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("緩慢移動的中空方塊")

# 色彩
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 方塊資訊
block_width, block_height = 450, 360
block_x = random.randint(0, WIDTH - block_width)
block_y = random.randint(0, HEIGHT - block_height)
block_speed = 0.05  # 更慢的移動速度

# 隨機移動方向
dx = random.choice([-1, 1]) * block_speed
dy = random.choice([-1, 1]) * block_speed

# 遊戲主迴圈
run = True
while run:
    # 檢查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 更新方塊位置
    block_x += dx
    block_y += dy

    # 碰撞邊界時改變移動方向
    if block_x <= 0 or block_x + block_width >= WIDTH:
        dx *= -1
    if block_y <= 0 or block_y + block_height >= HEIGHT:
        dy *= -1

    # 清空畫面
    win.fill(WHITE)

    # 繪製中空方塊
    pygame.draw.rect(win, GREEN, (block_x, block_y, block_width, block_height), 2)

    # 更新畫面
    pygame.display.update()

# 關閉 Pygame
pygame.quit()
