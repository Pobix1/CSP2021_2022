
import matplotlib.pyplot as plt
import pandas as pd
import math

co2_data = pd.read_csv("co2_data.csv", header=0)
print(co2_data)
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)

#Line Graph
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.ylabel('CO2 Average')
plt.xlabel('Decimal Year')
plt.title('Change in CO2 Average')
plt.show()
