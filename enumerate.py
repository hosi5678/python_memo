# enumerate() function is used to loop through a list, tuple, dictionary, string, etc. and return the index of the element in the list as well as the element itself.
# enumerate() function takes two parameters:
#   1. iterable: any object that supports iteration
#   2. start: the index value from which the counter is to be started, by default it is 0
#
# enumerate() function returns an enumerate object which is an iterator. You can convert this enumerate object to a list or a tuple or a set using list(), tuple(), or set() method. 
# enumerate: 列挙子
# enumerate関数は、リスト、タプル、辞書、文字列などをループ処理し、リスト内の要素のインデックスと要素自体を返します。
# enumerate関数は、2つのパラメータを取ります:
#   1. iterable: イテレーションをサポートする任意のオブジェクト
#   2. start: カウンタを開始するインデックス値。デフォルトは0です。
#
# enumerate関数は、イテレータであるenumerateオブジェクトを返します。このenumerateオブジェクトをlist()、tuple()、またはset()メソッドを使用してリスト、タプル、またはセットに変換できます。
#

n=input("input string:")

for i,str in enumerate(n):
    # print("n[{}] is {}".format(i,str))
    print(f"n[{i}] is {str}")
