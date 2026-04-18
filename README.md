# Reversible-Computing-ESP32
# Reversible-Computing-ESP32

這是我高三自主學習做的專案，用 ESP32-S3 接 LED 實作 Toffoli Gate，驗證蘭道爾原理。

我只是高中生，從0開始。過程很多失敗（LED不亮、燒壞板子），但失敗讓我思考更多。

- 1/29：寫 Toffoli Gate
- 1/30：算出 AND 擦除1 bit 會產生 2.869...×10⁻²¹ J 熱量
- 1/31：自動測試8種輸入
- 2/3：試能量回收，發現需要 CNOT 把狀態擴散（T-C-T）

完整程式和 LED 實際亮滅的照片在報告 PDF 裡。  
我沒有做得很完美，但這就是我高中能做到的全部，誠實呈現。

GitHub 連結：https://github.com/isaaccantwin/Reversible-Computing-ESP32  
完整報告見申請文件「F.高中自主學習計劃與成果」
-1/29從0開始:
 做一個最簡易Toffoli Gate的python並用esp32-s3及LED演示
-1/30損失計算:
 成功計算AND(不可逆)和TOFFOLI(可逆)的位元及能量損耗
-1/31今天做了三件事:
 1.用反演算證明計算可逆(如果f(x)可逆，f(f(x))=x)  2.把手動輸出換成自動運行三個LED燈的每種可能(2^3=8種)  3.做了總節能計算(例如模擬大腦每秒產生的熱可以煮開 0.08573223L的水)
2/3做了能量收回狀態保留的模擬(T-C-T)
