import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders_500.csv")

df["TotalAmount"] = df["Quantity"] * df["Price"]
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

total_price = df["Price"].sum()
avg_amount = df["TotalAmount"].mean()
order_by_client = df["Client"].value_counts()
orders_with_price_greater_than_500 = df[df["Price"] > 500]
rev_df = df.sort_values(by="OrderDate", ascending=False)

start_date = pd.to_datetime("06-05")
end_date = pd.to_datetime("06-10")

orders_in_june_range = df[
    (df["OrderDate"].dt.month == 6) &
    (df["OrderDate"].dt.day >= start_date.day) &
    (df["OrderDate"].dt.day <= end_date.day)
]

