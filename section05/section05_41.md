## 41. input関数
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# 入力が 'OK' になるまで繰り返す
while True:
    word = input('Enter:')
    if word == 'OK':
        break
    print('next')


# 入力が '10' になるまで繰り返す
while True:
    Num = input('Enter:')
    if Num == '10':
        break
    print('next')
```
## 📝 学習のまとめ
- `input([prompt])` : ユーザーから入力を受け取る関数  
- **返り値は常に文字列 (`str`)**  
- 数値として使う場合は `int()` や `float()` で型変換が必要  

#### 使用例
```python
# 文字列入力
name = input("名前を入力してください: ")
print("こんにちは,", name)

# 数値入力（型変換）
age = int(input("年齢を入力してください: "))
print("来年は", age + 1, "歳ですね")
```
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
