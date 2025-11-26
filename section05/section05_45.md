## 45. enumerate関数
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# インデックスを手動で管理する方法と enumerate を使う方法
i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
```
## 📝 学習のまとめ
- `enumerate` は要素とインデックスを同時に取得できる
- 構文: `enumerate(iterable, start=0)`
- `start` で開始番号を指定可能（デフォルトは 0）
- `range(len(...))` より可読性が高い

### 使い方例
```python
fruits = ["apple", "banana", "cherry"]

for i, v in enumerate(fruits, start=1):
    print(i, v)
```
出力:
1 apple
2 banana
3 cherry

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
