#%%エスケープシーケンス
print('\\')
print('1\t2\t3\t4')

#%%if else条件演算子
a = input('売り上げは好調ですか？○/×:')
ans = '好調' if (a == '○') else '普通'
print(ans)

#%%ネスト
v = False

for i in range(5):
    for j in range(5):
        if v is False:
            print('*',end = '')
            v = True
        else:
            print('-',end = '')
            v = False
    print()

#%%出力の末尾
print('1\t2\t3',end = ',')

#%%for文2
list_num = [1,4,2,8,3]

for i in list_num:
    print(i,end = '')

#%%リスト
list_num = [1,4,2,8,3]
del list_num[0]
print(list_num)

list_num_2 = list_num.copy()
print(list_num_2)

#%%スライス
list_num_3 = [1,2,3,4,5,6,7,8,9,10]
list_num_3[0:6]
list_num_3[6:]
list_num_3[::2]
list_num_3[::-1]
list_num_3[::-2]

list_num_3[7:] = [18,19,20]
list_num_3[7:]

del list_num_3[6:]
print(list_num_3)

#%%逆順の色々
list_num_4 = [1,2,3,4,5]

#スライスを用いた逆順
for num in list_num_4[::-1]:
    print(num)
print(list_num_4)
print('出力は逆順になるが、リストが変更されたわけではない。')

#reversed()関数を用いた逆順
for num in reversed(list_num_4):
    print(num)
print (list_num_4)
print(reversed(list_num_4))
print('出力は逆順になるが、リストは変更されない。関数文を出力しようとするとできない。')

#.reverseメゾッドを用いた逆順
list_num_4.reverse()
print(list_num_4)
print('リスト自体を逆順にする')

#%%イテレータ
it = iter(list_num_4)
print(next(it))
print(next(it))
print(next(it))

rv = reversed(list_num_4)
print(next(rv))
print(next(rv))
print(next(rv))

#%%リスト要素の組み合わせ
city = ['東京','名古屋','大阪','京都']
sale = [80,60,22,50,75]

print('都市名データは',city,'です。')
#print('都市名データは' + str(city) + 'です。')
print('売り上げデータは',sale,'です。')

#データの組み合わせ
for d in zip(city,sale):
    print(d)

#データとインデックスの組み合わせ
for d in enumerate(city):
    print(d)

#アンパック(リストの分解)
for c,s in zip(city,sale):
    print('都市名データは',c,'売り上げデータは',s,'です。')

list_num_5 = [1,2,3]
d_1,d_2,d_3 = list_num_5
print(d_1,d_2,d_3)

#%%リスト内包表記
data = [1,2,3,4,5]
print('現在のデータは',data,'です。')

n_data = [n * 2 for n in data if n != 3]
print('新しいデータは',n_data,'です。')

#%%リスト集計と並び替え
sale = [80,60,22,50,75]

print('現在のデータは',sale,'です。')
print('最大値は',max(sale))
print('最小値は',min(sale))
print('合計は',sum(sale))
print('昇順並び替えは',sorted(sale))
print('降順並び替えは',sorted(sale,reverse = True))

#リスト自体をソート
sale.sort()
print(sale)
sale.sort(reverse = True)
print(sale)


#%%多次元リスト（リストのリスト化）
data = [
    ['東京',32,25],
    ['名古屋',28,21],
    ['大阪',27,20],
    ['京都',26,19],
    ['福岡',27,22]
]

print('現在のデータは',data,'です。')

for dat in data:
    print('都市別のデータは',dat,'です。')

    for d in dat:
        print(d,end = '\t')
    print()

print(data[0][0],'の最高気温は',data[0][1],'最低気温は',data[0][2],'です。')

#%%タプル作成
t_1 = (1,2,3)
t_2 = 1,2,3
t_3 = tuple([1,2,3])
t_emp = tuple()
print(t_1,t_2,t_3,t_emp)

#タプルでできる操作例
#for文
for num in t_1[::-1]:
    print(num)

#スライス
t_1[1:]
t_1[::-1]

#逆順
sorted(t_1,reverse=True)

#zip()
t_1 = ('東京','京都','沖縄')
t_2 = ('日本の首都','和の境地','もはや外国')

for a,b in zip(t_1,t_2):
    print(a,'は',b,'である。')

for c in zip(t_1,t_2):
    print(c)

#enumerate()
for d in enumerate(t_1):
    print(d)

