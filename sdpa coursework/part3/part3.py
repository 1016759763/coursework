import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

filename = 'TSLA.csv'
df = pd.read_csv(filename)

#detail = df.info() # the details about this csv file the maximum, minmum, size, quantile and types
#print(detail)

#overview = df.describe()
#print(overview)

#print(df['High'])

#show the daily change rate into a new column. The rate = (high-low)/low *100

df.loc[:,'rate'] = (df['Close']-df['Open'])/df['Open'] * 100
print(df)

# show daily status rise or down
def get_dailychange(x):
    if x['rate']>1:
        return 'rocket rise'
    elif 0 <= x['rate'] <= 1:
        return 'rise'
    elif -1 <= x['rate'] <0:
        return 'down'
    else:
        return 'sharply fall'
df.loc[:,"status"] = df.apply(get_dailychange, axis=1)

x = df['Date']
y = df['Open']
plt.plot(x,y)
plt.show()