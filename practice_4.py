#%%線形回帰
from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------
#乱数のシード設定
np.random.seed(0)

#線形回帰のデータを準備
x,y = datasets.make_regression(n_samples=100, n_features=1, noise=30)

#学習データとテストデータを分割
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.3)

#回帰を行うためのインスタンスを取得
e = linear_model.LinearRegression()
e.fit(x_train, y_train)

#回帰モデルの取得
print('回帰係数は', e.coef_, 'です。')
print('切片は', e.intercept_, 'です。')

#テストデータから予測
y_pred = e.predict(x_test)
#---------------------------------------------------------------------

#学習データに対するモデルの評価
print('学習データによる決定係数は', e.score(x_train, y_train), 'です。')
#テストデータに対するモデルの評価
print('テストデータによる決定係数は', e.score(x_test, y_test), 'です。')

#学習データをプロット
plt.scatter(x_train, y_train, label='train')
#テストデータをプロット
plt.scatter(x_test, y_test, label='test')
#回帰直線をプロット
plt.plot(x_test, y_pred, color='m')
plt.legend()

plt.show()


#%%クラスタリング
#k-means法
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt

#---------------------------------------------------------------------
#クラスタリングを行うためのデータを作成
data, label = datasets.make_blobs(n_samples=500, n_features=2, centers=5)

#k-means法を行うインスタンスの取得
e = cluster.KMeans(n_clusters=5)
e.fit(data)

#各データが所属するクラスタを取得
print(e.labels_)
#クラスタの中心を取得
print(e.cluster_centers_)
#---------------------------------------------------------------------

#データを散布図に作成
plt.scatter(data[:, 0], data[:, 1], marker='o', c=e.labels_, edgecolor='k')
#クラスタの中心を散布図に作成
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker='x')

plt.show()
