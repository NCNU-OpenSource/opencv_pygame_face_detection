import pygame
import cv2
import os
import datetime

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

# 標題
pygame.display.set_caption("卡個位閃邊去")

# Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

num_faces = 0

img_folder = 'webcam_pics'
if not os.path.exists(img_folder):
    os.mkdir(img_folder)

# 初始畫面
font = pygame.font.Font('chinese.ttf', 48)
start_button = pygame.Rect(220, 200, 200, 50)
start_text = font.render('Start', True, (0, 0, 0))
exit_button = pygame.Rect(220, 300, 200, 50)
exit_text = font.render('Exit', True, (0, 0, 0))

font_title = pygame.font.Font('chinese.ttf', 64)
title_text = font_title.render('卡個位閃邊去', True, (0, 0, 0))

run = True
game_started = False
while run:
    if not game_started:
        screen.fill((255, 255, 255))  # 白色背景
        text_rect_title = title_text.get_rect(center=(320, 100))
        screen.blit(title_text, text_rect_title)
        pygame.draw.rect(screen, (0, 0, 255), start_button)
        text_rect_start = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, text_rect_start)
        pygame.draw.rect(screen, (0, 0, 255), exit_button)
        text_rect_exit = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, text_rect_exit)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            game_started = False  # 確保攝像頭迴圈也會停止
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            if start_button.collidepoint(event.pos):
                game_started = True
            elif exit_button.collidepoint(event.pos):
                run = False
                game_started = False  # 確保攝像頭迴圈也會停止

    if game_started:
        cap = cv2.VideoCapture(0)
        while game_started:
            ret, frame = cap.read()
            h, w = frame.shape[:2]

            if not ret:
                print("Error getting frame from webcam")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            num_faces = face_cascade.detectMultiScale(gray)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            pygame_frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "BGR")
            screen.blit(pygame_frame, (0, 0))
            pygame.display.flip()

            now = datetime.datetime.now()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        if frame is None:
                            print("Error, no webcam frame to save")
                        else:
                            filename = now.strftime('%Y%m%d_%H%M%S') + '.jpg'
                            img_path = os.path.join(img_folder, filename)
                            number_faces = len(num_faces)
                            print(f"Number of faces detected: {number_faces}")
                            cv2.imwrite(img_path, frame)
                            print("picture taken sucess \n " + img_path)

                            for (x, y, w, h) in faces:
                                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                face_roi = frame[y:y + h, x:x + w]
                                filename = now.strftime('%Y%m%d_%H%M%S') + '_cropped.jpg'
                                img_path = os.path.join(img_folder, filename)
                                cv2.imwrite(img_path, face_roi)
                                print("cropped image saved \n " + img_path)

                            game_started = False  # 停止遊戲循環
                            break  # 確保在退出後停止遊戲循環

            if not run:  # 確認是否要退出外層迴圈
                break

        cap.release()

pygame.quit()
