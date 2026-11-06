# First, import matplotlib package
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Check current version
print(f"Current version: {matplotlib.__version__}")

# A simple figure

months =['Jan', 'Feb', 'Mar', 'Apr']
sales =[123, 56, 487, 986]
#
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month") 
plt.ylabel("Units (k)")

plt.grid(alpha=0.4)

plt.savefig('monthly_sales.png')
plt.show()

gold_df = pd.read_csv('Download/monthly.csv')

gold_df.head()
gold_df.tail(10)

gold_df_2020 = gold_df[gold_df['Date'].str.startswith('2020')]


x = np.arange(-10,10,0.01)
y = x ** 2 + 5
sin_x = np.sin(x)

# make plot
plt.plot(x, y, c="red")
plt.plot(x, sin_x)
plt.title("Basic line plot")
plt.xlabel("x") 
plt.ylabel("y")

plt.grid(alpha=0.4)