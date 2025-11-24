## 28. 集合型
#### 📝 VSCodeで実行
#### 💻 ターミナルで実行
<div align="right">
  <a href="../README.md#28-集合型">READMEに戻る</a>
</div>


```bash
# 集合を作成。重複した要素は自動的に取り除かれる
a = {1, 2, 2, 3, 4, 4, 5, 6}
print(a)        # {1, 2, 3, 4, 5, 6}
print(type(a))  # <class 'set'>

# 別の集合を作成。こちらも重複は取り除かれる
b = {2, 3, 3, 6, 7}
print(b)        # {2, 3, 6, 7}

# 差集合（a にあって b にない要素）
print(a - b)    # {1, 4, 5}

# 差集合（b にあって a にない要素）
print(b - a)    # {7}

# 共通部分（積集合）
print(a & b)    # {2, 3, 6}

# 和集合（両方の要素を合わせた集合）
print(a | b)    # {1, 2, 3, 4, 5, 6, 7}

# 排他的論理和（どちらか一方にのみ含まれる要素）
print(a ^ b)    # {1, 4, 5, 7}
```

<div align="right">
  <a href="../README.md#28-集合型">READMEに戻る</a>
</div>


