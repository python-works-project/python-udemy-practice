## 29. 集合型のメソッド
#### 💻 ターミナルで実行
<div align="right">
  <a href="../README.md#29-集合型のメソッド">READMEに戻る</a>
</div>


```bash
# 集合を作成。重複は自動的に取り除かれる
s = {1, 2, 3, 4, 5}
print(s)  # {1, 2, 3, 4, 5}

# 集合は「順序なし」なのでインデックス指定はできない
# s[0] とするとエラーになる
# TypeError: 'set' object is not subscriptable

# 要素を追加
s.add(6)
print(s)  # {1, 2, 3, 4, 5, 6}

# 同じ要素を追加しても集合なので重複は無視される
s.add(6)
print(s)  # {1, 2, 3, 4, 5, 6}

# 要素を削除
s.remove(6)
print(s)  # {1, 2, 3, 4, 5}

# 全要素を削除（空集合になる）
s.clear()
print(s)  # set()

# 集合の場合
s = {1, 2, 3}
s.clear()           # 全要素を削除
print(s)            # set() → 空集合を表す特殊な表示

# 辞書の場合
a = {}              # {} は「空の辞書」として解釈される
print(type(a))      # <class 'dict'>
print(a)            # {} → 空の辞書を表す
```

## 📝 学習のまとめ
- 

<div align="right">
  <a href="../README.md#29-集合型のメソッド">READMEに戻る</a>
</div>


