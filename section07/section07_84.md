## 84. クラスを構造体として扱う時の注意点
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

```python
class T:
    def __init__(self, name, age):
        # ダブルアンダースコア付き属性は名前マングリングされる
        # 実際には self._T__name という名前で保持される
        self.__name = name
        self.age = age

t = T('Nancy',10)

# 外部から __name に直接アクセスすると AttributeError になる
# print(t.__name, t.age)

# ここで「t.__name = 'XXXXXXXXX'」とすると、
# 本来の _T__name とは別に「__name」という新しい属性がインスタンスに追加される
t.__name = 'XXXXXXXXX'

# この時点で t には「_T__name」と「__name」の2つの属性が存在する
# print(t.__name, t.age) は新しく追加された __name を参照 → 'XXXXXXXXX', 10
print(t.__name, t.age)

# さらに「t.name = 'Mike'」とすると、また新しい属性「name」が追加される
# age は既存の属性なので上書きされる
t.name = 'Mike'
t.age = 20

# この時点で t には「_T__name」「__name」「name」「age」が存在する
# print(t.name, t.age) は新しく追加された name と更新された age を参照 → 'Mike', 20
print(t.name, t.age)
```

## ✨ 学習のまとめ
- 「変更できないように見える属性」でも 再定義すれば値を変えられるので注意
- 本当に変更不可にしたい場合は` @property `で読み取り専用にする


<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>




