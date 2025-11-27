## 55. 関数内関数
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
def outer(a, b):
    # 内側関数 plus を定義（outer のスコープ内だけで使える）
    def plus(c, d):
        return c + d

    # 何度でも呼び出し可
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

# outer を呼び出す
outer(1, 2)
```

