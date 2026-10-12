# Video Compression 學習疑難筆記

這份筆記用來記錄學習過程中額外提出、容易混淆或需要之後複習的問題。

## 1. DCT coefficient 和 cosine similarity 的關係

DCT 會比較整體 sequence 和不同 basis 變化形式的相似程度。

教材 Ch2 PDF pp.25–27 使用 projection 與 inner product 來描述這件事：

\[
C[k] = x \cdot b_k
\]

其中：

- \(x\)：輸入的 sequence，例如一列 8 個 pixels。
- \(b_k\)：第 \(k\) 種標準變化形式，也就是 basis。
- \(C[k]\)：輸入在這個 basis 方向上的 coefficient。

內積可以直覺理解成「兩個變化形式有多像」。例如：

```text
[3, 3] · [1, 1] = 6
```

兩者同方向，因此結果是大的正數；但：

```text
[3, 3] · [1, -1] = 0
```

正負抵消，表示 `[3, 3]` 沒有 `[1, -1]` 這種交錯變化。

不過，DCT coefficient 不完全等於一般定義的 cosine similarity。

一般 cosine similarity 是：

\[
\cos\theta=\frac{x\cdot b_k}{\|x\|\|b_k\|}
\]

DCT 的 basis 已經正規化成單位長度，因此：

\[
C[k]=x\cdot b_k=\|x\|\cos\theta
\]

所以：

- cosine similarity 主要表示「形狀有多像」；
- DCT coefficient 同時保留形狀相似度和輸入訊號的大小；
- coefficient 可以大於 1，但 cosine similarity 介於 \(-1\) 和 \(1\) 之間。

### 小例子

若：

\[
x=[3,3], \qquad b_0=\frac{1}{\sqrt2}[1,1]
\]

兩者形狀完全相同，所以 cosine similarity 是 1；但 DCT coefficient 是：

\[
C[0]=x\cdot b_0=3\sqrt2\approx4.24
\]

因此，DCT 不是只判斷「像不像」，而是把 sequence 分解成多個 basis 的加權組合：

\[
x=\sum_k C[k]b_k
\]

## 2. 為什麼要做 DCT？

DCT 和 Quantization 密切相關，但兩者負責的事情不同。

影像壓縮的大致流程是：

```text
像素 block → DCT → Quantization → Huffman / entropy coding
```

- DCT：重新整理資料的表示方式。
- Quantization：降低係數精度，造成主要的有損失真。
- Huffman coding：利用常見符號做進一步的無損壓縮。

自然影像的鄰近 pixels 通常很像：

```text
[160, 161, 160, 162, 161, ...]
```

DCT 會把這些相似的 pixels 改寫成不同速度的變化成分：

- DC：整體平均亮度。
- 低頻 AC：緩慢的亮度變化。
- 高頻 AC：快速變化、細節和紋理。

平滑區域經過 DCT 後可能接近：

```text
[很大的 DC, 小的低頻 AC, 小的高頻 AC, 0, 0, ...]
```

也就是重要資訊集中在少數係數，而不是平均分散在 64 個 pixel 值中。

這種效果稱為 **energy compaction，能量集中**。這裡的 energy 不必理解成物理能量；可以先把它理解成 coefficient 的訊號強度，通常和 coefficient 的平方有關。

因此，Quantization 可以把許多不重要的高頻小係數變成 0：

```text
DCT 前：      [160, 161, 160, 162, 161, ...]
DCT 後：      [大 DC, 小 AC, 小 AC, 很小, ...]
量化後：      [保留,   0,     0,     0,    ...]
```

如果直接對原始 pixels 做 Quantization，平均亮度和細節變化混在一起，通常不容易得到這麼多可壓縮的零值。

所以可以這樣記：

> DCT 負責把資訊重新集中，讓資料變得適合壓縮；Quantization 負責降低精度並產生失真。

DCT 本身沒有減少 64 個係數，也沒有必然造成失真；真正丟失資訊的主要步驟是 Quantization。教材 Ch2 PDF pp.33–36 說明了可分離計算與能量集中。[Ch2 PDF](</Users/harryp/Desktop/Courses/Video-Compression/materials/Ch2-HVS_Transform_Quantization%20(1).pdf>)

## 3. dB 是什麼？

教材 Ch2 PDF pp.58–59 使用 dB（decibel，分貝）描述 SNR 的改善程度。

dB 不是一個單獨的絕對單位，而是用對數表示「兩個數值的比例」。對功率比而言：

\[
\text{dB}=10\log_{10}\left(\frac{P_1}{P_2}\right)
\]

其中 \(P_1/P_2\) 是兩個功率的比值。

可以先記住幾個直覺：

```text
功率變成 2 倍  → 約 +3.01 dB
功率變成 4 倍  → 約 +6.02 dB
功率不變        → 0 dB
```

