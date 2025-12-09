## 93. ファイルの読み込み
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

**文字列を準備（複数行）**
```python
s = """\
AAA
BBB
CCC
DDD
"""
```
**ファイルに書き込み**
```python
with open('test.txt', 'w') as f:
    f.write(s)
```

**ファイルを一括で読み込む方法**
```python
with open('test.txt', 'r') as f:
    print(f.read())
```

**ファイルを1行ずつ読み込む方法**
```python
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()   # 1行ずつ読み込む
        print(line, end='')   # 改行を二重にしないよう end='' を指定
        if not line:          # 空文字列ならEOF（読み込み終了）
            break
```

**ファイルを指定した文字数ずつ読み込む方法**
```python
with open('test.txt', 'r') as f:
    while True:
        chunk = 2             # 2文字ずつ読み込む
        line = f.read(chunk)  # 2文字分を取得
        print(line)           # 読み込んだ文字を表示
        if not line:          # 空文字列ならEOF（読み込み終了）
            break
```
## ✨ 学習のまとめ
- ` f.read() ` : ファイル全体を一度に読み込む。
- ` f.readline() ` : 1行ずつ読み込む。ループで使うと便利。
- ` f.read(n) ` : 指定した文字数だけ読み込む。大きなファイルを分割して処理するのに使える。


<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




