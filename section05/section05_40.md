## 40. while else文
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```bash
# while 条件が偽になった後に else が実行される例
count = 0

while count < 5:
    # if count == 1:
    #     break   # breakすると else は実行されない
    print(count)
    count += 1
else:
    print('done')  # ループが正常終了したときに実行
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
