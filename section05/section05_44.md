## 44. range関数
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_list:
    print(i)

# rangeで0〜9を処理
for i in range(10):
    print(i)

# rangeで2〜9を処理
for i in range(2, 10):
    print(i)

# rangeで2から9まで3刻みで処理
for i in range(2, 10, 3):
    print(i)

# 0〜9と文字列を同時に出力
for i in range(10):
    print(i, 'Hello')

# 変数を使わず繰り返し
for _ in range(10):
    print('Hello')
```
## ✨ 学習のまとめ
- `for _ in range(n):` と書くことで、ループ変数を使わずに繰り返し処理ができる  
- `_` は「値を使わない」ことを示す慣習的な書き方  
- 例: 10回だけ同じ処理を繰り返す
```python
for _ in range(10):
    print('Hello')
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
