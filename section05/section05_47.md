## 47. 辞書をfor文で処理する
#### 🖥 VSCodeで実行
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
## ✨ 学習のまとめ
**items() の特徴**
- items() の返り値は dict_items（辞書の内容を映すビューオブジェクト）
- リストではないが イテラブル（反復可能） なので for k, v in d.items(): のようにループできる
- インデックスアクセス（items[0]）はできない
- 辞書が更新されると ビューの内容もリアルタイムで変わる


<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
