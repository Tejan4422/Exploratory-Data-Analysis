import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
%matplotlib inline
plt.style.use('ggplot')
warnings.filterwarnings('ignore')

df = pd.read_csv('city_temperature.csv')

df.columns

df.dtypes

df['Day_STR'] = df['Day'].astype(str)
df['MONTH_STR'] = df['Month'].astype(str)
df['YEAR_STR'] = df['Year'].astype(str)

df.info()

df.isna().sum()

fig, ax = plt.subplots(figsize = (16,8))
sns.boxplot(x = 'Region', y = 'AvgTemperature', data = df, ax = ax)
plt.savefig('outliers.png', dpi = 100)

df[df['AvgTemperature']== -99.0].count()
df = df.drop(df[df['AvgTemperature']==-99.0].index)

df['Date'] = df['Day'].astype(str)+'/'+df['Month'].astype(str)+'/'+df['Year'].astype(str)
df.head()

df['Date'] = pd.to_datetime(df['Date'])

df.dtypes
df['Region'].nunique()
df['Country'].nunique()

df.groupby(['Region'])['Country'].nunique()
df.groupby(['Region'])['City'].nunique()
df.groupby(['Country'])['City'].nunique()

df.groupby(['Region'])['AvgTemperature'].mean()

pivot_df = pd.pivot_table(df[['Region', 'AvgTemperature', 'Year']],
                          values = 'AvgTemperature', index = ['Region'], 
                          columns = ['Year'], aggfunc = np.mean)

df.groupby(['Region'])['AvgTemperature'].mean().plot(kind='bar',figsize=(17,7))
plt.savefig('avg_temp.png', dpi = 100)

df.groupby(['Region', 'Country'])['AvgTemperature'].max().sort_values(ascending =  False).head(15)

df.groupby(['Region', 'Country'])['AvgTemperature'].min().sort_values(ascending =  False).head(15)


