import pandas as pd

carsale_df = pd.read_csv("Downloads/car-sales-extended-missing-data.csv")

print(carsale_df.head())

# Loại bỏ các dòng thiếu ngay trên df hiện tại
carsale_df.dropna(inplace=True)

carsale_df.isna().sum()