# Data visualisation 
#
# (C) 2021 Noorhakim bin Mohamed Kamari, Singapore, Singapore
# Released under GNU Public License (GPL)
# email: hakimkamari@outlook.com
# -----------------------------------------------------------

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt # this is the same as: from matplotlib import pyplot as plt
import string 
import mplcursors

df = pd.read_csv('singapore-citizens-by-ethnic-group-and-sex-end-june-annual.csv')

# I want to look at the 3 various ethnic groups 
index = ['Total Malays', 'Total Chinese', 'Total Indians']
df = df[df.level_1.isin(index)]

# 1970 and 1990 are the years that we will be focusing for this bar chart
df_1970 = df[df['year'] == 1970]
df_1990 = df[df['year'] == 1990]

print(df_1970)
print(df_1990)
  
# basically allocates the number of bar chart slots based on no of elements in X
# Return evenly spaced values within a given interval.
X_axis = np.arange(len(index))
  
# the -0.2 indicates the mid point of the first bar plot
plt.bar(X_axis - 0.2, df_1970['value'] , 0.4, label = '1970', color = 'green') # 0.4 refers to the total width of the 1st bar
plt.bar(X_axis + 0.2, df_1990['value'], 0.4, label = '1990', color = 'blue')
  
plt.xticks(X_axis, index)
plt.xlabel('(Ethnic Groups)')
plt.ylabel('Population/ Ethnic Group (in millions)')
plt.title('1970 vs 1990 Ethnic Group Representation')
plt.legend()

# With HoverMode.Transient, the annotation is removed as soon as the mouse leaves the artist
cursor = mplcursors.cursor(hover=mplcursors.HoverMode.Transient)
@cursor.connect("add")
def on_add(sel):
    x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
    sel.annotation.set(text=f"{'Population'}: {height}",
                       position=(0, 20), anncoords="offset points")
    sel.annotation.xy = (x + width/2, y + height) # this will dictate where the cursor will point at

plt.show()


