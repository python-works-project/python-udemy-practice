## 61. 辞書内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
w = ['Mon', 'Tue', 'Wen']
f = ['coffee', 'Milk', 'Water']

# for文 + zip で辞書を作成
d = {}
for x, y in zip(w, f):      # 対応する要素をペアに取り出す
    d[x] = y                # キーに曜日、値に飲み物を登録
print(d)                    # {'Mon': 'coffee', 'Tue': 'Milk', 'Wen': 'Water'}
```
**辞書内包表記で同じ処理を簡潔に書く**
```python
d = {x: y for x, y in zip(w, f)}  # zipでペアを作り、キー:値の辞書を生成
print(d)                          # {'Mon': 'coffee', 'Tue': 'Milk', 'Wen': 'Water'}
```
## ✨ 学習のまとめ
- 

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
