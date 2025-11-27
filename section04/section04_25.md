## 25. 辞書型のメソッド
#### 💻 ターミナルで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```bash
# 辞書の作成
d = {'x':10 ,'y':20}
d                       # {'x': 10, 'y': 20}

# キー一覧を取得
d.keys()                # dict_keys(['x', 'y'])

# 値一覧を取得
d.values()              # dict_values([10, 20])

# update() で辞書をマージ（既存キーは上書き）
d2 = {'x':1000, 'j':500}
d2                      # {'x': 1000, 'j': 500}
d.update(d2)
d                       # {'x': 1000, 'y': 20, 'j': 500}

# キーを指定して値を取得
d['x']                  # 1000
d.get('x')              # 1000

# 存在しないキーを [] で参照するとエラー
d['z']                  # KeyError: 'z'

# get() なら存在しないキーは None を返す
d.get('z')              # None
r = d.get('z')
type(r)                 # <class 'NoneType'>

# pop() でキーを指定して削除しつつ値を返す
d.pop('x')              # 1000
d                       # {'y': 20, 'j': 500}

# del でキーを削除
del d['y']
d                       # {'j': 500}

# del で辞書そのものを削除
del d
# d を参照するとエラー（存在しない）
# NameError: name 'd' is not defined

# clear() で辞書を空にする
d = {'x':100 ,'y':200}
d.clear()
d                       # {}

# in 演算子でキーの存在確認
d = {'x':100 ,'y':200}
'a' in d                # False
'x' in d                # True
```

## ✨ 学習のまとめ
**辞書の値取得**   
`d['x'] `
- キーが無いと KeyError
- キーが必ず存在する前提で使う

`d.get('x')`  
- キーが無くてもエラーにならない
- デフォルト値を返せる（例：d.get('x', 0)）
- 無い可能性があるキーを扱うときに便利



<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>


