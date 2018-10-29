#-*-coding:utf-8-*-
import pandas as pd

data=pd.read_csv('pandas.csv')      #读取外部文件
print(data)

data.to_pickle('pandas.pickle')     