#p.90
#%%3
for i in range(9):
    for j in range(9):
        print((i + 1) * (j + 1),end = '\t')
    print()

#%%3-2
for i in range(9):
    for j in range(9):
        print((i + 1) * (j + 1),'\t',end = '')
    print()

#%%4
for i in range(5):
    print((i + 1) * '*')
    print()

#p.136
#%%1
score = [74,85,69,77,81]

print('テストの点は',score,'です。')
print('最高点は',max(score),'です。')
print('最低点は',min(score),'です。')
print('平均点は',sum(score) / len(score),'です。')

#2
print('昇順は',sorted(score),'です。')
print('降順は',sorted(score,reverse=True),'です。')

#3
n_score = [n for n in score if n >= 80]
print('80点以上は',n_score,'です。')
print('80点以上の人数は',len(n_score),'です。')

#%%4
city = ['東京','名古屋','大阪','京都','福岡']
max_t = [32,28,27,26,27]
min_t = [25,21,20,19,22]

print('都市名データは',city,'です。')
print('最高気温のデータは',max_t,'です。')
print('最低気温のデータは',min_t,'です。')

for c,m,n in zip(city,max_t,min_t):
    print(c,'の最高気温は',m,'最低気温は',n,'です。')

#p.209
#%%1
def rpast(num):
    print('*' * num)

num = int(input('*を表示する個数を選んでください。:'))
rpast(num)

#%%2
def rpstr(num,str = '*'):
    print(str * num)

word = input('文字列を入力してください。:')
num = int(input('個数を入力してください。:'))

if word != '':
    print('文字列あり---')
    rpstr(num,word)
else:
    print('文字列なし---')
    rpstr(num)

#%%3
def num_count(x):
    while True:
        yield x
        x += 1

a = int(input('開始値(整数)を入力してください。:'))
b = int(input('停止値(整数)を入力してください。:'))

n = num_count(a)

for m in n:
    if b <= m:
        break
    print(m)
#for i in range(b - a):
    #print(next(n))

#%%p .256
class Car:
    def __init__(self,number,gasoline):
        self.number = number
        self.gasoline = gasoline

car_1 = Car(1234,25.5)
car_2 = Car(2345,30.5)

print('ナンバーは',car_1.number,'ガソリン量は',car_1.gasoline,'です。')
print('ナンバーは',car_2.number,'ガソリン量は',car_2.gasoline,'です。')

#%%p.284
import re

file_list = ['Sample.csv','Sample.exe','Sample1.py','Sample2.py','Sample.txt','index.html']

print('ファイルのリストは以下です。')
for file in file_list:
    print(file)

a = input('拡張子を入力してください。')
a_com = re.compile(a)

print('該当するファイルのリストは以下です。')
for file in file_list:
    b = a_com.search(file)

    if b == None:
        pass
    else:
        print(file)

#p.315
#%%1
import os
import os.path

file_info = os.listdir('.')

print('名前\t\tサイズ')
for file_name in file_info:
    file_size = os.path.getsize(file_name)
    print(file_name,'\t',file_size,'バイト')

#%%2
import os
import os.path
import datetime

file_name = os.listdir('.')

print('名前\t\t最終アクセス時刻')
for file_name in file_info:
    file_timestamp = os.path.getatime(file_name)
    file_time = datetime.datetime.fromtimestamp(file_timestamp)
    print(file_name,'\t',file_time)

#p.340
#%%1
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS product')

c.execute('CREATE TABLE product("name(商品名)" CHAR(20),"num(在庫)" INT)')
c.execute('INSERT INTO product VALUES("みかん",80)')
c.execute('INSERT INTO product VALUES("いちご",60)')
c.execute('INSERT INTO product VALUES("りんご",22)')
c.execute('INSERT INTO product VALUES("もも",50)')
c.execute('INSERT INTO product VALUES("くり",75)')

conn.commit()

itr = c.execute('SELECT * FROM product')

for row in itr:
    print(row)

conn.close()

#%%2
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

itr = c.execute('SELECT * FROM product WHERE "num(在庫)" <= 30')

for row in itr:
    print(row)

conn.close()

#p.367
#%%1
import matplotlib.pyplot as plt

data = [8,17,0,11,6,21,16,6,17,11,7,9,6,13,12,16,3,14,13,12]

plt.title('Histogram')

plt.xlabel('value')
plt.ylabel('frequency')

plt.hist(data,bins = 8,color = 'm')
plt.show()

#%%2
import random
import matplotlib.pyplot as plt

x = []
y = []

for i in range(100):
    x.append(random.randint(1, 50))
    y.append(random.randint(1, 50))

#plt.axis([-100,100,-100,100])
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.scatter(x,y,marker = 'x')
plt.show()

#%%3
import matplotlib.pyplot as plt

data = []

for i in range(1000):
    data.append(random.normalvariate(0,10))

plt.title('Histogram')

plt.hist(data,bins = 50)
plt.show()

#%%4
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8,8,0.01)
y_1 = 3 * x + 5
y_2 = x ** 2

plt.title('y=f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.plot(x,y_1)
plt.plot(x,y_2)

plt.show()

# p.394
#%%1
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x,y = datasets.make_regression(n_samples=200, n_features=1, noise=15)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train, y_train)
print('回帰係数は', e.coef_, 'です。')
print('切片は', e.intercept_, 'です。')

y_pred = e.predict(x_test)

print('学習データによる決定係数は', e.score(x_train, y_train), 'です。')
print('テストデータによる決定係数は', e.score(x_test, y_test), 'です。')

plt.scatter(x_train, y_train, label='train')
plt.scatter(x_test, y_test, label='test')
plt.plot(x_test, y_pred, color='m')
plt.legend()

plt.show()

#%%2
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

data, label = datasets.make_blobs\
(n_samples=600, n_features=2, centers=4, cluster_std=0.75)

e = cluster.KMeans(n_clusters=4)
e.fit(data)

print(e.labels_)
print(e.cluster_centers_)

plt.scatter(data[:, 0],data[:, 1], marker='o', c=e.labels_, edgecolor='k')
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker='x')

plt.show()
