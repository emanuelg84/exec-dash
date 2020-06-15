import pandas
import matplotlib.pyplot as plt
import os

year = input("insert year you would like to analyse: ")
month = input("insert month you would like to analyse: ")

if month == "1":
    month_str="January"
elif month =="2":
    month_str="February"
elif month =="3":
    month_str="March"
elif month =="4":
    month_str="April"
elif month =="5":
    month_str="May"
elif month =="6":
    month_str="June"
elif month =="7":
    month_str="July"
elif month =="8":
    month_str="August"
elif month =="9":
    month_str="September"
elif month =="10":
    month_str="October"
elif month =="11":
    month_str="November"
else:
    month_str="December"


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#NEED TO INCLUDE HERE VALIDATION REQUIERMENT

df = pandas.read_csv(f'data/sales-{year}{month}.csv')

#print(df.head(5))

total_sales = df['sales price'].sum()


df_agg = df.groupby('product')  \
           .agg({'unit price': 'mean', 
                 'units sold': 'sum',
                 'sales price': 'sum'})

df_agg.sort_values('units sold', ascending=False, inplace=True)


print("-----------------------")

print("Total Sales in " + month_str + " " + str(year) + ": " + str(to_usd(total_sales)))
print("-----------------------")
print("Top Selling Products:")


top_sellers = []
rank = 1
for i, row in df_agg.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + str(to_usd(d["monthly_sales"])))



print("-----------------------") #print("VISUALIZING THE DATA...")   

chart_title = "Top Selling Products " + month_str + " " + str(year)

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

plt.bar(sorted_products, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")
plt.show()