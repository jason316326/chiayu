# Copilot 指令 (Flask Todo 應用程式)

## 專案概述
這是一個使用 Flask 框架開發的待辦事項清單應用程式。專案採用 MVC 架構，使用 SQLite 作為資料庫。

## 環境設定
### 必要條件
- Python 環境：使用 Conda base 環境
- 資料庫：SQLite (自動建立於 instance/app.db)

### 快速開始
1. 啟動環境：
```bash
conda activate base
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

3. 初始化資料庫：
```bash
python -c "from app import db; db.create_all()"
```

4. 啟動應用程式：
```bash
python app.py
```

## 專案結構
```
lesson21/
├── .env                # 環境變數設定
├── app.py             # 主應用程式 (路由、模型定義)
├── requirements.txt   # 專案依賴
├── static/           # 靜態資源 (CSS)
└── templates/        # HTML 模板
```

## 核心組件
1. 資料模型 (`app.py`)：
   - `Todo` 類別：管理待辦事項
   - 欄位：id, title, description, created_at, completed

2. 路由 (`app.py`)：
   - GET `/`: 顯示所有待辦事項
   - POST `/add`: 新增待辦事項
   - GET `/complete/<id>`: 切換完成狀態
   - GET `/delete/<id>`: 刪除待辦事項

## 開發工作流程
1. 資料庫變更：
   - 修改 `Todo` 模型後，需要重新執行 `db.create_all()`
   - 資料庫檔案位於 `instance/app.db`

2. 前端修改：
   - HTML 模板位於 `templates/index.html`
   - CSS 樣式位於 `static/style.css`

## 注意事項
- 執行任何 Python 命令前必須先激活 Conda 環境
- 修改資料模型後需要重新初始化資料庫
- 保持 `.env` 檔案的安全性，不要提交敏感資訊

## 常見問題排解
1. 資料庫錯誤：
   - 刪除 `instance/app.db`
   - 重新執行 `db.create_all()`

2. 套件相關錯誤：
   - 確認是否在正確的 Conda 環境中
   - 重新執行 `pip install -r requirements.txt`
