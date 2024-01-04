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
- 在主循環中，使用pygame.event.get()檢測Pygame事件，包括退出事件和鍵盤事件。
- 使用cap.read()讀取攝像頭的幀。將幀轉換為灰度圖像，然後使用Haar級聯分類器檢測人臉，並在檢測到的人臉周圍繪製矩形。
- 使用pygame.image.frombuffer()將OpenCV圖像轉換為Pygame表面。使用screen.blit()將Pygame表面繪製到屏幕上，然後使用pygame.display.flip()更新顯示。
- 使用cv2.imwrite()保存整個幀和裁剪的人臉圖像。
- 通過按下'C'鍵觸發保存圖像的事件。
- 使用draw_text()函數在Pygame窗口上顯示文本。
- 使用show_init和run變量來控制在初始化階段和主循環中的行為。


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
