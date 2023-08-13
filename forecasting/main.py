import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

carsales = pd.read_csv('carsales.csv')

# rename the column headers
carsales.columns = ['month', 'sales']

# copy all rows but last one to new df. doing this because the last row is information and not data.
carsales = carsales.loc[0:107, :].copy()

carsales['period'] = list(range(108))

# set up scatter plot
plt.scatter(carsales['period'], carsales['sales'])
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# set up regression line
# slope formula: y = m * x + b
# m = slope or coefficient
# b = intercept or y-intercept
# carsales = 81.2 * period + 10250.8
x = carsales['period'].values.reshape(-1, 1)
y = carsales['sales'].values.reshape(-1, 1)
regressor = LinearRegression()
regressor.fit(x, y)
print(regressor.coef_)
print(regressor.intercept_)

# hypothesized line & regression line from up above
# carsales = 125 * period + 8000
plt.scatter(carsales['period'], carsales['sales'])
plt.plot(carsales['period'], [
         81.2 * i + 10250.8 for i in carsales['period']], 'r-', label='Regression Line')
plt.plot(carsales['period'], [
         125 * i + 8000 for i in carsales['period']], 'r--', label='Hypothesized line')
plt.legend(loc='upper left')
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
