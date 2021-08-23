3 steps:
1. `argparse.ArgumentParser()` 物件
2. `add_argument()` 我們需要哪些引數
3. `parse_args()` 取得引數


指定argument的數量：
* `nargs=3` 剛好3個
* `nargs=?` 0或1個
* `nargs=+` 至少一個
* `nargs=*` 任意數量

```python
parser.add_argument("arg2",  
 nargs='?',  
 help="argument 2, type 1 value or none",  
 default=None)
```

`+`和`*`會用list儲存arguments

## `store_true` ON / OFF

有加該argument就是True，否則False
```python
parser.add_argument("--verbose",
	action="store_true", # 引數儲存為 boolean
	help="簡單開關的引數")
```

## Choices
必須從選項中挑選一個
```python
parser.add_argument("-v",
"--verbosity",
	type=int,
	choices=[0, 1, 2],
	help="請輸入囉唆程度")
```

## argparse.ArgumentParser的額外HELP資訊

```python
parser = argparse.ArgumentParser(
	prog="我的程式",
	description="這是用來介紹程式功能的地方",
	epilog="這是寫在 help 頁面最後面的句子")
```