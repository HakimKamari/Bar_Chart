# Data visualisation 
#
# (C) 2021 Noorhakim bin Mohamed Kamari, Singapore, Singapore
# Released under GNU Public License (GPL)
# email: hakimkamari@outlook.com
# -----------------------------------------------------------

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('singapore-citizens-by-ethnic-group-and-sex-end-june-annual.csv')

# I want to look at the 3 various ethnic groups 
index = ['Total Malays', 'Total Chinese', 'Total Indians']
df = df[df.level_1.isin(index)]

# 1970 and 1990 are the years that we will be focusing for this bar chart
df_1970 = df[df['year'] == 1970]
df_1990 = df[df['year'] == 1990]

print(df_1970)
print(df_1990)

# setting the bar chart labels
X = ['Total Malays','Total Chinese','Total Indians']
  
# basically allocates the number of bar chart slots based on no of elements in X
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, df_1970['value'] , 0.4, label = '1970', color = 'green')
plt.bar(X_axis + 0.2, df_1990['value'], 0.4, label = '1990', color = 'blue')
  
plt.xticks(X_axis, X)
plt.xlabel('(Ethnic Groups)')
plt.ylabel('Population/ Ethnic Group (in millions)')
plt.title('1970 vs 1990 Ethnic Group Representation')
plt.legend()
plt.show()

