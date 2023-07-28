import matplotlib.pyplot as plt
import pandas as pd

hourCsv = pd.read_csv('./hour.csv')

# scatter plot
fix, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=hourCsv['instant'], y=hourCsv['count'])
plt.show()
