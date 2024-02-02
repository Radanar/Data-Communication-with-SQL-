import numpy as np
import pandas as pd

# a = np.array([[1,2],[3,4]])
# print(a)

# print("------------")

# b = np.array([1,2,3,4], ndmin=3)
# print(b)

# print("------------")

# df1 = pd.DataFrame(a, index=['r1', 'r2'], columns= ['C1','C2'])
# print(df1)

# print("------------")

# data1 = {'Name': ["Radanar", "Charles", "Ming Thet", "Aung Kyaw Win"], 'Age': [22,20,21,19]}
# df2 = pd.DataFrame(data1)
# print(df2)

# print("------------")
#Adding the index and columns in the dataFrame function all at once
df3 = pd.DataFrame(np.random.randn(5,3), index=['a','b','c','d','e'], columns=['One','Two','Three'])
print(df3)

print("------------")

df4 = df3.reindex(['a','g','d','l','c'])
print(df4)

print("------------")
#Setting the index and columns can be done separately from dataFrame function
df4.index = ['I','II','III','IV','V']
df4.columns = ['i','ii','iii']
print(df4)

print("------------")
print(df4.isnull())

print("------------")
#we can add the numbers we like for the NaN null values in the data frame

# print(df4.fillna(0)) #just printing the values but it doesn't write values in the data frame

# df4 = df4.fillna(0) #overwriting the df4 and changing the value in the data frame
# print(df4)

# print("")
# print("Why does the value 0 not changed into -1??? Can't we fill new values with fillna() to the ones already filled?")

# df5 = df4.fillna(-1)
# print(df5)

# print("------------")
# print("Forward Fill")
# df6 = df4.fillna(method='pad') #Foreward fill the null values
# print(df6)

# print("------------")
# print("Forward Fill")
# df7 = df4.fillna(method='ffill') #Foreward Fill the null values - taking the values before it
# print(df7)

# print("------------")
# print("Backward Fill")
# df8 = df4.fillna(method='bfill') #Backward Fill the null values - taking the values after it
# print(df8)

# df9 = df4.dropna() 
# print(df9)


df10 = pd.DataFrame({'one':[4000, 5000, 20, 30], 'two':[10, 20, 700, 100]}) #Addind the values as dictionary type in the data frame
print(df10)

print("------------")
df11 = df10.replace({4000:1, 700:7}) #replacing the values with replace funtion of the data frame
print(df11)


