## 103. datetime
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

```python
import datetime
```
**現在日時を取得**
```python
now = datetime.datetime.now()
print(now)                                # 現在日時をそのまま表示
print(now.isoformat())                    # ISO形式 (YYYY-MM-DDTHH:MM:SS.mmmmmm) で表示
print(now.strftime('%d/%m/%Y-%H%M%S%f'))  # 日/月/西暦4桁-時分秒マイクロ秒
print(now.strftime('%d/%m/%y-%H%M%S%f'))  # 日/月/西暦下2桁-時分秒マイクロ秒
```

**今日の日付だけを取得**
```pytohn
today = datetime.date.today()
print(today)                        # 今日の日付 (YYYY-MM-DD)
print(now.isoformat())              # 再度ISO形式で表示
print(now.strftime('%d/%m/%y'))     # 日/月/西暦下2桁
```

**時刻オブジェクトを作成**
```pytohn
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)                            # 01:10:05.000100
print(t.isoformat())                # ISO形式で時刻表示
print(t.strftime('%H_%M_%S_%f'))    # 時_分_秒_マイクロ秒
```

**timedelta（時間差）の利用**
```pytohn
print(now)                          # 現在日時
d = datetime.timedelta(weeks=-1)    # 1週間前
print(now + d)                      # 現在日時から1週間前
d = datetime.timedelta(weeks=1)     # 1週間後
print(now - d)                      # 現在日時から1週間前（同じ結果）
```

**timedeltaのいろいろな単位指定**
```pytohn
d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
d = datetime.timedelta(seconds=1)
d = datetime.timedelta(microseconds=1)
```
**指定した時間処理を停止**
```python
import time
print('########')
time.sleep(2)                       # 2秒間処理を停止
print('########')
```
**エポックタイム**
```python
print(time.time())                  # UNIX時間（1970年からの秒数）
```

**バックアップのファイル名の付け方（例）**
```python
import os
import shutil

file_name = 'test.txt'

# ファイルが存在する場合、タイムスタンプ付きでコピー
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

# ファイルを新規作成して "test" と書き込む
with open(file_name, 'w') as f:
    f.write('test')
```
## ✨ 学習のまとめ
- ` datetime `： 日付・時刻の取得と整形
- ` timedelta `： 時間差の計算
- ` time.sleep `： プログラムを一時停止
- ` os.path.exists `： ファイル存在チェック
- ` shutil.copy `： ファイルコピー（バックアップ用途に便利）
- ` with open(..., 'w') `： ファイル書き込み


<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




