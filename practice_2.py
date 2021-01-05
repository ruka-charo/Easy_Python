#%%クラス変数・クラスメソッド

class Person:
    #クラス変数
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1

    def __str__(self):
        str = self.name + 'さん'
        return str

    @classmethod
    def getCount(cls):
        return cls.count

class Customer(Person):
    def __init__(self,name,age,adress,tel):
        super().__init__(name,age)
        self.adress = adress
        self.tel = tel


pr1 = Person('柏木',22)
pr2 = Person('佐倉',21)
cus1 = Customer('倉崎',24,'Tokyo','080')

print(pr1.name,'さんは',pr1.age,'才です。')
print(pr2.name,'さんは',pr2.age,'才です。')
print('合計人数は',Person.getCount(),'人です。')

print(str(pr1))

print(cus1.name,'さんは',cus1.age,'才です。'\
,cus1.adress,'在住で、携帯電話は',cus1.tel,'です。')

#%%標準ライブラリ
#カレンダー
import calendar

c = calendar.TextCalendar()
c.pryear(2020)
c.prmonth(2020,12)

#文字列の基本操作
word = input('何か言葉を入れてください。:')

print('入力した言葉は',word,'です。')
print('最初の文字は',word[0],'です。')
print('逆順にすると',word[::-1],'です。')
print('文字数は',len(word),'です。')

#%%format()の基本
'{0}は{1}が好きです。{0}は{2}も好きです。'.format('私','犬','東京')
'{key1}支店の{key2}です。'.format(key1 = '東京',key2 = '売り上げ')
#カンマ区切りの数字を入力
'{:,}円'.format(1000)
#２進数表記
'{:b}'.format(21)

#%%文字列の検索
word = input('文字列を入力してください。')
find_word = input('検索したい文字を入力してください。')

num = word.find(find_word)

if num != -1:
    print(word,'の',num + 1,'番目に',find_word,'がありました。')
else:
    print('見つかりませんでした。')

#%%文字列の置換
word = 'こんにちは'
old = 'にち'
new = 'ばん'

word.replace(old, new)

#%%ファイルへの書き込み
f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sample.txt','w')

f.write('こんにちは\n')
f.write('さようなら\n')

f.close()

#%%ファイルの読み込み
f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sample.txt','r')
lines = f.readlines()

for line in lines:
    print(line,end = '')

f.close()

#%%csvファイルの読み書き
import csv

f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sample.csv','r')
rd = csv.reader(f)

#→
for row in rd:
    #↓
    for col in row:
        print(col,end = ',')
    print()

f.close()

#%%
import csv

f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sample_2.csv','w')
w = csv.writer(f)

w.writerow(['東京','消しゴム'])
w.writerows([['東京','消しゴム'],['名古屋','ノート']])

f.close()

#%%JSONファイルの読み込み
import json

f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sample.json','r')
data = json.load(f)
print(data)

f.close()

#%%JSONファイルの書き込み
import json

f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sample_2.json','w')
json.dump({'東京':30,'大阪':20},f,ensure_ascii=False)

f.close()

#%%例外処理
#例外の発生を調べる文
try:
    f = open('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/Python/Easy_Python/Sampleq.txt','r')

#例外が起きた時の処理
except FileNotFoundError:
    print('ファイルを開けませんでした。')
#except (FileNotFoundError,FileExixtsError): 複数同じ処理ができる
#except: 全ての例外に対して処理ができる

#例外が起きなかった時の処理
else:
    lines = f.readlines()
    for line in lines:
        print(line,end = '')
    f.close()

#必ず最後に行う処理
finally:
    print('処理を終了します。')

#%%例外クラスの定義
class MyExcepution(RuntimeError):
    pass

raise MyExcepution

#%%システム処理
import os

os.getcwd()
curdir = os.listdir('.')

for name in curdir:
    print(name)

#%%ファイル情報の取得
import os
import os.path

dir = os.listdir('/Users/rukaoide/Library/Mobile Documents/com~apple~CloudDocs/Documents/数理系')

for name in dir:
    print(os.path.abspath(name),end = '')

    if (os.path.isfile(name)):
        print('ファイルです。')
    else:
        print('ディレクトリです。')

#%%日付と時刻
import datetime

#datetimeモジュールのdatetimeクラスのnow()メソッド
dt = datetime.datetime.now()
#dt = datetime.date.today()
print('現在は',dt,'です。')
print('年：',dt.year)
print('月：',dt.month)
print('日：',dt.day)

dt += datetime.timedelta(days=100)
print('100日後は',dt,'です。')

#日付情報のフォーマット
dt_2 =dt.strftime('%c')
print(dt_2)

dt_3 = dt.strftime('%Y-%m-%d')
print(dt_3)

#%%練習
import datetime

my_birthday = datetime.date(1996,1,20)
bro_birthday = datetime.date(1999,9,18)

my_birthday.strftime('%Y-%m-%d-%A')
bro_birthday.strftime('%Y-%m-%d-%A')

#%%データベース
import sqlite3

conn = sqlite3.connect('pdf.db')

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS product")

#「''」のなかに「''」を使用したい場合は「""」を使う。
#同じのものを同一の行で使うとエラーになる。
c.execute('CREATE TABLE product(name CHAR(20),price INT)')
c.execute('INSERT INTO product VALUES("鉛筆",80)')
c.execute('INSERT INTO product VALUES("消しゴム",50)')
c.execute('INSERT INTO product VALUES("定規",200)')
c.execute('INSERT INTO product VALUES("コンパス",300)')
c.execute('INSERT INTO product VALUES("ボールペン",100)')

conn.commit()

itr = c.execute('SELECT * FROM product')

for row in itr:
    print(row)

conn.close()

#%%条件をつけて絞り込み
import sqlite3

conn = sqlite3.connect('pdf.db')
c = conn.cursor()

#条件設定
itr = c.execute('SELECT * FROM product WHERE price >= 200')
itr_2 = c.execute('SELECT * FROM product WHERE name == "鉛筆"')

for row in itr:
    print(row)

for row_2 in itr_2:
    print(row_2)

conn.close()

#%%データの一部から検索する
import sqlite3

conn = sqlite3.connect('pdf.db')
c = conn.cursor()

itr_3 = c.execute('SELECT * FROM product WHERE name LIKE "%ン%"')

for row_3 in itr_3:
    print(row_3)

conn.close()

#%%データの並び替え
import sqlite3

conn = sqlite3.connect('pdf.db')
c = conn.cursor()

itr_4 = c.execute('SELECT * FROM product ORDER BY price DESC')

for row_4 in itr_4:
    print(row_4)

conn.close()

#%%URLを読み込む
import urllib.request

page = urllib.request.urlopen('https://www.python.org/')

html = page.read()
word = html.decode()

print(word)

#%%HTMLの解析
import urllib.request
from html.parser import HTMLParser

#解析の定義
class SampleHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = False

    def handle_starttag(self,tag,attrs):
        if tag == 'title':
            self.title = True

    def handle_data(self,data):
        if self.title is True:
            print('タイトル：',data)
            self.title = False

#ページ読み込み
page = urllib.request.urlopen('https://www.python.org/')

html = page.read()
word = html.decode()

#解析実行
p = SampleHTMLParser()
p.feed(word)

p.close()
