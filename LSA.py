import pygame
import random
import cv2
import os
import sys
import datetime
FPS = 60
WIDTH = 640
HEIGHT = 480

WHITE =(255, 255, 255)

# 初始化 Pygame、建立視窗
pygame.init()
screen = pygame.display.set_mode((640,480)) 

# Open webcam
cap = cv2.VideoCapture(0)

# Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

num_faces = 0

run = True
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



# 遊戲迴圈
show_init = True
running = True
while run:
    
    # Read frame from webcam
    ret, frame = cap.read()

    h, w = frame.shape[:2] 
    #print(f"Frame: ({w} x {h})")

    if not ret:
        print("Error getting frame from webcam")
    # OpenCV image processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    num_faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 

    # Convert to Pygame surface and display    
    pygame_frame = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1],"BGR")
    screen.blit(pygame_frame, (0,0))
    pygame.display.flip()


    img_folder = 'webcam_pics'
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    now = datetime.datetime.now()

    # Check events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # Capture image with faces marked 
                if frame is None:
                    print("Error, no webcam frame to save")
                else: 
                    filename = now.strftime('%Y%m%d_%H%M%S') + '.jpg' 
                    img_path = os.path.join(img_folder, filename)  
                    number_faces = len(num_faces)
                    print(f"Number of faces detected: {number_faces}")
                    cv2.imwrite(img_path,frame)
                    print("picture taken sucess \n "+img_path)

                    #cropped
                    for (x, y, w, h) in faces:
                        # Draw rectangle on full frame
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        # Extract face ROI 
                        face_roi = frame[y:y+h, x:x+w]
                        # Save cropped face image
                        filename = now.strftime('%Y%m%d_%H%M%S') + '_cropped.jpg' 
                        img_path = os.path.join(img_folder, filename)  
                        cv2.imwrite(img_path, face_roi)
                        print("cropped image saved \n "+img_path)

while running:
#    if show_init:
#        draw_init()
#       show_init=False
    clock.tick(FPS)
#取得輸入
#    for event in pygame.event.get():
#        if event.type ==pygame.QUIT:
#           running = False

    pygame.display.update()

pygame.quit()
sys.exit()  # 確保程式完全退出
