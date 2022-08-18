import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import openpyxl
import pandas as pd

fig = plt.figure()
ax1 = fig.subplots()								# 左側のy軸の定義
ax2 = ax1.twinx()								# 右側のy軸の定義

df = pd.read_excel("sample.xlsx",engine='openpyxl',skiprows=1) 			# エクセルファイルを開いて最初の１行を飛ばして(skiprows=1)読み込み
df['day']=pd.to_timedelta(df['日にち'],unit='D')+pd.to_datetime("1899/12/30") 	# 日にちをシリアル値から日付に変更してdayという名前の行にする
a = df['day'].values								# aにdayという行の値を入れる
b = df['出現'].values								# bに出現という行の値を入れる
c = df['確率'].values								# cに確率という行の値を入れる
ax1.plot(a,b,color='r',label='1-0')						# 横軸a（day）、縦軸bで左の縦軸にプロット、その際線の色は赤(r)、凡例は1-0とする
ax2.plot(a,c,color='g',label='%')						# 横軸a（day）、縦軸cで右の縦軸にプロット、その際線の色は緑(g)、凡例は%とする
ax1.set_ylim([0,1])								# 左の縦軸（ax1）の範囲を0から1にする
ax2.set_ylim([0,100])								# 右の縦軸（ax2）の範囲を0から100にする
ax1.set_ylabel(df['出現'].name)							# 左の縦軸（ax1）のラベルを"出現"にする
ax2.set_ylabel(df['確率'].name)							# 左の縦軸（ax1）のラベルを"出現"にする
plt.grid(True)									# グラフにグリッドを入れる
fig.autofmt_xdate(rotation=45)							# x軸のラベルを45度回転させる（はみ出るので）
plt.savefig("fig1.png")								# fig1.pngというファイルで保存する
plt.show()									# 図として表示する
