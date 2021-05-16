# Data visualisation 
#
# (C) 2020 Noorhakim bin Mohamed Kamari, Singapore, Singapore
# Released under GNU Public License (GPL)
# email: hakimkamari@outlook.com
# -----------------------------------------------------------

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('singapore-citizens-by-ethnic-group-and-sex-end-june-annual.csv')

# I want to look only at the year 1990 
df = df[df['year'] == 1990]

# I also want to look at the 3 various ethnic groups 
index = ['Total Malays', 'Total Chinese', 'Total Indians']
df = df[df.level_1.isin(index)]

print(df)

# Plotting the bar chart 
New_Colors = ['green','blue','purple']
plt.bar(df['level_1'], df['value'], color = New_Colors)
plt.title('1990 Ethnic Representation')
plt.xlabel('Ethnic Groups in Singapore')
plt.ylabel('Population/ Ethnic Group (in millions)')
plt.show()

