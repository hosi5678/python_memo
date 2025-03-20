# range関数は、指定された範囲の整数を生成するイテレータを返す。
# range(start, stop, step)
# start: イテレータの開始値
# stop: イテレータの終了値
# step: イテレータの増分
# startが省略された場合、0が開始値として使用される。
# stepが省略された場合、1が増分として使用される。
# stopが省略された場合、イテレータは無限に続く。
# range関数は、for文と組み合わせて使用されることが多い。
# for i in range(5):
#     print(i) # 0 1 2 3 4
# for i in range(2, 5):
#     print(i) # 2 3 4
# for i in range(0, 10, 2):
#     print(i) # 0 2 4 6 8
# for i in range(10, 0, -2):
#     print(i) # 10 8 6 4 2
# range関数は、リストを生成するわけではないので、リストのように要素の追加や削除ができない。
# x = range(5)
# x.append(5) # AttributeError: 'range' object has no attribute 'append'
# x.clear() # AttributeError: 'range' object has no attribute 'clear'
# x[0] # TypeError: 'range' object is not subscriptable
# x[0] = 1 # TypeError: 'range' object does not support item assignment
# range関数は、イテレータを生成するため、メモリ効率が良い。
# range関数は、ジェネレータを生成するため、メモリ効率が良い。
# range関数は、イテレータを生成するため、メモリ効率が良い。

# start=int(input("開始値を入力してください:"))
# stop=int(input("終了値を入力してください:"))
# step=int(input("増分を入力してください:"))

# for i in range(start,stop,step):
#     print(i)

# n=int(input("整数を入力してください:"))
# for i in range(1,n+1,2):
#     print(i)

n=int(input("整数を入力してください:"))

# _ は、変数名として使用されるが、その値を使用しないことを示す。

for _ in range(n):
    print("*",end="")
print()
