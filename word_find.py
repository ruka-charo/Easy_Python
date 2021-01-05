#%%正規表現
import re

word_list = ['Apple','Goodbye','Thankyou']
find_list = ['Hello','Goodbye','Thankyou']

for word_1 in word_list:
    print('------')
    a = re.compile(word_1)

    for word_2 in find_list:
        #コンパイルした文字でsearchする。
        b = a.search(word_2)

        if b == None:
            m = '×'
        else:
            m = '○'

        msg = '(パターン)' + word_1 + '文字列' + word_2 + '(マッチ)' + m
        print(msg)

#%%pra
import re

#一つの''の塊で検索している
a = re.compile('に')
b = a.search('こんにちは')
print(b)

#%%正規表現（行頭、行末）
import re

word_list = ['TXT','^TXT','TXT$','^TXT$']
find_list = ['TXT','TXTT','TXTTT','TTXT']

for word_1 in word_list:
    print('------')
    a = re.compile(word_1)

    for word_2 in find_list:
        b = a.search(word_2)

        if b == None:
            m = '×'
        else:
            m = '○'

        msg = '(パターン)' + word_1 + '文字列' + word_2 + '(マッチ)' + m
        print(msg)

#%%正規表現(.による任意の一文字)
import re

word_list = ['TXT.','TXT..','.TXT','..TXT']
find_list = ['TXT','TXTT','TXTTT','TTXT','TTTXT']

for word_1 in word_list:
    print('------')
    a = re.compile(word_1)

    for word_2 in find_list:
        b = a.search(word_2)
        if b == None:
            m = '×'
        else:
            m = '○'

        msg = '(パターン)' + word_1 + '文字列' + word_2 + '(マッチ)' + m
        print(msg)

#%%文字クラス
import re

word_list = ['[012]','[0-3]','[^012]']
find_list = ['0','1','2','3']

for word_1 in word_list:
    print('------')
    a = re.compile(word_1)

    for word_2 in find_list:
        b = a.search(word_2)
        if b == None:
            m = '×'
        else:
            m = '○'

        msg = '(パターン)' + word_1 + '文字列' + word_2 + '(マッチ)' + m
        print(msg)

#%%繰り返しを表す正規表現
import re

word_list = ['T*','T+','T?','T{3}']
find_list = ['X','TT','TTT','TTTT']

for word_1 in word_list:
    print('------')
    a = re.compile(word_1)

    for word_2 in find_list:
        b = a.search(word_2)
        if b == None:
            m = '×'
        else:
            m = '○'

        msg = '(パターン)' + word_1 + '文字列' + word_2 + '(マッチ)' + m
        print(msg)

#%%グループ化と選択
import re

word_list = ['(TXT)+','TXT|XTX']
find_list = ['TX','TXT','XTX','TXTXT']

for word_1 in word_list:
    print('------')
    a = re.compile(word_1)

    for word_2 in find_list:
        b = a.search(word_2)
        if b == None:
            m = '×'
        else:
            m = '○'

        msg = '(パターン)' + word_1 + '文字列' + word_2 + '(マッチ)' + m
        print(msg)

#%%正規表現と置換
import re

words_1 = '\.(csv|html|py)$'
words_2 = ['Sample.csv','Sample.exe','test.py','index.html']

a = re.compile(words_1)

for word_2 in words_2:
    b = a.sub('.txt',word_2)

    print('変更前：',word_2,'変更後：',b)
    
