# FastAPI Hello API

部署到 Render 後，呼叫根路徑會回傳：

```json
{"message": "Hello"}
```

## 本機執行

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

開啟 <http://127.0.0.1:8000/>。

API 文件位於 <http://127.0.0.1:8000/docs>。

## 部署到 Render

1. 把本專案上傳至 GitHub repository。
2. 登入 Render，選擇 **New > Blueprint**。
3. 連接該 GitHub repository。
4. Render 會讀取 `render.yaml` 並建立 Web Service。
5. 部署完成後，開啟 Render 提供的網址即可看到回傳結果。
