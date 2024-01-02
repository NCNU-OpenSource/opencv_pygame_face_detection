import pygame
import random
import os
import sys

FPS = 60
WIDTH = 640
HEIGHT = 480

WHITE =(255, 255, 255)

# 初始化 Pygame、建立視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 指定字體檔案路徑
font_name = os.path.join(os.path.dirname(__file__), 'chinese.ttf')



def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_init():
    draw_text(screen, "卡個位閃邊去", 50, WIDTH/ 2, HEIGHT / 4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # 當使用者按下關閉視窗，直接離開程式
            elif event.type == pygame.KEYUP:
                waiting = False

show_init = True
running = True

# 遊戲迴圈
while running:
    if show_init:
        draw_init()
        show_init = False

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()  # 確保程式完全退出
