# イテラブルとイテレータ

---
<div align="right"><a href="../README.md#5-その他">◀️READMEに戻る</a></div>

### ` イテラブル `

- 繰り返し可能なオブジェクト
- for 文で回せるもの
- for 文は内部で` iter() `と` next() `を自動で呼んでいる
- ` __iter__() `メソッドを持っている
- 例: ` リスト `、` タプル `、`  文字列 `、` 辞書 `、` 集合 `、` range() `など

### { イテレータ `
- 実際に値を1つずつ取り出す仕組みを持つオブジェクト
- ` __iter__() `と` __next__() `メソッドを持っている
- ` next() `を呼ぶと次の値を返し、最後まで行くと` StopIteration `を出す

```python
nums = [10, 20, 30]   # リスト → イテラブル

it = iter(nums)       # イテラブルからイテレータを作成

print(next(it))  # → 10
print(next(it))  # → 20
print(next(it))  # → 30
print(next(it))  # → StopIteration が発生
```
