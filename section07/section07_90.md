## 90. 特殊メソッド
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

```python
class Word(object):
    def __init__(self, text):
        self.text = text                               # インスタンス生成時に文字列を保持

    def __str__(self):
        return 'word!!!!!!!!'                          # print() で表示される文字列を定義

    def __len__(self):
        return len(self.text)                          # len() 関数で返す値を定義

    def __add__(self, word):
        return self.text.lower() + word.text.lower()   # 小文字に変換して連結

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()  # 小文字に変換して比較

# インスタンス生成
w = Word('test')
w2 = Word('#########')
w3 = Word('#########')

print(w)          # __str__ が呼ばれる → "word!!!!!!!!"
print(len(w))     # __len__ が呼ばれる → 4（'test' の長さ）
print(w + w2)     # __add__ が呼ばれる → "test#########"
print(w == w2)    # __eq__ が呼ばれる → False
print(w2 == w3)   # __eq__ が呼ばれる → True（両方 '#########'）
```


