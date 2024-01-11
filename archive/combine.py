import pygame
import cv2
import os
import datetime
import random
import time

# 初始化 Pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640, 480))


# 載入背景音樂
pygame.mixer.music.load('Audio Library 音樂庫 免費背景音樂下載 歌名 Marvins Dance 作者 Silent Partner 開心音樂 Happy Music .MP3')
pygame.mixer.music.play(-1)  # 播放背景音樂，-1 表示無限循環

# 標題
pygame.display.set_caption("卡個位閃邊去")

# Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

num_faces = 0

img_folder = 'webcam_pics'
if not os.path.exists(img_folder):
    os.mkdir(img_folder)

# 載入初始介面的背景圖片
initial_screen_background = pygame.image.load('th.JPEG')  # 替換為您的初始介面背景圖片路徑
initial_screen_background = pygame.transform.scale(initial_screen_background, (640, 480))  # 调整图像大小以适应屏幕    

# 初始畫面
font = pygame.font.Font('chinese.ttf', 48)
start_button = pygame.Rect(220, 200, 200, 50)
start_text = font.render('Start', True, (0, 0, 0))
exit_button = pygame.Rect(220, 300, 200, 50)
exit_text = font.render('Exit', True, (0, 0, 0))

font_title = pygame.font.Font('chinese.ttf', 64)
title_text = font_title.render('卡個位閃邊去', True, (0, 0, 0))

# 綠色方塊的相關變數
block_width, block_height = 450, 360
block_x = random.randint(0, 640 - block_width)
block_y = random.randint(0, 480 - block_height)
block_speed_x = 1
block_speed_y = 1

run = True
game_started = False
start_time = 0
game_over = False

while run:
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

    # 將初始介面背景圖片填充到整個屏幕
    screen.blit(initial_screen_background, (0, 0))     

    if not game_started and not game_over:
        text_rect_title = title_text.get_rect(center=(320, 100))
        screen.blit(title_text, text_rect_title)
        pygame.draw.rect(screen, (0, 0, 255), start_button)
        text_rect_start = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, text_rect_start)
        pygame.draw.rect(screen, (0, 0, 255), exit_button)
        text_rect_exit = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, text_rect_exit)
        pygame.display.update()

    pygame.display.flip()

    

    if game_started:
        cap = cv2.VideoCapture(0)
        start_time = time.time()
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

            # 繪製綠色方塊
            block_x += block_speed_x
            block_y += block_speed_y

            if block_x <= 0 or block_x >= 640 - block_width:
                block_speed_x *= -1
            if block_y <= 0 or block_y >= 480 - block_height:
                block_speed_y *= -1

            frame[block_y:block_y + 2, block_x:block_x + block_width] = [0, 255, 0]  # 上邊框
            frame[block_y + block_height - 2:block_y + block_height, block_x:block_x + block_width] = [0, 255, 0]  # 下邊框
            frame[block_y:block_y + block_height, block_x:block_x + 2] = [0, 255, 0]  # 左邊框
            frame[block_y:block_y + block_height, block_x + block_width - 2:block_x + block_width] = [0, 255, 0]  # 右邊框

            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= 20:
                green_box_area = frame[block_y:block_y + block_height, block_x:block_x + block_width]

                if green_box_area is not None:
                    now = datetime.datetime.now()
                    filename =  '_auto_capture.jpg'
                    img_path = os.path.join(img_folder, filename)
                    cv2.imwrite(img_path, green_box_area)
                    print("Automatic picture taken at: " + img_path)
                else:
                    print("Error, no green box area to save")

                game_started = False  # 停止遊戲循環
                game_over = True  # 遊戲結束

            # 顯示視訊畫面和 Pygame 的畫面
            pygame_frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "BGR")
            screen.blit(pygame_frame, (0, 0))
            pygame.display.flip()
            now = datetime.datetime.now()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        # 取得綠色方塊範圍內的圖片
                        green_box_area = frame[block_y:block_y + block_height, block_x:block_x + block_width]

                        if green_box_area is not None:
                            # 將圖片儲存到指定資料夾
                            now = datetime.datetime.now()
                            filename = '_green_box.jpg'
                            img_path = os.path.join(img_folder, filename)
                            cv2.imwrite(img_path, green_box_area)
                            print("Green box area image saved at: " + img_path)
                        else:
                            print("Error, no green box area to save")

                            for (x, y, w, h) in faces:
                                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                face_roi = frame[y:y + h, x:x + w]
                                filename = '_cropped.jpg'
                                img_path = os.path.join(img_folder, filename)
                                cv2.imwrite(img_path, face_roi)
                                print("cropped image saved \n " + img_path)

                            game_started = False  # 停止遊戲循環
                            break  # 確保在退出後停止遊戲循環
# 在遊戲迴圈結束後新增以下程式碼

    if game_over:  # 確認是否要退出外層迴圈
        cap.release()

        # 畫面清空
        screen.fill((255, 255, 255))

        # 顯示自動截的圖片和 Winner 標題
        img_path = 'webcam_pics/_auto_capture.jpg'  # 更換為自動截圖的路徑
        if os.path.exists(img_path):
            img = pygame.image.load(img_path)
            img_rect = img.get_rect()
            img_rect.center = (320, 240)  # 圖片置中
            screen.blit(img, img_rect)

            # 加入 Winner 標題
            font_winner = pygame.font.Font('chinese.ttf', 64)
            winner_text = font_winner.render('Winner!!!', True, (0, 0, 0))
            winner_rect = winner_text.get_rect(center=(320, 100))
            screen.blit(winner_text, winner_rect)

        pygame.display.flip()  # 更新畫面
        pygame.time.wait(15000)  # 停留15秒顯示結果
        pygame.mixer.music.stop()  # 停止背景音樂
        pygame.quit()
