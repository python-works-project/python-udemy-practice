## 47. 辞書をfor文で処理する
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
d = {'x': 100, 'y': 200}

# 辞書をループすると「キー」が順に取り出される
for v in d:
    print(v)

# items() を使うと「キーと値」を同時に取り出せる
for k, v in d.items():
    print(k, ':', v)

# items() は (キー, 値) のタプルの集合を返す
print(d.items())
```
## 📝 学習のまとめ
#### items() の特徴まとめ
- 辞書の キーと値のペア(タプルの集合)を返す
- `items()` の返り値は dict_items というビューオブジェクト（リストではないがループ可能）
- ループで キーと値を同時に取り出すのに最適
- 辞書の内容が変わると items() の結果もリアルタイムで変わる（ビューオブジェクト）


<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