在影像壓縮裡，常用 SNR（Signal-to-Noise Ratio，訊號與雜訊的功率比）表示訊號相對於誤差有多強：

\[
\text{SNR}_{\text{dB}}
=10\log_{10}\left(\frac{P_{\text{signal}}}{P_{\text{noise}}}\right)
\]

SNR 越高，表示訊號功率相對於量化誤差越大，通常代表重建品質較好。

在理想均勻量化中，量化雜訊功率約為：

\[
P_{\text{noise}}\approx\frac{\Delta^2}{12}
\]

多增加 1 bit 時，量化步階 \(\Delta\) 約減半：

\[
\Delta_{\text{new}}=\frac{\Delta_{\text{old}}}{2}
\]

因此雜訊功率約變成四分之一：

\[
\frac{P_{\text{noise,old}}}{P_{\text{noise,new}}}=4
\]

SNR 改善量就是：

\[
10\log_{10}(4)\approx6.02\text{ dB}
\]

所以「6 dB per bit」的意思不是品質一定增加 6 dB，而是：在理想均勻量化、誤差分布等假設成立時，每增加 1 bit 的精度，量化雜訊功率約變成四分之一，SNR 約改善 6.02 dB。

這是近似規則，不代表作業中每張影像都會精確增加 6.02 dB。實際 PSNR 還會受到影像內容、量化矩陣、rounding 和 clipping 影響。

### \(\Delta^2/12\) 中的 12 從哪裡來？

把量化誤差記成 \(e\)。若量化步階是 \(\Delta\)，而輸入沒有超出量化器的可表示範圍，四捨五入造成的誤差會落在：

\[
-\frac{\Delta}{2}\le e < \frac{\Delta}{2}
\]

理想均勻量化假設誤差在這個區間內均勻分布，因此誤差的機率密度是 \(1/\Delta\)。誤差平均值為 0，所以 noise power 就是誤差的平均平方值，也就是 variance：

\[
\begin{aligned}
P_{\text{noise}}
&=E[e^2]\\
&=\frac{1}{\Delta}
\int_{-\Delta/2}^{\Delta/2}e^2\,de\\
&=\frac{1}{\Delta}
\left[\frac{e^3}{3}\right]_{-\Delta/2}^{\Delta/2}\\
&=\frac{1}{\Delta}\cdot\frac{\Delta^3}{12}\\
&=\frac{\Delta^2}{12}
\end{aligned}
\]

所以 12 來自兩件事：

- 平方函數積分會產生除以 3；
- 誤差上下界是 \(\pm\Delta/2\)，立方後合併會再產生除以 4；
- 合起來就是 \(3\times4=12\)。

例如 \(\Delta=2\) 時，誤差落在 \([-1,1]\)：

\[
P_{\text{noise}}=\frac{2^2}{12}=\frac13
\]

這個公式依賴均勻分布、沒有 overload，以及量化誤差可近似獨立等假設；它不是所有實際影像和所有量化器都會精確符合的結果。

## 4. 二階段 Huffman code：category prefix + amplitude

這份作業的 Huffman coding 容易和「直接對每個完整 value 建 Huffman tree」混淆。一般 Huffman coding 會把每個完整 symbol 當成 leaf，例如：

```text
-7, -6, ..., -1, 0, 1, ..., 7
```

但本作業採用的是兩階段表示：

```text
Huffman prefix（category）+ amplitude bits（實際 value）
```

### Category 是 Huffman symbol，不是完整 value

Category 不是任意命名或任意分組，而是由 quantized coefficient 的絕對值需要幾個 binary bits 決定。令 quantized coefficient 為 \(v\)：

\[
s=
\begin{cases}
0, & v=0\\
\lfloor\log_2|v|\rfloor+1, & v\ne0
\end{cases}
\]

也就是：

```text
s = abs(v) 的 binary bit length
```

因此 category \(s>0\) 會把 magnitude 落在

\[
2^{s-1}\le |v|\le 2^s-1
\]

的 values 放在同一組。這樣同一 category 內的每個 value 都需要恰好 \(s\) 個 amplitude bits：

```text
category 1: abs(v) = 1       → 1 個 amplitude bit
category 2: abs(v) = 2..3    → 2 個 amplitude bits
category 3: abs(v) = 4..7    → 3 個 amplitude bits
```

例如：

```text
5  = 101₂   → category 3
7  = 111₂   → category 3
-6 的絕對值是 6 = 110₂ → category 3
```

所以 category 的建立邏輯是：

```text
先依 abs(value) 的 binary bit length 分組
→ 統計每一組 category 的總頻率
→ 若自行建立 category Huffman tree，使用這些總頻率計算 prefix
→ 再用該 category 固定長度的 amplitude bits 表示實際 value
```

