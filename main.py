# Import libraries
import pandas as pd  # For data manipulation
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For plotting graphs

# Step 1: Load the CSV data
data = pd.read_csv("data/sales_data.csv")
print("Data Loaded Successfully")
print(data.head())  # Display first 5 rows

# Step 2: Compute Total Sales per row
data['Total_Sale'] = data['Quantity'] * data['Price']
print("\nData with Total Sales:\n", data)

# Step 3: Compute Overall Statistics
total_revenue = data['Total_Sale'].sum()  # Total revenue
average_sale = data['Total_Sale'].mean()  # Average sale per item
print(f"\nTotal Revenue: {total_revenue}")
print(f"Average Sale per Transaction: {average_sale}")

# Step 4: Sales per Category
category_sales = data.groupby('Category')['Total_Sale'].sum()
print("\nSales per Category:\n", category_sales)

# Step 5: Visualize the data

# Line Plot - Total Sales over Dates
daily_sales = data.groupby('Date')['Total_Sale'].sum()
plt.figure(figsize=(8,5))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='b')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# Bar Plot - Sales per Category
plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values, color='orange')
plt.title("Sales per Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Pie Chart - Category Contribution
plt.figure(figsize=(6,6))
plt.pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
plt.title("Sales Contribution by Category")
plt.show()
