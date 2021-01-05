#%%統計指標を得る
import statistics

data = [8,17,0,11,6,21,16,6,17,11,7,9,6,13,12,16,3,14,13,12]

print('平均値は',statistics.mean(data),'です。')
print('中央値は',statistics.median(data),'です。')
print('最頻値は',statistics.mode(data),'です。')
print('分散は',statistics.pvariance(data),'です。')
print('標準偏差は',statistics.pstdev(data),'です。')

#%%ヒストグラム
import matplotlib.pyplot as plt

data = [8,17,0,11,6,21,16,6,17,11,7,9,6,13,12,16,3,14,13,12]

plt.title('Histogram')

plt.xlabel('value')
plt.ylabel('frequency')

#plt.hist(data)
plt.hist(data,bins = max(data))
plt.show()

#matplotlibで日本語を表示
import matplotlib.pyplot as plt

data = [8,17,0,11,6,21,16,6,17,11,7,9,6,13,12,16,3,14,13,12]

plt.rcParams["font.family"] = 'Hiragino Sans'

plt.title('ヒストグラム')

plt.xlabel('値')
plt.ylabel('頻度')

#plt.hist(data)
plt.hist(data,bins = max(data))
plt.show()

#%%散布図
import random
import matplotlib.pyplot as plt

x = []
y = []

for i in range(100):
    x.append(random.randint(1, 50))
    y.append(random.randint(1, 50))

plt.scatter(x,y)
plt.show()

#%%数学関連のグラフを書く
import math
import matplotlib.pyplot as plt

x = []
sin = []
cos = []

for i in range(50):
    x.append(i * 0.05 * math.pi)
    sin.append(math.sin(x[i]))
    cos.append(math.cos(x[i]))

plt.title('sin/cos functions')
plt.xlabel('rad')
plt.ylabel('value')
#グリッドを表示
plt.grid(True)

plt.plot(x,sin,label = 'sin')
plt.plot(x,cos,label = 'cos')
#ラベルから凡例を作成
plt.legend()

plt.show()

#%%numpyモジュール
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0,2.5,0.05) * np.pi
sin = np.sin(x)
cos = np.cos(x)

plt.title('sin/cos functions')
plt.xlabel('rad')
plt.ylabel('value')
plt.grid(True)

plt.plot(x,sin,label = 'sin')
plt.plot(x,cos,label = 'cos')
plt.legend()

plt.show()
