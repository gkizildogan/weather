import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from pmdarima import auto_arima

df = pd.read_csv("D:/PYTHON/weather/files/weather_jan.csv", index_col=0, parse_dates=True)

# df.plot(title="JAN 21\" Weather Plot", xlabel="Day", ylabel="Temperature (C)")

train_data = df[:len(df)-24]
test_data = df[len(df)-24:]

auto_arima(train_data, m=24).summary()

# Model:             SARIMAX(2, 1, 0)x(2, 0, 0, 24)

model = SARIMAX(train_data, order=(2, 1, 0), seasonal_order=(2, 0, 0, 24))
result = model.fit()

predictions = result.predict(start=len(train_data), end=len(df)-1)

rmse_error = mean_squared_error(test_data, predictions, squared=False)
mse_error = mean_squared_error(test_data, predictions)
mean_value = test_data.mean()

print(f'MSE: {mse_error} \n RMSE: {rmse_error} \n Mean:{mean_value}')

test_data.plot(legend=True)
predictions.plot(legend=True)
plt.tight_layout()

