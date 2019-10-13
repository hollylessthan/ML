# HW 6 computer assignment readme

在此作業分成三個檔案，課本版本Adaboost, oroginal Adaboost, perceptron learning。

**Introduction**
-

This code is written in Python 3.7.0 64-bit

**Explanation of the Code**
-

* 以original的版本為來看，第一部分是random挑選十個example,第一round是隨機，第二round以後就是按照Adaboost的機率去抽機率比較大的，機率一樣就隨機抽。（課本版本Adaboost也一樣）

*    再來是建立1nn classifier，接在下面是用這個training set 分類testing example（課本版本Adaboost也一樣）


*    再來是把第二點 training examples裡的十個train出來的結果，用講義的公式改變權重。，並且標準化。（這一部份課本版本Adaboost和original 版本，beta及改變probability的計算方式分別按照chapter9投影片Table 9.4 的例題方法去計算，是兩個部分不同的地方。）

*   再來是用apha去評估classifier的weight然後去算正確率（課本版本的Adaboost是用perceptron）

*   輸出結果1代表分類錯誤，0代表分類正確

*   另外perceptron 是用chapter4公式改寫的，輸出結果第一行為更改後的權重，第二行為分類結果，一樣0代表分類正確，其他都是代表分類錯誤。
  


  