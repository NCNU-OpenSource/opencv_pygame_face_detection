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
### 初始化

- 初始化 Pygame。
- 創建 Pygame 視窗和設定標題。

### 設定 Cascade Classifier：

- 使用 OpenCV 的 haarcascade_frontalface_default.xml 來檢測人臉。

### 設定遊戲初始狀態和按鈕：

- 設定遊戲狀態的變數，例如遊戲是否開始、是否結束等。
- 創建 Pygame 中的按鈕和相關文字。

### 主遊戲迴圈：

- 在遊戲未開始和未結束時，顯示初始畫面和按鈕。
- 使用滑鼠事件檢測是否按下了 "Start" 或 "Exit" 按鈕，根據按下的按鈕進行相應的處理。

### 攝像頭迴圈：

- 當遊戲開始時，進入攝像頭迴圈。
- 每一個迴圈中讀取攝像頭畫面，並使用 Haar 级聯分類器檢測人臉。
- 同時，移動並畫出綠色方塊，確保方塊在視窗內來回移動。
- 在指定的時間內（20秒）自動截取綠色方塊區域的畫面。

### 遊戲結束後的處理：

- 釋放攝像頭資源。
- 清空 Pygame 視窗。
- 顯示自動截取的畫面和 "Winner!!!" 標題。
- 更新 Pygame 視窗。

### 顯示結果並等待一段時間：

- 等待 15 秒，顯示遊戲結果。
- 關閉 Pygame 視窗。。


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
