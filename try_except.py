# author: zhuangyuan time:2020/11/3
a = "A"


def func():
    # you cannot use the global 'a' because...
    a = 'bbb'
    print("BIG"+a)
    print('A' + a)


func()

