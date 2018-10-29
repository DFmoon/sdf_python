#-*-coding:utf-8-*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#线性数据
data=pd.Series(np.random.randn(1000),index=np.arange(1000)) #生成一个随机序列
data=data.cumsum()      #数据的累加
data.plot()             #数据转化为图像，plot()中含有设置图像性质的各种参数
plt.show()              #显示图像

#矩阵数据
data2=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
data2=data2.cumsum()     #数据的累加
print(data2.head(5))     #显示前5行数据
data2.plot()
plt.show()

#在一张图中显示两个图像
b=data2.plot.scatter(x='A',y='B',color='pink',label='A&B')     #scatter为数据点画图
data2.plot.scatter(x='A',y='C',color='yellow',label='A&C',ax=b) #ax属性，将b的数据也放在该图中
plt.show()