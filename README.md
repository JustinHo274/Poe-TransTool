# PoE GGPK Translator Portal | 流亡黯道 GGPK 翻譯啟動器

[English](#english) | [繁體中文](#繁體中文)

---

## English

A lightweight, professional translation launcher for **Path of Exile**. This tool streamlines the process of applying community translations to the game's core data file (`Content.ggpk`) by providing a modern GUI and automating background tasks.

### Features
- **Path Persistence**: Automatically remembers your tool and game paths for one-click access.
- **Background Execution**: Runs the translation process in a separate thread to keep the UI responsive.
- **Auto-Enter Automation**: Automatically handles the "Press Enter to exit" prompt from the original command-line tool.
- **Modern UI**: Sleek, dark-themed interface built with `CustomTkinter`.
- **Zero Assets**: Pure code implementation, lightweight and fast.

### How to Use
1. **Download**: Get the latest `poe_trans.exe` from the [Releases](../../releases) page.
2. **Setup**: Select your `PoeChinese.exe` and `Content.ggpk` file paths.
3. **Execute**: Click **TRANSLATE**. The tool will handle the rest.
4. **Result**: A "COMPLETE" message will appear once the modification is successful.

### 🛠️ For Developers
If you wish to run from source:
1. Clone the repo: `git clone https://github.com/JustinHo274/PoE-TransTool.git`
2. Install dependencies: `pip install customtkinter`
3. Run: `python poe_trans.py`

---

## 繁體中文

這是一個專為 **《流亡黯道 (Path of Exile)》** 設計的輕量化翻譯啟動器。本工具為傳統的命令列翻譯工具提供了一個現代化的圖形介面 (GUI)，並自動化了許多繁瑣的步驟。

### 功能特色
- **路徑記憶**: 自動儲存翻譯工具與 GGPK 檔案位置，下次開啟即可一鍵翻譯。
- **異步執行**: 透過多執行緒 (Threading) 技術，在翻譯時介面不會卡死。
- **自動模擬輸入**: 自動處理原始工具「按 Enter 結束」的提示，實現全自動化流程。
- **現代化介面**: 使用 `CustomTkinter` 打造的暗黑金屬風格介面。
- **純碼實作**: 不需額外圖片素材，檔案極小且啟動迅速。

### 使用說明
1. **下載**: 從 [Releases](../../releases) 頁面下載編譯好的 `poe_trans.exe`。
2. **設定**: 點擊「Browse」選擇你的翻譯工具 (`PoeChinese.exe`) 與遊戲檔案 (`Content.ggpk`)。
3. **翻譯**: 點擊「TRANSLATE」按鈕。
4. **完成    
