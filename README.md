# Reversible-Computing-ESP32

這是我高三自主學習做的專案，用 ESP32-S3 接 LED 實作 Toffoli Gate，驗證蘭道爾原理。

我只是高中生，從0開始。過程很多失敗（LED不亮、程式報錯、線亂接），但失敗讓我思考更多也學到更多。

- 1/29：1/29從0開始:
 做一個最簡易Toffoli Gate的python並用esp32-s3及LED演示
- 1/30：損失計算:
 成功計算AND(不可逆)和TOFFOLI(可逆)的位元及能量損耗
- 1/31：今天做了三件事:
 1.用反演算證明計算可逆(如果f(x)可逆，f(f(x))=x)  2.把手動輸出換成自動運行三個LED燈的每種可能(2^3=8種)  3.做了總節能計算(例如模擬大腦每秒產生的熱可以煮開 0.08573223L的水)
- 2/3：試能量回收，發現需要 CNOT 把狀態擴散（T-C-T）

完整程式和 LED 實際亮滅的照片在報告 PDF 裡。  

GitHub 連結：https://github.com/isaaccantwin/Reversible-Computing-ESP32  
完整報告見申請文件「多元表現」
