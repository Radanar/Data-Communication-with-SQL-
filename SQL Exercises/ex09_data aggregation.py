import pandas as pd
import numpy as np

data = pd.data_range('1/1/2022', periods =12, freq = '2H')

df1 = pd.DataFrame(data, columns = ['data'] )
df1['values'] = [23, 45, 32, 4, 55, 44, 34, 34, 76, 89, 55, 34 ]

print(df1)
print("----------- rolling(2).mean() -----------------")

# v2 = df1['values'].rolling(2).mean()
# print(v2)

v2 = df1['values'].rolling(5).mean()
print(v2)

v3 = df1['values'].rolling(window=5, min_period=1).mean()
print(v3)

v4 = df1['values'].rolling(2).min()
print(v4)

v5 = df1['values'].rolling(2).max()
print(v5)

v6 = df1['values'].rolling(3).sum()
print(v6)

print("----------------------------------------------")

df2 = pd.DataFrame(np.random.rand(10,4),
                   index = pd.date_range('1/1/2022', periods =12, freq = '2H'),
                   columns = ['A','B','C','D'])

v7 = df2['A'].rolling(4).sum()
v7 = df2.rolling(4).sum()
v7 = df2['C','D'].rolling(4).sum()
v7 = df2['C','D'].rolling(4).aggregate([np.min, np.max, np.sum])