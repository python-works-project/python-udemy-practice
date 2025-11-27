## 39. while文とcontinue文とbreak文
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# 基本パターン
count = 0
while count < 5:
    print(count)
    count += 1

# break/continue で制御するパターン
count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
