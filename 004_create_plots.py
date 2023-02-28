import pandas as pd

import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

print(f"Air Quality:\n{air_quality.head()}")

air_quality.plot()

plt.show()

air_quality["station_paris"].plot()

plt.show()

air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

plt.show()
