import pandas as pd

df = pd.read_csv('test_file.csv')
print(df.columns)

df["order.order_purchase_date"] = pd.to_datetime(df["order.order_purchase_date"])
df["month_name"] = df["order.order_purchase_date"].apply(lambda x: x.strftime('%B'))

sales = df.groupby('month_name')['sales_amt'].sum()
highest_sales = sales.idxmax()
print("THE MONTH WITH THE HIGHEST SALES IS:", highest_sales) #May


profit = df.groupby('month_name')['profit_amt'].sum()
# print(profit)
highest_profit = profit.idxmax()
print("THE MONTH WITH THE HIGHEST PROFIT IS:", highest_profit) #March

df_1 = pd.DataFrame({'profit': profit})
print(type(df_1))


df_2 = df_1.assign(profit_per = lambda x : (x['profit']/df_1["profit"].sum()*100))
print(df_2)

df_3 = df_2[df_2["profit_per"] > 20]
print(df_3) #3