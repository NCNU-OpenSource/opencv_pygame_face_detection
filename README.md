# LSA_1121_group3-卡個位閃邊去


## 動機 Motivation
- 黃am同學甚麼都不做又懶散，所以不但交不到女朋友也沒什麼朋友，他希望能做一個有趣的遊戲，建立起他跟他朋友的友情，再順帶撈一個女朋友，因此我們想了這個遊戲，讓他在跟他的朋友聯繫感情的時候，還可以拉近他們之間的距離，趁機讓他們貼貼，增加黃sam同學交到女朋友的機會。

## 玩法 Gameplay
- 所有參與玩家須擠進鏡頭裡並嘗試將對方擠出鏡頭外，一段時間後會將畫面拍下，檢查那些人不在鏡頭裡就淘汰

## 應用資源 Implementation Resources
- Pygame
- OpenCV
- chatgpt
- python
- ubuntu

## 在ubuntu要先設置的環境
- `sudo apt-get update`
- `sudo apt-get install python3-opencv`
- `sudo apt-get install python3-pip`
- `pip install pygame`

## 程式執行
- required files "bg.jpg, music.mp3, chinese.ttf, combine.py"
- `python3 combine.py` 

## Pygame
- 使用pygame.init()初始化Pygame
- 使用pygame.display.set_mode()創建一個窗口，設置窗口的寬度和高度。
- screen = pygame.display.set_mode((640, 480)) # 建立視窗

## OpenCV
- 使用cv2.VideoCapture(0)打開camera
- cap = cv2.VideoCapture(0) # 打開camera
- 使用Haar級聯分類器(cv2.CascadeClassifier)載入人臉檢測模型。
- face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

1. 導入需要的工具：pygame 用於遊戲開發，cv2 用於視訊處理，os 用於檔案和目錄操作，datetime 用於處理日期和時間，random 用於產生隨機數，time 用於計時
- ` import pygame `
- ` import cv2 `
- ` import os `
- ` import datetime `
- ` import random `
- ` import time `
  
2.載入背景音樂
- `pygame.mixer.music.load('music.MP3')`
- `pygame.mixer.music.play(-1)`
- 
3.載入初始介面的背景圖片
- `initial_screen_background = pygame.image.load('bg.JPG')`
- `initial_screen_background = pygame.transform.scale(initial_screen_background, (640, 480))`
- 
4.做一個進度條
- `def init_progressbar(screen, x, y, width, height, progress):`
- `    """Initialize the progress bar on the screen"""`
- `    pygame.draw.rect(screen, (36,120,210), (x, y, width, height), 0)`
- `    progress_width = int(progress * width)`
- `    pygame.draw.rect(screen, (255,255,255), (x, y, progress_width, height))`

- `def update_progressbar(screen, x, y, width, height, progress):`
- `    """Update the progress bar to the new progress amount"""`
- `    init_progressbar(screen, x, y, width, height, 0) # clear `
- `    progress_width = int(progress * width)`  
- `    pygame.draw.rect(screen, (255,255,255), (x, y, progress_width, height))`
- `    pygame.display.update()`

5. 初始化 Pygame 和設定視窗大小為 640x480
- ` pygame.init() `
- ` screen = pygame.display.set_mode((640, 480)) `

6. 設定視窗標題為 "卡個位閃邊去"。
- ` pygame.display.set_caption("卡個位閃邊去") `

7. 設定 Haar 级聯分類器用於偵測人臉，並初始化人臉數目的變數
- ` face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') `
- ` num_faces = 0 `

8. 設定存放圖片的資料夾，如果該資料夾不存在，則創建一個
- ` img_folder = 'webcam_pics' `
- ` if not os.path.exists(img_folder): `
- `       os.mkdir(img_folder) `

9. 設定 Pygame 中的按鈕和相關文字
- ` font = pygame.font.Font('chinese.ttf', 48) `
- ` start_button = pygame.Rect(220, 200, 200, 50) `
- ` start_text = font.render('Start', True, (0, 0, 0)) `
- ` exit_button = pygame.Rect(220, 300, 200, 50) `
- ` exit_text = font.render('Exit', True, (0, 0, 0)) `

10. 設定遊戲標題文字
- ` font_title = pygame.font.Font('chinese.ttf', 64) `
- ` title_text = font_title.render('卡個位閃邊去', True, (0, 0, 0)) `

11. 設定綠色方塊的相關變數
- ` block_width, block_height = 450, 360 `
- ` block_x = random.randint(0, 640 - block_width) `
- ` block_y = random.randint(0, 480 - block_height) `
- `  block_speed_x = 1 `
- ` block_speed_y = 1 `

12. 初始化遊戲控制的變數
- ` run = True `
- ` game_started = False `
- ` start_time = 0 `
- ` game_over = False `

13. 遊戲主迴圈，包含了遊戲未開始、開始和結束三種狀態的處理
- ` while run: `
- `     if not game_started and not game_over: `
- `         # 初始畫面和按鈕的顯示 `
- `     for event in pygame.event.get(): `
- `         # 處理事件，例如點擊按鈕、退出遊戲等 `
- `     if game_started: `
- `         # 攝像頭迴圈 `
- `         # 顯示視訊畫面和 Pygame 的畫面 `
- `     if game_over: `
- `         # 遊戲結束後的處理 `

14. 遊戲結束後的清理和顯示畫面
- ` cap.release() `
- ` screen.fill((255, 255, 255)) `
- ` # 顯示自動截的圖片和 Winner 標題 `

15. 更新 Pygame 視窗，等待 15 秒顯示遊戲結果，最後關閉 Pygame
- ` pygame.display.flip()  # 更新畫面 `
- ` pygame.time.wait(15000)  # 停留15秒顯示結果 `
- `pygame.mixer.music.stop()  # 停止背景音樂`
- ` pygame.quit() `

## 困難及未來展望
### 困難

- 在創新性這方面想很久
- 第一次接觸pygame跟opencv，所以要做出整個框架想很久
- 將pygame跟OpenCV的程式結合時，我們因為原本選用pygame當作基底去做，導致前期一直碰壁
- 在虛擬機上無法使用鏡頭
- 進度調會一閃一閃

### 未來展望

- 遊戲內還存在一些bug，還可以再更好
- 希望能把開始介面弄得更精緻一點(例如點按鈕時有個壓下去的動畫)
- 整個遊戲能在更流暢
- 可以添加更多功能(像排行榜）
- 能確實將進度條弄好
- 希望能增加隨機音樂，音樂停止時偵測的功能
- 還有躲貓貓，離開鏡頭的玩法

## 工作分配 Job Assignment
- 108213041 吳健瑋
  -  OpenCV
  -   程式撰寫
- 110213061 黃士祐
  -   readme製作
  -   pygame
  -   程式撰寫
- 110213062 黃聖軒
  -   readme
  -   OpenCV
  -   程式撰寫
- 110213073 張瑋倫
  -   pygame
  -   pygame跟OpenCV程式結合
  -   程式撰寫


## 特別感謝
- 感謝助教柏瑋借我們無敵電腦
- 感謝 ivy rita ray 激發我們想法
- 感謝助教們跟BlueT，辛苦了

## 參考資料 Reference

- https://hackmd.io/@Derek46518/HyZHsD0Qo
- https://www.youtube.com/watch?v=61eX0bFAsYs
- https://www.youtube.com/watch?v=xjrykYpaBBM
- https://itecnote.com/tecnote/python-display-cv2-videocapture-image-inside-pygame-surface/
