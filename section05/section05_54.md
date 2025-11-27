## 54. Docstrings
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
def example_func(param1, param2):
    """
    example_func の Docstring
    :param param1: 説明
    :param param2: 説明
    """
    print(param1, param2)
    return True

# __doc__ 属性で docstring を直接参照できる
print(example_func.__doc__)

# help() を使うと docstring が整形されて表示される
help(example_func)
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
