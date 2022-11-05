import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("D:/PYTHON/weather/files/weather_jan.csv", index_col=0, parse_dates=True)

df.plot(title="JAN 21\" Weather Plot", xlabel="Day", ylabel="Temperature (C)")

weather_decomposition = seasonal_decompose(df["Temperature"])

weather_decomposition.plot()

# plt.figure()
weather_decomposition.seasonal.plot(title="Seasonal")

# plt.show()
