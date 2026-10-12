# Video Compression 教材主題索引

最後更新：2026-10-06。已索引 `materials/` 內 5 份 PDF，共 245 頁。

這份文件是課程教材的查找入口：先依問題找到主題，再沿著來源與頁碼回到原始投影片。摘要用於定位；公式、圖表、數值例題與作業要求仍以讀取原始內容後的確認結果為準。

## 使用與引用方式

1. 回答課程問題前，先確認 `materials/` 是否有新增、刪除、更名或替換的教材；若索引已過期，先更新受影響的項目。
2. 從「問題快速導航」或「主題索引」選擇相關來源。來源代號 `C1` 至 `C5` 對應下方清單，代號後的頁碼只屬於該檔案。
3. **本文的 p. / pp. 一律指 PDF 實際頁序，從 1 開始，包含封面。** 不直接拿頁角印刷的投影片編號當成 PDF 頁序。
4. 一般概念可先利用摘要定位；涉及推導、計算、矩陣、圖示、演算法步驟或作業實作時，必須讀取相關原頁及必要的前後頁。圖片內的公式與表格可能無法由文字擷取取得，需檢視頁面影像。
5. 回答時在相關敘述旁標示來源，例如：`[C2] PDF pp. 33–35，〈2D DCT Separable Computation〉`，並提供原始檔案連結。若使用者說「第 22 頁」而存在兩種頁碼，先說明採用哪一種。
6. 區分「投影片內容」、「根據教材做的推導」與「教材之外的補充」。不要把摘要或自行推導的內容冒充投影片原文；有疑似筆誤時說明差異並核對，不直接照抄。
7. 作業題目、輸入格式、參數、限制和評分方式，要另讀該份作業的原始說明；教材只提供相關概念依據。索引找不到時，搜尋現有檔案並註明缺口，不捏造頁碼或題號。

## 教材清單與版本基準

| 代號 | 原始檔案 | PDF 頁數 | 主要涵蓋範圍 | SHA-256 前 16 碼 |
| --- | --- | ---: | --- | --- |
| C1 | [Ch1-DigitalVideoFundamentals (1).pdf][C1] | 34 | 數位影像、色彩、取樣、壓縮與品質評估 | `f561a6da6f683e7c` |
| C2 | [Ch2-HVS_Transform_Quantization (1).pdf][C2] | 81 | HVS、Gamma、DCT、量化、Lloyd–Max、VQ | `650da1bda7d4474f` |
| C3 | [Ch3-EntropyCoding.pdf][C3] | 37 | 資訊理論、Huffman、Arithmetic Coding、機率模型 | `320d77a6cbf5e71d` |
| C4 | [Ch4-JPEG.pdf][C4] | 22 | JPEG 流程、MCU、量化、DC/AC 編碼、Restart Marker | `1a5c4b77ab386b1c` |
| C5 | [Ch5-Prediction.pdf][C5] | 71 | DPCM、Intra/Inter Prediction、ME/MC、區塊切割、MV 編碼 | `94c1207ce40d3aa6` |

雜湊用於辨識同名檔案是否換版；檔名相同不代表內容或頁碼相同。本次索引範圍只包含 `materials/`，不包含根目錄的作業檔案，也尚未建立任何作業題號對照。

已確認的頁碼差異：C4 的 PDF p. 21 印為投影片 22，PDF p. 22 印為投影片 23；引用這兩頁時應同時註明 PDF 頁序與投影片編號。

## 問題快速導航

