#変数に対する代入を行っても値の変更が行われるわけではなく、新しいオブジェクトが生成される
#そのため、変数が参照しているオブジェクトのIDは変わる
#変数が参照しているオブジェクトのIDを取得するにはid()関数を使用する
#id()関数は、引数に指定したオブジェクトのIDを返す
#id()関数は、オブジェクトのIDを表す整数値を返す
#id()関数は、オブジェクトのIDを取得するため、引数には変数を指定する
#id()関数は、変数が参照しているオブジェクトのIDを取得する


n=17
print(id(17))
print(id(n))

n="abc"
print(id("abc"))
print(id(n))
