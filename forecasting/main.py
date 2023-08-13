import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


def get_mae(line, actual):
    error = [(x-y) for x, y in zip(line, actual)]
    errorabs = [abs(value) for value in error]
    mae = np.mean(errorabs)
    return (mae)


def get_rmse(line, actual):
    error = [(x-y) for x, y in zip(line, actual)]
    errorsquared = [(value)**2 for value in error]
    rmse = np.sqrt(np.mean(errorsquared))
    return (rmse)


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

# calculating regression errors
saleslist = carsales['sales'].tolist()
regressionline = [81.2 * i + 10250.8 for i in carsales['period']]
hyptothesizedline = [125 * i + 8000 for i in carsales['period']]
error1 = [(x-y) for x, y in zip(regressionline, saleslist)]
error2 = [(x-y) for x, y in zip(hyptothesizedline, saleslist)]

# mean absolute error (MAE)
# regression line
error1abs = [abs(value) for value in error1]
# hypothesized line
error2abs = [abs(value) for value in error2]
print(np.mean(error1abs))
print(np.mean(error2abs))

# root mean squared error (RMSE)
error1squared = [(value)**2 for value in error1]
error2squared = [(value)**2 for value in error2]
print(np.sqrt(np.mean(error1squared)))
print(np.sqrt(np.mean(error2squared)))

print(get_rmse(regressionline, saleslist))
print(get_rmse(hyptothesizedline, saleslist))

# extending out the x-axis for forecasting out the future.
x_extended = np.append(carsales['period'], np.arange(108, 116))
x_extended = x_extended.reshape(-1, 1)
extended_prediction = regressor.predict(x_extended)

plt.scatter(carsales['period'], carsales['sales'])
plt.plot(x_extended, extended_prediction, 'r--')
plt.title('Car Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
