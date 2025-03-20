# tuple,dictionary, set

# タプルについて
# タプルはリストと同じように複数の要素を格納することができるが、要素の追加、削除、変更ができない
# タプルは()で囲む
# t = (1, 2, 3, 4, 5)
# print(t) # (1, 2, 3, 4, 5)
# print(type(t)) # <class 'tuple'>

# tuple16=divmod(13,3)

# print(tuple16) # (4, 1)

# tupleのpackについて
# packは、複数の変数をまとめて1つの変数に格納することを指す。

pack=1,2,3,4


# dir()関数はPythonの標準関数です。
# dir()を使うと、そのオブジェクトが対象の変数や関数、オブジェクトなどのつまり属性をリストで返してくれます。

# （＊属性（attribute）とはオブジェクトに存在する変数や関数のこと）

# dir()を使うことで、dir()の引数に渡したパッケージやモジュールの持つ全ての属性を取得することが出来る関数です。


print(dir(pack))
print(pack.__len__())
# print(pack)

# tupleのunpackについて
# unpackは、packを分解する

# a,b,c,d=pack

# print(a)

a,_,c,_=pack

print(c)