#%%ディクショナリー作成
dict_1 = {'ゲーム':'機械','万年筆':'文房具','ベッド':'家具'}
#dict_2 = dict('ゲーム' = '機械','万年筆' = '文房具','ベッド' = '家具')
dict_3 = dict((('ゲーム','機械'),('万年筆','文房具'),('ベッド','家具')))
dict_4 = dict({'ゲーム':'機械','万年筆':'文房具','ベッド':'家具'})

print(dict_1,dict_3,dict_4)

#要素の削除
del dict_3['ゲーム']
print(dict_3)

#キーがあるかないか
'ゲーム' in dict_1
'スポーツ' in dict_1

#%%0や空のデータがあるかの判別
data = [0,1,2,4,7]
#一個でも0がある → True
any(data)
#一個も0がない → True
all(data)

#%%高度な操作
sale = {'東京':80,'名古屋':60,'京都':22,'大阪':50,'福岡':75}
print('現在のデータは',sale,'です。')

#キーの取得
for k in sale.keys():
    print(k,end = '\t')
print()

#値の取得
for v in sale.values():
    print(v,end = '\t')
print()

for i in sale:
    print(sale[i],end = '\t')
print()

#キーと値の表示
for i in sale.items():
    print(i,end = '')
print()

#%%ディクショナリー同士の追加
sale_1 = {'東京':80,'名古屋':60,'京都':22}
sale_2 = {'京都':100,'大阪':50,'福岡':75}

print('１のデータは',sale_1)
print('２のデータは',sale_2)
sale_1.update(sale_2)
print('更新したデータは',sale_1)

#%%セット
city = {'東京','名古屋','京都','大阪','福岡'}

city.add('北海道')
city.remove('大阪')
print(city)

#%%集合演算
city_1 = {'東京','名古屋','京都','大阪'}
city_2 = {'京都','大阪','福岡'}

print('city_1の都市は',city_1)
print('city_2の都市は',city_2)

print('共通するデータは',city_1 & city_2)
print('和集合は',city_1 | city_2)
print('city_1のみにあるデータは',city_1 - city_2)
print('片方にしかないデータは',city_1 ^ city_2)

#%%可変長引数
def func(*args):
    print(args)

func(1,2,3,4,5)

def func(**kwargs):
    print(kwargs)

func(a = 1,b = 2,c = 3,d = 4,e = 5)

#%%複数の戻り値を持つ関数
def sell():
    y = 2020
    m = 12
    d = 24
    print(y,'年',m,'月',d,'日に販売が行われました。')
    return y,m,d

sy,sm,sd = sell()
print('販売完了：',sy,sm,sd)

#%%関数をリストに代入する
def append():
    print('データを追加します。')

def update():
    print('データを更新します。')

def delete():
    print('データを削除します。')

list = [append,update,delete]

list[0]()
list[1]()
list[2]()

#%%lambda関数
#式の形で記述できる簡単な関数を名前を付けずに作成できる
a = lambda x: x ** 2
a(3)

data = [1,3,5,7,9]

for d in map(lambda x: x ** 2,data):
    print(d)

#リスト内包表記を使うと
for d in [x ** 2 for x in data]:
    print(d)

#%%デコレータで機能を追加
def deco(func):
    def wrapper(x):
        wx = '---' + x + '---'
        return func(wx)
    return wrapper

@deco
def printmsg(x):
    print(x,'を入力しました。')

str = input('メッセージを入力してください。')

printmsg(str)

#%%ジェネレータ
def makex(x):
    while True:
        yield x
        x += 1

n = makex(0)
print(next(n))
print(next(n))

#%%ローカル変数、グローバル変数

#グローバル変数
a = 0

def funcB():
    #ローカル変数
    b = 1
    #global d   関数内でのグローバル変数の定義
    #d = 3

    print('funcBの中では、aとbの変数が使えます。')
    print('他の関数のローカル変数は使えません。')
    print('a：',a,'b：',b)

def funcC():
    #ローカル変数
    c = 2

    print('funcCの中ではaとcの変数が使えます。bは使えません。')
    print('a：',a,'c：',c)


print('関数の外ではaが使えます。b,cは使えません。')
print('a：',a)

funcB()
funcC()

#%%dir()関数による名前の取得
a = 5
def cal():
    x = 3
    y = 4
    print(dir())
    return x * y + 1

print(a + cal())

#%%記憶寿命
a = 0

def func():
    global a
    b = 0

    print('変数aは',a,'変数bは',b)

    a += 1
    b += 1

for i in range(5):
    func()

print('変数aはグローバル変数なので、プログラムが終わるまで値を保持できる。')
print('変数bはローカル変数なので、関数が終了すると値がリセットされる。')
