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

# printing value row three of the Count column. 0 based index
countIndividualValue = hourCsv.loc[3, 'count']
print(f'row three value of the Count column: {countIndividualValue}')

# get a range of row values from the Registered column
registeredValuesArray = hourCsv.loc[2:4, 'registered']
print(f'registeredValues: {registeredValuesArray}')

# nighttime observations
registeredNighttimeObservations = hourCsv.loc[hourCsv['hr'] < 5, 'registered'].mean(
)
print(f'Nighttime observation: {registeredNighttimeObservations}')

# warmer morning hours
countWarmerMornings = hourCsv.loc[(hourCsv['hr'] < 5) & (
    hourCsv['temp'] < .50), 'count'].mean()
print(f'Warmer mornings: {countWarmerMornings}')

# colder morning hours
countColderMornings = hourCsv.loc[(hourCsv['hr'] < 5) & (
    hourCsv['temp'] > .50), 'count'].mean()
print(f'Colder mornings: {countColderMornings}')

# higher temps or higher humidity
countHigherTempHumidity = hourCsv.loc[(hourCsv['temp'] > 0.5) | (
    hourCsv['hum'] > .5), 'count'].mean()
print(f'Mean of higher temp or humidity: {countHigherTempHumidity}')

# seasonal data
countSeasonalGrouping = hourCsv.groupby(['season'])['count'].mean()
print(f'Seasonal data: {countSeasonalGrouping}')

# seasonal and holiday grouping
countSeasonalHolidayGrouping = hourCsv.groupby(
    ['season', 'holiday'])['count'].mean()
print(f'Seasonal and Holiday grouping: {countSeasonalHolidayGrouping}')
