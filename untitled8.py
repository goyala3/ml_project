# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16nS_Xv_4WD-gGSOltU2Sxjkq5D2WK_K6
"""

import pandas as pd
import matplotlib.pyplot as plt
import glob

l = [pd.read_csv(filename) for filename in glob.glob("/content/*.csv")]
print(len(l))

#  create the dataset using all files under the data directory
df = pd.concat(l, axis=0)
df.head()

import datetime

df.dtypes

df['sale_time']=df['sale_time'].astype('datetime64[ns]')

df['sale_date'] = df['sale_time'].dt.date

df['sale_time1']= df['sale_time'].dt.time

df

df=df[['sale_date','purchaser_gender','sale_time1']]

df

result=df.groupby(['sale_date']).agg({'sale_time1': "size"}).reset_index()

result

x=result['sale_date']
y= result['sale_time1']
plt.plot(x,y)

"""##It looks like there has been a sudden change in daily sales. What date did it occur?##"""

result.dtypes

# create a lag column
result['lag'] = result['sale_time1'].shift(1)

result

result['difference']= result['sale_time1']-result['lag']

result

result['difference'].max()

result

results = result[result['difference'] == 274]

results

"""##Is the change in daily sales at the date you selected statistically significant? If so, what is the p-value?"""

result['lead']=result['sale_time1'].shift(-1)

result

results= result[result['difference'] == 274]

results

from scipy import stats

stats.ttest_1samp(result['sale_time1'], 732)

"""The value of p is less than 0.0s so, we can say that Null hypothesis will reject and alternative hypothesis is select. So, this date is important for us.

##Question 4
Does the data suggest that the change in daily sales is due to a shift in the proportion of male-vs-female customers? Please use plots to support your answer (a rigorous statistical analysis is not necessary).
"""

df

df['purchaser_gender'].value_counts()

