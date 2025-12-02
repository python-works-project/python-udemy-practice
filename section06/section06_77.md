## 77. __nameと__main__
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る</a>
</div>

**section06.py**
```python
if __name__ == '__main__':
    main()
```
section06.py を直接実行したときだけ main() が呼ばれる

**hello.py**
```python
if __name__ == '__main__':
    print('mypackage:', __name__)
```
hello.py を直接実行したときだけ動く
section06.py から import された場合は実行されない

## ✨ 学習のまとめ
- ` __name__ ` ： モジュールの名前を表す特別変数
- ` __main__ ` ： 「直接実行されたとき」の印
- ` if __name__ == "__main__" `： 直接実行されたときだけ動かす処理を書く場所
- メインプログラムでは「エントリーポイント」、呼び出されるプログラムでは「テスト用コード」に使う

<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る<a>
</div>