| 我想問的問題 | 先看主題 | 優先讀取 |
| --- | --- | --- |
| 解析度、fps、bit depth 如何決定資料量？ | [T01 數位影像基礎](#t01) | C1 pp. 2–8、14–21、26 |
| RGB、YCbCr、4:2:0 差在哪？為什麼可以減少色彩資料？ | [T01](#t01)、[T02 視覺感知](#t02) | C1 pp. 22–26；C2 pp. 5–6、15；C4 pp. 4–7 |
| MSE、PSNR、MOS 或壓縮率怎麼看？ | [T01](#t01) | C1 pp. 30–34 |
| Gamma、JND、Masking 與壓縮有什麼關係？ | [T02](#t02) | C2 pp. 3–16 |
| DCT 的基底、DC/AC、正逆轉換與矩陣怎麼理解？ | [T03 轉換編碼](#t03) | C2 pp. 18–36 |
| 大小 DCT 區塊、Integer Transform 或 DFT/DCT 差在哪？ | [T03](#t03) | C2 pp. 37–51 |
| 量化、Dead Zone、6 dB/bit、Lloyd–Max 怎麼算？ | [T04 量化](#t04) | C2 pp. 53–67 |
| VQ、Codebook、LBG、K-means、VQ-VAE 是什麼？ | [T04](#t04) | C2 pp. 68–81 |
| Entropy、Huffman Tree、Arithmetic Coding 怎麼做？ | [T05 熵編碼](#t05) | C3 pp. 7–31 |
| Adaptive 與 Context-adaptive 機率模型差在哪？ | [T05](#t05) | C3 pp. 33–37 |
| JPEG 每一步做什麼？MCU、Zig-zag、DC/AC 如何編碼？ | [T06 JPEG](#t06) | C4 pp. 3–22 |
| 為什麼編碼 residual？為什麼預測需要 closed loop？ | [T07 預測與 Intra](#t07) | C5 pp. 2–10 |
| Intra 的 Vertical、Horizontal、DC、Angular、Plane 怎麼做？ | [T07](#t07) | C5 pp. 12–24 |
| Motion Vector、SAD、Sub-pixel、TSS/DS/HS/TZ Search？ | [T08 Inter 與 ME/MC](#t08) | C5 pp. 26–35、45–58 |
| CU、CTU、Quad-tree、QTMT、RDO 如何選區塊？ | [T09 區塊切割與 RDO](#t09) | C5 pp. 37–43；C2 p. 60 |
| MVP/MVD、AMVP、HMVP、AMVR、SMVD、Affine Motion？ | [T10 運動資訊編碼](#t10) | C5 p. 35、pp. 60–70 |

## 主題索引

<a id="t01"></a>

### T01｜數位影像、色彩格式與壓縮品質

建立影像的資料表示方式，理解壓縮利用的冗餘，以及如何比較資料量和重建品質。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Sampling、Quantization、Raw Video Data Rate | 空間／時間取樣、bit depth、RGB 每像素位元數；`W × H × fps × bits per pixel` | [C1][C1] pp. 2–8 |
| CFA、Bayer、Demosaicing、Foveon-like | 感測器如何取得色彩、空間與深度取樣、缺失色彩插值 | [C1][C1] pp. 9–13 |
| Digital Video Format、Resolution | QCIF/CIF、SD/HD/UHD、格式與資料率比較表 | [C1][C1] pp. 14–16 |
| Progressive、Interlace、De-interlacing | Frame/field、逐行／交錯掃描、Weave/Bob、PAL/NTSC frame rate | [C1][C1] pp. 17–21 |
| Color Space、RGB、YUV、YIQ、YCbCr | 亮度與色度分離、色彩空間轉換、RGB 分量權重 | [C1][C1] pp. 22–25 |
| Chroma Subsampling、4:4:4、4:2:2、4:2:0 | 各色彩分量的取樣比例、減少色度解析度 | [C1][C1] p. 15、p. 26；[C4][C4] pp. 4–7 |
| Redundancy、Perceptual Irrelevance、Lossless/Lossy | 空間／時間／統計冗餘、感知不重要資訊、有損與無損 | [C1][C1] pp. 27–29 |
| Compression Ratio、MSE、PSNR、MOS | 壓縮率公式、客觀品質、PSNR 與主觀感知的限制 | [C1][C1] pp. 30–34 |

銜接：色度取樣的感知理由看 [T02](#t02)；量化失真看 [T04](#t04)；壓縮率與品質的取捨看 [T09](#t09)。計算 raw bitrate 時須先確認色度格式、分量 bit depth，以及輸入是 frames/sec 還是 fields/sec。

<a id="t02"></a>

### T02｜人類視覺系統與感知編碼

重點是「相同數值誤差不一定造成相同視覺影響」，再連到 Gamma、色度取樣和量化配置。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Nonlinear Brightness、Weber’s Law、JND | 背景亮度、相對亮度差、最小可察覺差異 | [C2][C2] pp. 3–4 |
| Luminance vs. Chroma Sensitivity | 亮度與色度的空間敏感度及比較圖 | [C2][C2] pp. 5–6 |
| Spatial Frequency、CSF、CPD、Campbell-Robson Chart | 空間頻率、對比敏感度與視角單位 | [C2][C2] pp. 7–8 |
| Spatial/Temporal Masking | 紋理、運動與時間遮蔽；Forward/Backward Masking | [C2][C2] pp. 9–10 |
| Gamma Encoding/Correction、OETF、EOTF | 從光到訊號再到顯示的流程、非線性編碼曲線 | [C2][C2] pp. 12–14 |
| Perceptual Coding Summary | 色度次取樣、各種 HVS 特性對壓縮的啟示 | [C2][C2] pp. 15–16 |

銜接：加權量化的實際應用看 [C4][C4] p. 11；不要把 Gamma、色彩空間轉換、色度次取樣當成同一個步驟。

<a id="t03"></a>

### T03｜Transform Coding、DCT 與實作考量

從基底轉換和投影理解 DCT，再連到能量集中、可分離運算、區塊大小與整數近似。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Coordinate Rotation、Projection、Energy Compaction | 相鄰像素相關性、基底與內積、反轉換的線性組合 | [C2][C2] pp. 18–22 |
| 1D DCT、Basis Vector、DC/AC | 8-point 基底、正規化、係數意義、低／高頻例子 | [C2][C2] pp. 23–27 |
| 2D DCT、Outer Product、IDCT | 由 1D 基底組成 2D basis image；64 個係數、正逆轉換 | [C2][C2] pp. 28–32 |
| Separable Computation | 兩次 1D DCT、矩陣形式 `C = B F Bᵀ`、運算複雜度 | [C2][C2] pp. 33–35 |
| 2D DCT Energy | 自然影像的低頻能量集中 | [C2][C2] p. 36；[C4][C4] p. 9 |
| Transform Block Size | 64×64 與多個 8×8、基底涵蓋範圍、誤差分布、動態尺寸 | [C2][C2] pp. 37–44 |
| Integer Transform、Shift-and-Add、Normalization | 浮點實作與 drift、整數近似、縮放合併到量化 | [C2][C2] pp. 45–49 |
| DFT vs. DCT | 比較示意與能量集中、重建影像比較 | [C2][C2] pp. 50–51 |

銜接：DCT 後的精度損失看 [T04](#t04)；具體矩陣算例看 [C4][C4] pp. 12–14。做數值題前核對基底正規化、row/column 順序與 DC 定義；C2 pp. 26–27 的直觀頻率向量例子不可直接取代 p. 23 的正式 DCT 基底。

<a id="t04"></a>

### T04｜量化、失真模型與 Codebook

理解如何把高精度數值映射到有限表示，以及均勻、非均勻、向量量化如何取捨。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Quantization、Decision Boundary、Reconstruction Level | 精度降低、量化索引與反量化重建的兩階段模型 | [C2][C2] pp. 53–55 |
| Uniform、Mid-Tread、Mid-Riser、Dead Zone | 是否有零重建值、零區間加寬、產生更多零係數 | [C2][C2] pp. 56–57 |
| Quantization Noise、6 dB Rule | 加性誤差模型、均勻誤差假設下的 `Δ²/12`、每 bit 約 6 dB | [C2][C2] pp. 58–59 |
| Rate–Distortion Theory | Rate/Distortion 定義、品質與位元數的取捨 | [C2][C2] p. 60 |
| Non-Uniform、Lloyd–Max | 機率密度、邊界中點條件、重建值質心條件、迭代程序 | [C2][C2] pp. 61–64 |
| Lloyd–Max Example | 四階量化、指數型輸入例子、迭代結果與 MSE 比較 | [C2][C2] pp. 65–67 |
| Vector Quantization、VQ、Codevector | 區塊向量化、最近 codevector 搜尋、傳送 codebook index | [C2][C2] pp. 68–70 |
| LBG、K-means | Codebook 設計、分群與質心更新、迭代圖例 | [C2][C2] pp. 71–76 |
| VQ-VAE、Latent Space | 傳統 VQ 與 learned latent VQ 的流程比較、實務取捨 | [C2][C2] pp. 77–81 |

銜接：JPEG 的逐係數加權量化看 [C4][C4] pp. 10–14；量化後的符號如何再壓縮看 [T05](#t05)。`Δ²/12` 和 6 dB/bit 是帶有假設的模型，計算時需交代輸入範圍、量化步階與是否發生飽和。

<a id="t05"></a>

### T05｜資訊理論、熵編碼與機率模型

從機率與資訊量理解平均碼長，再定位 Huffman、算術編碼及模型更新。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Bit、Biased Coin、Self-Information、Entropy | bit/log₂、偏硬幣例子、`−log₂ p(x)`、平均資訊量與碼長下界 | [C3][C3] pp. 2–8 |
| Sequence Coding、Fixed/Variable-Length、Prefix-Free | 平均小數 bit 的意義、聯合編碼、固定／變長碼、無歧義解碼 | [C3][C3] pp. 9–12 |
| Huffman Coding | 建樹、合併最小權重、例題、prefix-free 性質、最適性範圍與限制 | [C3][C3] pp. 14–18 |
| Huffman Applications、CAVLC、CABAC | 各編碼標準應用的概覽；此處僅簡介 CAVLC/CABAC | [C3][C3] p. 19 |
| Arithmetic Coding/Decoding | 區間細分、SQUEEZE 編解碼、停止條件、AABAA 比較 | [C3][C3] pp. 21–26 |
| Integer Implementation、Renormalization | 有限精度區間、輸出共同前綴、區間縮放與整數運算 | [C3][C3] pp. 27–31 |
| Static/Adaptive Probability Model | 固定模型、side information、同步更新機率 | [C3][C3] pp. 33–35 |
| Context-Adaptive、Conditional Entropy | 依 context 選模型、條件機率、條件熵例子 | [C3][C3] pp. 36–37 |

銜接：JPEG 的符號來源看 [T06](#t06)；prediction residual 的統計特性看 [T07](#t07)。寫可執行的算術編碼器時，需另確認區間端點慣例、終止方式及完整 renormalization/underflow 規則，不能只把示意投影片當成完整規格。

<a id="t06"></a>

### T06｜JPEG：把色彩、DCT、量化與熵編碼串起來

這份教材適合用來對照完整編解碼流程，及辨認各階段對資料與失真的影響。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| JPEG Overview、Encoding Pipeline | 各階段順序、有損／無損及資料量變化；最後一頁是流程圖 | [C4][C4] pp. 2–3、p. 22（投影片 23） |
| RGB to YCbCr、Chroma Subsampling | 色彩轉換與色度次取樣的不同作用 | [C4][C4] pp. 4–5 |
| DCT、MCU、IDCT、Energy Compaction | 8×8 DCT、4:2:0 的 MCU：4 Y + 1 Cb + 1 Cr、重建 | [C4][C4] pp. 6–9 |
| Quantization、Weighted Quantization | 量化矩陣、反量化、不同頻率的精度配置 | [C4][C4] pp. 10–11 |
| DCT → Quantization → Dequantization → IDCT | 平滑區塊與紋理區塊的矩陣例題、重建誤差比較 | [C4][C4] pp. 12–14 |
| Zig-zag Scanning | 係數重新排序、零係數集中與後續編碼的關係 | [C4][C4] p. 15 |
| AC、RLC、RunLength/Size/Amplitude | AC 係數的零游程與數值表示、哪些部分交給 Huffman | [C4][C4] pp. 16–17 |
| DC、DPCM | 相鄰 block 的 DC 差值編碼 | [C4][C4] p. 18 |
| Restart Marker、DRI、RST0–RST7 | MCU 間隔、DC predictor 重設、錯誤傳播與重新同步 | [C4][C4] pp. 19–20 |
| VLC、Huffman | 建樹示意與符號碼字表 | [C4][C4] p. 21（投影片 22） |

銜接：需要推導 DCT 看 [T03](#t03)，量化設計看 [T04](#t04)，Huffman 原理看 [T05](#t05)。注意 MCU 與單一 8×8 DCT block 是不同層級。

<a id="t07"></a>

### T07｜Predictive Coding、DPCM 與 Intra Prediction

先理解 residual 與編解碼端的共同參考，再延伸到同張影像的區塊預測。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Residual、DPCM | `原始值 − 預測值`、殘差分布、編碼器／解碼器流程 | [C5][C5] pp. 2–5 |
| Open-Loop、Closed-Loop、Drift | 原始與重建參考、mini decoder、同步與誤差累積比較 | [C5][C5] pp. 6–10 |
| 1D/2D/3D Prediction、Spatial Redundancy | DPCM/Intra/Inter 的關係、可用重建鄰居與掃描限制 | [C5][C5] pp. 12–13 |
| Vertical、Horizontal、DC | 4×4 預測範例、top/left 邊界與參考不可用時的處理 | [C5][C5] pp. 14–15 |
| Angular Prediction | 方向性預測、插值與斜向紋理 | [C5][C5] p. 16 |
| Plane Prediction、Least Squares | 平面模型、亮度梯度、理論數值例題、最小平方法 | [C5][C5] pp. 17–20 |
| H.264 Plane Mode | 邊界梯度近似、16×16 plane、整數實作與比較 | [C5][C5] pp. 21–24 |

銜接：跨影格預測看 [T08](#t08)。JPEG 的 DC DPCM 在 [C4][C4] p. 18；這裡的 DPCM 是更一般的預測編碼架構，引用時說明所處階段。

<a id="t08"></a>

### T08｜Inter Prediction、Motion Estimation 與 Motion Compensation

理解參考影格、block matching、搜尋成本與精度，再比較快速搜尋的路徑。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Temporal Redundancy、ME、MC、MV | 參考影格、區塊運動補償、平移／仿射模型與編碼流程 | [C5][C5] pp. 26–31 |
| BMA、Search Window、SAD | 區塊匹配與誤差成本；Full Search 與 Fast Search 的取捨 | [C5][C5] pp. 30–32 |
| Sub-pixel、Half-pel、Quarter-pel、6-tap FIR | 分數像素動機、插值濾波與計算／記憶體成本 | [C5][C5] pp. 33–34 |
| MV Coding and Residual Coding | MV 差分與殘差的 transform/quantization/entropy coding | [C5][C5] p. 35 |
| Full Search、Three-Step Search（TSS） | coarse-to-fine、step size 4→2→1、與全搜尋點數比較 | [C5][C5] pp. 45–47 |
| Diamond Search（DS）、LDSP/SDSP | 大菱形搜尋、小菱形精修、位置移動例子 | [C5][C5] pp. 48–50 |
| Hexagon Search（HS） | 六角形搜尋與精修、TSS/DS/HS 比較 | [C5][C5] pp. 51–52 |
| TZ Search、Raster Search | 起始 predictor、多尺度搜尋、raster 與 refinement、圖例及總結 | [C5][C5] pp. 53–58 |

銜接：區塊切割看 [T09](#t09)，如何節省 MV 位元看 [T10](#t10)。搜尋點數需依題目指定的搜尋範圍、邊界、重複點計算方式和停止條件重新核算；投影片的例子不是所有輸入的固定成本。

<a id="t09"></a>

### T09｜區塊切割與 Rate–Distortion Optimization

把 transform 尺寸、prediction partition 和位元／失真成本連起來，但保留各自的定義。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| Rate–Distortion、RDO | Rate/Distortion 觀念與最佳化目標 | [C2][C2] p. 60 |
| Adaptive Transform Block Size | 能量集中、誤差空間範圍與運算量 | [C2][C2] pp. 38–44 |
| Macroblock、CU、CTU | MPEG-2、H.264、HEVC、VVC 區塊切割演進概覽 | [C5][C5] pp. 37–38 |
| Quad-tree、Recursive Splitting | HEVC 切割示意、父節點／子節點的 RDO 比較 | [C5][C5] pp. 39–40 |
| QTMT、MTT、Binary/Ternary Tree | VVC 方形／矩形分割、QT 與 MTT 階段及例子 | [C5][C5] pp. 41–43 |
| RDO for Motion Information | AMVP predictor 選擇與其位元成本取捨 | [C5][C5] p. 64；延伸例子 pp. 67–69 |

銜接：問「block size」時先辨識是 transform block、prediction block、CU/CTU 還是 JPEG MCU；不同層級不能直接混用。

<a id="t10"></a>

### T10｜Motion Vector Prediction 與進階運動表示

本主題聚焦如何表示與編碼 motion information；與搜尋最佳匹配位置的 ME 互相關聯。

| 子主題／原文關鍵字 | 可查內容 | 原始位置 |
| --- | --- | --- |
| MVP、MVD | `MVD = MV − MVP`、差分編碼 | [C5][C5] p. 35 |
| AMVP | 候選清單、編碼 predictor index 與 MVD、解碼重建 | [C5][C5] p. 60 |
| Spatial/Temporal Candidates | A0/A1、B0/B1/B2、co-located block、時間距離縮放 | [C5][C5] pp. 61–62 |
| Candidate List、Pruning、RDO | 候選搜尋順序、去重、清單建構與選擇成本 | [C5][C5] pp. 63–64 |
| HMVP（History-based MVP） | 歷史運動資訊 buffer 與候選來源 | [C5][C5] pp. 65–66 |
| AMVR（Adaptive MV Resolution） | MV 精度選擇與 rate–distortion 取捨 | [C5][C5] p. 67 |
| SMVD（Symmetric Motion Vector Difference） | 雙向預測的對稱 MVD、共用差分與取捨 | [C5][C5] pp. 68–69 |
| Affine Motion、Control-point MV | 旋轉、縮放、剪切；控制點與 4/6 參數模型 | [C5][C5] p. 29、p. 70 |
| Summary & Future Outlook | Inter prediction 總結與神經網路運動補償展望 | [C5][C5] p. 71 |

## 例題與圖表的直接入口

以下適合需要手算、逐步推演或對照圖示時優先開啟；不是作業題號。

| 例題／圖表 | 原始位置 |
| --- | --- |
| DCT 基底圖、正逆轉換、兩次 1D 與直接 2D 的比較 | [C2][C2] pp. 23–35 |
| Lloyd–Max 四階量化例子與 MSE 比較 | [C2][C2] pp. 65–67 |
| K-means 初始分群至收斂 | [C2][C2] pp. 72–76 |
| Huffman Tree | [C3][C3] pp. 15–18；[C4][C4] p. 21 |
| SQUEEZE 算術編解碼、AABAA 比較 | [C3][C3] pp. 23–25 |
| 算術編碼整數區間與 Renormalization | [C3][C3] pp. 28–30 |
| JPEG 平滑／紋理區塊數值矩陣與誤差 | [C4][C4] pp. 12–14 |
| JPEG Restart Marker 錯誤傳播例子、總流程圖 | [C4][C4] p. 20、p. 22 |
| Intra 基本模式、Plane 理論例子與 H.264 公式 | [C5][C5] pp. 14–22 |
| Sub-pixel 插值圖、QTMT 切割圖 | [C5][C5] p. 34、pp. 41–43 |
| TSS、Diamond、Hexagon、TZ 搜尋圖例 | [C5][C5] pp. 46–57 |
| AMVP 空間／時間候選位置 | [C5][C5] pp. 61–63 |

## 原始教材核對提醒

這些是本次閱讀遇到的局部不一致或使用限制，並非完整勘誤表。回答涉及這些位置時，先重看原頁，必要時說明推導或查證依據。

| 位置 | 核對重點 |
| --- | --- |
| C1 p. 14 | 格式比較表的 raw data rate 應搭配解析度、fps、bit depth 與色度格式重算，不將表中的所有數值視為共用相同假設。 |
| C2 pp. 23、26–27 | 正式 DCT 正規化基底與直觀正負交替向量例子有所區別；計算係數應確認使用哪個定義。 |
| C3 pp. 36–37 | 機率範例文字有疑似筆誤，例如 Context B 重複標示 `P(0)`，以及某組條件機率相加不為 1；代入熵公式前須核對。 |
| C4 pp. 5、7 | p. 5 將 4Y+1Cr+1Cb 寫在 DCT block 的敘述下；p. 7 明確把六個 8×8 blocks 對應到一個 4:2:0 MCU。 |
| C4 p. 16 | JPEG 章節的敘述中出現 `MPEG-2`；引用時需辨識章節脈絡，不將此句當成兩種格式完整語法相同的證據。 |
| C4 pp. 12–14；C5 p. 7 等 | 重要內容可能主要存在於圖片；文字擷取很少不代表空白頁。 |
| C5 pp. 6、8–10 | 閉迴路的文字敘述與個別公式標記需相互核對，重點是雙方以相同重建資料作為參考。 |

目前 CAVLC/CABAC、VQ-VAE 與神經網路運動補償只涵蓋概覽或展望；不能據此假定已提供完整實作規格、模型訓練細節或標準條文。

## 持續加入教材時的更新流程

本文件是可持續維護的索引，**放入新檔案不會自行更新 Markdown**。新增教材後，可要求：「請掃描 materials/ 並更新 MATERIALS.md」，或在下一次課程問答時先依本文件的使用方式檢查差異。

1. **盤點差異**：遞迴列出 `materials/` 的檔案，與來源清單比對；對 PDF 檢查頁數及 SHA-256。新增、換版、更名、移除分別處理，不只比較檔名。
2. **閱讀新增或變更的內容**：確認實際主題、頁序、章節標題、例題、圖表及必要的視覺內容；掃描檔需 OCR 或直接閱讀影像。未讀到的內容標為「待索引」，不要猜測範圍。
3. **維持來源代號穩定**：既有 C1–C5 不因排序改變而重編。新增講義接續使用未使用的 C 代號；作業可用 HW01、HW02，補充文件可用 S01、S02。不同版本同時保留時給予可區分的代號並註明關係，不把不同版本頁碼混在一起。
4. **依主題整合**：同一概念跨教材出現時加入同一主題，標明主要講解、例題或延伸來源；真的出現新主題才新增 T11、T12 等。保留既有主題代號與錨點。
5. **更新所有定位資訊**：來源清單、頁數、版本指紋、受影響頁碼、快速導航、例題入口、作業對照和核對提醒都應同步更新。檔案移除或更名後修正連結；未重新確認的舊頁碼標為待核對。
6. **驗證並記錄**：確認連結存在、頁碼不超出檔案範圍、列出的主題可在原頁找到；更新頁首日期、檔案／頁數總計與下方更新紀錄。

目前連結使用本機絕對路徑；若課程資料夾搬移，需同步調整來源連結。

### 新教材項目範本

```markdown
來源代號：C06 / HW01 / S01（擇一並保持唯一）
檔案：[實際檔名](<實際絕對路徑>)
類型：投影片／作業／補充資料
版本識別：頁數、SHA-256 前 16 碼、索引日期
主題：Txx；新增主題時補上名稱與固定錨點
位置：PDF pp. x–y／文件小節／程式路徑與函式名稱
內容：可以回答哪些問題；保留原文術語以便搜尋
例題／圖表：頁碼與標題
關聯：先備主題、延伸教材、相關作業題號
狀態：已索引／待索引／換版後待核對
```

作業加入後，另建立「作業代號／題號 → 題目頁碼 → 涉及主題 → 教材頁碼」對照表。必須先讀作業說明；不從檔名推測題目、參數或繳交規定。非 PDF 文件使用實際存在的小節、工作表、題號或程式位置，不虛構 PDF 頁碼。

## 更新紀錄

| 日期 | 變更 |
| --- | --- |
| 2026-10-06 | 首次索引 C1–C5，共 245 頁；建立 T01–T10、問題導航、例題入口、頁碼規則與更新流程。 |

[C1]: </Users/harryp/Desktop/Courses/Video-Compression/materials/Ch1-DigitalVideoFundamentals (1).pdf>
[C2]: </Users/harryp/Desktop/Courses/Video-Compression/materials/Ch2-HVS_Transform_Quantization (1).pdf>
[C3]: </Users/harryp/Desktop/Courses/Video-Compression/materials/Ch3-EntropyCoding.pdf>
[C4]: </Users/harryp/Desktop/Courses/Video-Compression/materials/Ch4-JPEG.pdf>
[C5]: </Users/harryp/Desktop/Courses/Video-Compression/materials/Ch5-Prediction.pdf>
