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

## 遊戲程式執行
- 開始遊戲時的初始畫面
<img width="481" alt="螢幕擷取畫面 2024-01-18 190132" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/7e5eaae7-9240-4523-94ec-af2cdaaf56c1">

- 設定遊戲介面按鈕

<img width="479" alt="image" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/4cde38fa-95e2-43f2-a8e4-2e16386ada59">
 
- 進入到遊戲初始畫面後會撥出聲音，音樂來源是YouTube音樂庫 無版權配樂 免費背景音樂下載: https://goo.gl/Z6TsBI
- 載入背景圖
<img width="883" alt="image" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/d49fd141-9fb5-4aa4-8890-a7bc0f104956">

- 點擊start後會開始臉部偵測
<img width="586" alt="螢幕擷取畫面 2024-01-11 182053" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/1f3a9c92-fbea-4095-9283-5a908ea0ebb4">

- 製作一個綠色方框去限制玩家跟著移動
<img width="523" alt="image" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/add6fe0e-1ccd-4814-afec-3d93e4de3780">

- 做一個時間條讓玩家知道說時間還剩多久
<img width="546" alt="image" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/09158b2f-0472-49e4-8fe3-ab43a6508ea9">

- 遊戲時間結束並出現贏家
<img width="503" alt="螢幕擷取畫面 2024-01-11 182203" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/d56b437d-df04-4c38-ae8a-7220f75fe262">

- 標題會跑出winner並自動儲存圖片到webcame_pics這個資料夾裡面
<img width="485" alt="image" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/308c5c1f-8577-4653-9d9b-3d9bc0238b9b">

<img width="879" alt="螢幕擷取畫面 2024-01-18 192900" src="https://github.com/NCNU-OpenSource/opencv_pygame_face_detection/assets/152016407/7e3c7edf-948c-4b03-8303-2b676bc4eb14">










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
- 感謝 Ivy Rita Ray 激發我們想法
- 感謝助教們跟BlueT，辛苦了

## 參考資料 Reference
- bg.jpg <a href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.backgroundlelo.com%2Fsnapseed-background-hd-4k-for-editing-download%2F&psig=AOvVaw00dEkhCvu_KNloM9zfBLPH&ust=1705055276263000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCKiMk4KQ1YMDFQAAAAAdAAAAABAD">source</a>
- Music by <a href="https://pixabay.com/users/top-flow-production-28521292/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=181126">Sergio Prosvirini</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=181126">Pixabay</a>
- <a href=https://github.com/ACh-K/Cubic-11.git>chinese.ttf</a>
- https://hackmd.io/@Derek46518/HyZHsD0Qo
- https://www.youtube.com/watch?v=61eX0bFAsYs
- https://www.youtube.com/watch?v=xjrykYpaBBM
- https://itecnote.com/tecnote/python-display-cv2-videocapture-image-inside-pygame-surface/
