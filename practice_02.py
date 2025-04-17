import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders_500.csv")

df["TotalAmount"] = df["Quantity"] * df["Price"]
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# # task 3
# total_price = df["TotalAmount"].sum()
# avg_amount = df["TotalAmount"].mean()
# order_by_client = df["Customer"].value_counts()

# print(f"Сумарний дохід магазину: {total_price}$")
# print(f"Середнє значення 'Total Amount': {avg_amount}")
# print(f"Кількість замовлень по кожному клієнту:\n{order_by_client}")

# task 4
# orders_with_price_greater_than_500 = df[df["Price"] > 500]

# print(orders_with_price_greater_than_500)

# task 5
# rev_df = df.sort_values(by="OrderDate", ascending=False)

# print(f"Таблиця вісортована за 'OrderDate' у зворотному порядку:\n{rev_df}")

# task 6
# start_date = pd.to_datetime("06-05-2023")
# end_date = pd.to_datetime("06-10-2023")

# orders_in_june_range = df[
#     (df["OrderDate"].dt.month == 6) &
#     (df["OrderDate"].dt.day >= start_date.day) &
#     (df["OrderDate"].dt.day <= end_date.day)
# ]

# print(orders_in_june_range)

# task 7
# category_group = df.groupby("Category")

# number_of_products_by_category = category_group["Product"].value_counts()

# print(f"Кількість товарів за категорією:\n{number_of_products_by_category}")

# total_amount_by_category = category_group["TotalAmount"].sum()

# print(f"Загальна сума продажів по кожній категорії:\n{total_amount_by_category}")

# task 8
# top_three_clients_by_total_amount = df.groupby("Customer")["TotalAmount"].sum().sort_values(ascending=False).head(3)

# print("Топ 3 клієнти за загальною сумою покупок (TotalAmount)")
# print(top_three_clients_by_total_amount)