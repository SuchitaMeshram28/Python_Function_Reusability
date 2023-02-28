import pandas as pd

df = pd.read_csv('test_file.csv')
# print(df.columns)

df["order.order_delivered_customer_date"] = pd.to_datetime(df["order.order_delivered_customer_date"])
df["order.order_estimated_delivery_date"] = pd.to_datetime(df["order.order_estimated_delivery_date"])

df['delay'] = df["order.order_delivered_customer_date"] - df["order.order_estimated_delivery_date"]
df['delay'] = df['delay'].dt.days

df['delay_status'] = df['delay'].apply(lambda x: "Late" if(x>0) else "Early")
# print(df)

df_1 = df[df['delay_status'] == 'Late']
# print(len(df_1))
# print(df_1)

df_2 = df_1.groupby('order.vendor.VendorID')['delay_status'].count()
print(df_2)