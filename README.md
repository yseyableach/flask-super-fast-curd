## server裡面是api
- model裡面的app會對應到server裡面的api
- 透過blueprint 即可完成分開開發
    - ex: server中的gameservice和userservice是完全分開的，故開發者可以透過此方式共同開發


## 執行程式
- 在最外層輸入**python main.py**
- 確認資料庫名稱與model中的app.py相同
- 先確認models中的shcema是否已經migrate到db當中
- 測試api http://localhost:5000:user?id=1 有無資料
    - 也可以在apidoc找到postman的collection測試