接著各 category 的 values 為：

```text
category 0:  0
category 1: -1, 1
category 2: -3, -2, 2, 3
category 3: -7, -6, -5, -4, 4, 5, 6, 7
```

因此 category 3 的 Huffman prefix 可以是：

```text
category 3 → 100
```

但 `100` 只表示「接下來是 category 3」，還不能決定完整 value。category 3 中的每個 value 還需要 3 個 amplitude bits：

```text
VALUE(4)  = 100 | 100
VALUE(5)  = 100 | 101
VALUE(6)  = 100 | 110
VALUE(7)  = 100 | 111

VALUE(-4) = 100 | 011
VALUE(-5) = 100 | 010
VALUE(-6) = 100 | 001
VALUE(-7) = 100 | 000
```

所以要區分：

```text
Huffman symbol：category 3
完整 token：    VALUE(5)
完整 bits：     100101
```

Category 0 是特殊情況，因為它只包含 value 0，因此沒有 amplitude bits：

```text
VALUE(0) = 00
```

### 如果自己建立 category Huffman tree，頻率怎麼算？

若採用這種兩階段設計並自行建立 Huffman tree，category 的頻率會把同一 category 內所有 values 的出現次數加總：

\[
f(\text{category }3)
=f(-7)+f(-6)+f(-5)+f(-4)+f(4)+f(5)+f(6)+f(7)
\]

例如：

```text
value  4 出現 100 次
value  5 出現  30 次
value -4 出現   2 次
value  7 出現   1 次
其他 category 3 values 出現 17 次
```

則：

```text
f(category 3) = 100 + 30 + 2 + 1 + 17 = 150
```

Huffman tree 只會看到：

```text
category 0 → 總頻率
category 1 → 總頻率
category 2 → 總頻率
category 3 → 150
...
```

它不會再區分 category 3 裡是 `4`、`5` 或 `-7`。同一 category 內的 values 不需要有相同頻率。

### 這份作業的實際情況

作業不要求從影像統計頻率，也不要求自行建立 Huffman tree。`codec_parameters.py` 已經提供固定的 `VALUE_CODE` 與 `EOB_CODE`，所以實作時是：

```text
quantized value
→ 計算 category s
→ 查固定 VALUE_CODE[s]
→ 計算 amplitude bits
→ prefix + amplitude
```

而不是：

```text
統計完整 values 的頻率
→ 建立新的 Huffman tree
→ 產生新的 codebook
```

### 這種方法的取捨

這不是對每個完整 value 做全域最佳化的 Huffman coding。例如 category 3 中 `4` 很常見、`-7` 很罕見時，它們仍然使用同樣長度的 amplitude bits。

它換來的好處是：

- codebook 比「每個 value 一個 leaf」小很多；
- decoder 讀到 category 後，就知道要讀幾個 amplitude bits；
- 實作簡單，而且很適合 transform coefficients 的 magnitude 分布。

因此可以記成：

> Huffman tree 仍然是一個 symbol 對一個 leaf；只是本作業選擇把 category 當作 symbol，而不是把完整 coefficient value 當作 symbol。category 的 prefix 負責描述幅度範圍，amplitude bits 負責描述該範圍內的實際 value。

## 5. 正式 JPEG 的 DC、DPCM 與本作業的差異

單一 8×8 DCT coefficient matrix 只有一個 DC coefficient：左上角的 \(F[0,0]\)。

```text
一個 block：
F[0,0] = DC
其他 63 個位置 = AC coefficients
```

但整張影像有很多 blocks，因此可以把相鄰 blocks 的 DC 係數排成序列。例如：

```text
Block 1 的 F[0,0] = 100
Block 2 的 F[0,0] = 102
Block 3 的 F[0,0] = 101

DC sequence = [100, 102, 101]
```

正式 JPEG 會依照 block raster order，對這個跨 block 的 DC sequence 做 DPCM：

```text
第一個：100       （通常直接編）
第二個：102-100=2
第三個：101-102=-1

DPCM sequence = [100, 2, -1]
```

因為相鄰 blocks 通常亮度相近，差分值比原始 DC 值小，較容易再交給 Huffman/VLC 編碼。

正式 JPEG 的簡化流程可寫成：

```text
DCT → Quantization → Zigzag
                  ├─ DC：DPCM
                  └─ AC：Run-Length Coding
                         ↓
                    Huffman/VLC
```

本作業省略這兩個前處理：

```text
DC：直接 VALUE(DC)，不做 DPCM
AC 內部零：每個零直接 VALUE(0)，不做完整 RLC
AC 尾端零：使用 EOB
```

因此作業中每個 block 的 \(F[0,0]\) 仍然是自己的 DC coefficient；它不會和前一個 block 的 DC 做差分。
