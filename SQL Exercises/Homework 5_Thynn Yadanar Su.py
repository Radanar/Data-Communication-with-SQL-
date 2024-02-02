"""
Homework #5
1) Download the following file from eLearning.: “sales.csv” which contains 19 months of ecommerce sales data (was exported from Google Analytics) and load it into a Pandas dataframe.
2) Calculate rolling means or rolling averages for the conversion_rate column. Calculate a three-month, six-month, nine-month, and 12-month rolling average, and assign the values back to the original dataframe.
3) Print the final dataframe. The final output should look like:
"""

import pandas as pd

# reading the data from the csv file
sales = pd.read_csv(r"F:\Parami\Courses\2023, Fall Semester Materials\Parami Courses\Data Communication and Ethics\Projects & Assignments\sales.csv")

df = pd.DataFrame(sales)
#print(df)

df['mean_conversion_rate_3m'] = df['conversion_rate'].rolling(3).mean()
df['mean_conversion_rate_6m'] = df['conversion_rate'].rolling(6).mean()
df['mean_conversion_rate_9m'] = df['conversion_rate'].rolling(9).mean()
df['mean_conversion_rate_12m'] = df['conversion_rate'].rolling(12).mean()

final_output = ['year_month', 'sessions', 'transactions', 'conversion_rate', 'revenue', 'aov', 'mean_conversion_rate_3m', 'mean_conversion_rate_6m', 'mean_conversion_rate_12m']
df_final = df[final_output]

print(df_final.columns.tolist())
print(df_final)




