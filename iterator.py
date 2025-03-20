# iterable:
#   __iter__(): return an iterator object
# iterator:
#   __next__(): return the next item
#   __iter__(): return itself
#   raise StopIteration when there is no more item
#   can only be iterated once
#   can be used in for loop
#   can be used in list(), tuple(), set(), dict(), etc.

# dir(): mothods and attributes of an object
# hasattr(obj, attr): check if an object has an attribute
# getattr(obj, attr): get the value of an attribute
# setattr(obj, attr, value): set the value of an attribute
# delattr(obj, attr): delete an attribute
# isinstance(obj, cls): check if an object is an instance of a class
# issubclass(cls, cls): check if a class is a subclass of another class

# c={1,2,3,4}

# it=iter([1,2,3,4])

# print(next(it))

# print(dir(a))
# a.__next__()
# # a.__next__()
# b=a

# # b=next(a)
# print(b)

# next(a)
# print(a)

# b=[1,2,3,4]
# print(dir(b))


# for文の仕組み

# for文は、実は iter next StopIteration を使ったwhile文の形で表現できます。具体的には、

# for x in [0,1,2]:
#     print(x)

# 0
# 1
# 2

# このfor文は、次のwhile文と等価です。

try:
    it = iter([0,1,2])
    print(it) # __repr__が呼ばれる。メモリアドレスが表示される。
    while True:
        x = it.__next__()
        print(x)
except StopIteration:
    pass

# 0
# 1
# 2

# このように、for文は、iter next StopIteration を使ったwhile文の形で表現できます。

# イテラブルとは、iterメソッドを持つオブジェクトのことです。イテラブルは、for文で反復処理できます。
# イテラブルオブジェクトを組み込み関数iterに渡すと、イテレータオブジェクトが返ります。
