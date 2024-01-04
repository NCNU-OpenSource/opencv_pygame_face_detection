# LSA_1121_group3-卡個位閃邊去


## 動機 Motivation
- 黃聖軒同學甚麼都不做又懶散所以交不到女朋友，他希望能做一個有趣的遊戲，建立起他跟他朋友的友情，希望得到意外的愛情，因此我們想了這個遊戲，讓他在跟他的朋友聯繫感情的時候，還可以拉近他們之間的距離，讓他們貼貼。
## 玩法 Gameplay
- 所有參與玩家須擠進鏡頭裡並嘗試將對方擠出鏡頭外，一段時間後會將畫面拍下，檢查那些人不在鏡頭裡就淘汰

## 應用資源 Implementation Resources
- Pygame
- OpenCV
- chatgpt
- python

## Pygame
- 使用pygame.init()初始化Pygame
- 使用pygame.display.set_mode()創建一個窗口，設置窗口的寬度和高度。
- screen = pygame.display.set_mode((640, 480)) # 建立視窗

## OpenCV
- 使用cv2.VideoCapture(0)打開攝像頭
- cap = cv2.VideoCapture(0) # 打開攝像頭
- 使用Haar級聯分類器(cv2.CascadeClassifier)加載人臉檢測模型。
- face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

## 程式執行
- 導入需要的庫：pygame 用於遊戲開發，cv2 用於視訊處理，os 用於檔案和目錄操作，datetime 用於處理日期和時間，random 用於產生隨機數，time 用於計時
``` import pygame ```
``` import cv2 ```
``` import os ```
``` import datetime ```
``` import random ```
``` import time ```

- 初始化 Pygame 和設定視窗大小為 640x480
``` pygame.init() ```
``` screen = pygame.display.set_mode((640, 480)) ```

- 設定視窗標題為 "卡個位閃邊去"。
``` pygame.display.set_caption("卡個位閃邊去") ```

- 設定 Haar 级聯分類器用於偵測人臉，並初始化人臉數目的變數
``` face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') ```
``` num_faces = 0 ```

- 設定存放圖片的資料夾，如果該資料夾不存在，則創建一個
``` img_folder = 'webcam_pics' ```
``` if not os.path.exists(img_folder):
```        os.mkdir(img_folder) ```

- 設定 Pygame 中的按鈕和相關文字
``` font = pygame.font.Font('chinese.ttf', 48) ```
``` start_button = pygame.Rect(220, 200, 200, 50) ```
``` start_text = font.render('Start', True, (0, 0, 0)) ```
``` exit_button = pygame.Rect(220, 300, 200, 50) ```
``` exit_text = font.render('Exit', True, (0, 0, 0)) ```

- 設定遊戲標題文字
``` font_title = pygame.font.Font('chinese.ttf', 64) ```
``` title_text = font_title.render('卡個位閃邊去', True, (0, 0, 0)) ```

- 設定綠色方塊的相關變數
``` block_width, block_height = 450, 360 ```
``` block_x = random.randint(0, 640 - block_width) ```
``` block_y = random.randint(0, 480 - block_height) ```
```  block_speed_x = 1 ```
``` block_speed_y = 1 ```

- 初始化遊戲控制的變數
``` run = True ```
``` game_started = False ```
``` start_time = 0 ```
``` game_over = False ```

- 遊戲主迴圈，包含了遊戲未開始、開始和結束三種狀態的處理
``` while run: ```
```     if not game_started and not game_over: ```
```         # 初始畫面和按鈕的顯示 ```
```     for event in pygame.event.get(): ```
```         # 處理事件，例如點擊按鈕、退出遊戲等 ```
```     if game_started: ```
```         # 攝像頭迴圈 ```
```         # 顯示視訊畫面和 Pygame 的畫面 ```
```     if game_over: ```
```         # 遊戲結束後的處理 ```

- 遊戲結束後的清理和顯示畫面
``` cap.release() ```
``` screen.fill((255, 255, 255)) ```
``` # 顯示自動截的圖片和 Winner 標題 ```

- 更新 Pygame 視窗，等待 15 秒顯示遊戲結果，最後關閉 Pygame
``` pygame.display.flip()  # 更新畫面 ```
``` pygame.time.wait(15000)  # 停留15秒顯示結果 ```
``` pygame.quit() ```

## 困難及未來展望
### 困難
- OpenCV即將程式導入到樹梅派 使用上較不習慣，需要再多精進
- 將pygame跟OpenCV的程式結合一直產生bug
### 未來展望
- 希望能擴充更多功能

## 工作分配 Job Assignment
- 108213041 吳健瑋 
    - OpenCV
    - 程式撰寫
- 110213061 黃士祐 
    - ppt製作 
    - pygame
    - 程式撰寫 
- 110213062 黃聖軒
    - readme
    - OpenCV
    - 程式撰寫 
- 110213073 張瑋倫 
    - pygame
    - pygame跟OpenCV程式結合
    - 程式撰寫

## 參考資料 Reference

- https://hackmd.io/@Derek46518/HyZHsD0Qo
- https://www.youtube.com/watch?v=61eX0bFAsYs
- https://www.youtube.com/watch?v=xjrykYpaBBM
- https://itecnote.com/tecnote/python-display-cv2-videocapture-image-inside-pygame-surface/
