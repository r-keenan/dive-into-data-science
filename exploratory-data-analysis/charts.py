import matplotlib.pyplot as plt
import pandas as pd

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
