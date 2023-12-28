

# Specifications of the Face Recognizer System
* 透過深度學習訓練一個基本的人臉辨識系統 


## 訓練相關使用
* 語言 - Python
* 工具 - Keras , PIL
* 神經網路結構 - CNN 
* Model - Sequential
* Batch size - 16
* Optimizer - Adadelta (放棄: Adam , RMSProp)


## 相關技術
* Conv2D
* Dropout
* MaxPooling2D
* activation - Relu , Softmax
* Valid Padding
* Crossentropy

## test recognizer to evaluate its recognition rate
* 將所有照片都去做測試，再將識別錯誤總數紀錄，越少錯誤表示訓練結果預準。
 
 
## the problems suffered in our development
batch size太大的話GPU會吃不消，所以不能設太大。
 
## any bonus features or functionalities included in your recognizer
我們有把資料換成自己組三個人各20張圖片下去訓練，但可能是資料太少，且每個人長相差距頗大，所以能完全成功辨識3個人。


## 心得感想
* resize部分可能會會因為和原本的照片比例和後來的比例沒有成正確比例，導致有失真的情況，以後有機會會先把圖片都先弄成正方形，再進行縮放，可能會有更好的結果。

