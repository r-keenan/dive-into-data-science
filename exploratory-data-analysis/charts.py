import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

hourCsv = pd.read_csv('./hour.csv')

# scatter plots
fix, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hourCsv['instant'], y=hourCsv['count'])
plt.show()

hour_first48 = hourCsv.loc[0:48, :]
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hour_first48['instant'], y=hour_first48['count'])
plt.xlabel('Hour')
plt.ylabel('Count')
plt.title('Count by Hour - First Two Days')
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hour_first48['instant'],
           y=hour_first48['count'], c='red', marker='+')
plt.xlabel('Hour')
plt.ylabel('Count')
plt.title('Count by Hour = First Two Days')
plt.show()

# line plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hour_first48['instant'], hour_first48['casual'],
        c='red', label='casual', linestyle='-')
ax.plot(hour_first48['instant'], hour_first48['registered'],
        c='blue', label='registered', linestyle='--')
ax.legend()
plt.show()

# Box plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='hr', y='registered', data=hourCsv)
plt.xlabel('Hour')
plt.ylabel('Count')
plt.title('Counts by Hour')
plt.show()

# histogram - plots out frequency
fix, ax = plt.subplots(figsize=(10, 6))
ax.hist(hourCsv['count'], bins=80)
plt.xlabel('Ridership')
plt.ylabel('Frequency')
plt.title("Ridership Histogram")
plt.show()

# pair plot
thevariables = ['hr', 'temp', 'windspeed']
hour_first100 = hourCsv.loc[0:100, thevariables]
sns.pairplot(hour_first100, corner=True)
plt.show()

# correlations || -1 == negative correlation || 1 == positive correlation || 0 == uncorrelated
print(hourCsv['casual'].corr(hourCsv['registered']))
print(hourCsv['temp'].corr(hourCsv['hum']))

# correlation matrix
thenames = ['hr', 'temp', 'windspeed']
cor_matrix = hourCsv[thenames].corr()
print(cor_matrix)

# heat map
plt.figure(figsize=(14, 10))
corr = hourCsv[thenames].corr()
sns.heatmap(corr, annot=True, cmap='binary', fmt='.3f',
            xticklabels=thenames, yticklabels=thenames)
plt.show()
