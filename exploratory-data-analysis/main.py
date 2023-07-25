import pandas as pd
hourCsv = pd.read_csv('./hour.csv')

print(hourCsv.head())

# Summary statistics - manual way
countMean = hourCsv['count'].mean()
countMedian = hourCsv['count'].median()
countStandardDeviation = hourCsv['count'].std()
registeredMinimum = hourCsv['registered'].min()
registeredMaximum = hourCsv['registered'].max()

print(f'Count mean: {countMean}')
print(f'Count median: {countMedian}')
print(f'Count standard deviation: {countStandardDeviation}')
print(f'Registered Minimum: {registeredMinimum}')
print(f'Registered Maximum: {registeredMaximum}')

# Summary statistics - automatic way
hourDescribe = hourCsv.describe()

print(hourDescribe)