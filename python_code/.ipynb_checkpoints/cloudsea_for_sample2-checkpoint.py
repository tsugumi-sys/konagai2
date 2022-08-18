import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import openpyxl
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = ax1.twinx()
ax3 = fig.add_subplot(1,2,2)
ax4 = ax3.twinx()
plt.subplots_adjust(wspace=0.6, hspace=0.5)

df1 = pd.read_excel("sample2.xlsx",engine='openpyxl',sheet_name="Sheet1",skiprows=1)
df1['day']=pd.to_timedelta(df1['日にち'],unit='D')+pd.to_datetime("1899/12/30") 
a1 = df1['day'].values
b1 = df1['出現'].values
c1 = df1['確率'].values

df2 = pd.read_excel("sample2.xlsx",engine='openpyxl',sheet_name="Sheet2",skiprows=2)
df2['day']=pd.to_timedelta(df2['日にち'],unit='D')+pd.to_datetime("1899/12/30") 
a2 = df2['day'].values
b2 = df2['出現'].values
c2 = df2['確率'].values

ax1.plot(a1,b1,color='r',label='1-0')
ax2.plot(a1,c1,color='g',label='%')
ax1.set_ylim([0,1])
ax2.set_ylim([0,100])
ax1.set_ylabel(df1['出現'].name)
ax2.set_ylabel(df1['確率'].name)
ax1.grid(True)

ax3.plot(a2,b2,color='k',linestyle="-",label='1-0')
ax4.plot(a2,c2,color='k',linestyle="--",label='%')
ax3.set_ylim([0,1])
ax4.set_ylim([0,100])
ax3.set_ylabel(df2['出現'].name)
ax4.set_ylabel(df2['確率'].name)
ax3.grid(True)
fig.autofmt_xdate(rotation=45)
plt.savefig("fig2.png")
plt.show()
