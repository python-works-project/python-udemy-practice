## 65. 例外処理
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
l = [1, 2, 3]
i = 5

# l[i]  # インデックスが範囲外 → IndexError
# del l # リスト自体を削除 → NameError（変数が未定義になる）

try:
    l[i]               # インデックス 5 は存在しない → IndexError が発生
    # () + l           # タプルとリストは足せない → TypeError が発生
    # l[0]             # コメントアウトを外せば正常に動作（値 1 を返す）
except IndexError as ex:
    # インデックス範囲外のときにここに入る
    print("IndexError: {}".format(ex))
except NameError as ex:
    # 変数が存在しないときにここに入る
    print("NameError: {}".format(ex))
except Exception as ex:
    # その他の例外（TypeErrorなど）はここに入る
    print("Exception: {}".format(ex))
else:
    # tryブロックで例外が出なかった場合に実行される
    print('done')
finally:
    # 例外の有無に関わらず必ず実行される
    print("clean up")
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
