#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Install Libraries and loading the data
import pandas as pd

# Provide the full path to the CSV file
df = pd.read_csv(r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\sales_data.csv')

# View the first few rows of the dataset
print(df.head())


# In[3]:


#Inspect the Data
# Display the first few rows of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Check data types and basic statistics
print(df.info())
print(df.describe())


# In[4]:


#Data Cleaning
# Handle missing values (if any)
df.fillna(0, inplace=True)  # Or you can use df.dropna()

# Convert date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Create a new column for Total Sales if it doesn't exist
df['Total Sales'] = df['Quantity Sold'] * df['Unit Price']


# In[5]:


#Basic Analysis
# 1. Total Sales
total_sales = df['Total Sales'].sum()
print(f"Total Sales: {total_sales}")


# In[6]:


# 2. Sales by Region
sales_by_region = df.groupby('Region')['Total Sales'].sum().reset_index()
print(sales_by_region)


# In[7]:


#3 Sales by Product
sales_by_product = df.groupby('Product')['Total Sales'].sum().reset_index()
sales_by_product = sales_by_product.sort_values(by='Total Sales', ascending=False)
print(sales_by_product)


# In[8]:


#  4.Sales by Category
sales_by_category = df.groupby('Category')['Total Sales'].sum().reset_index()
print(sales_by_category)


# In[9]:


# 5. Sales by Month
df['Month'] = df['Date'].dt.month
sales_by_month = df.groupby('Month')['Total Sales'].sum().reset_index()
print(sales_by_month)


# In[10]:


#Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(data=sales_by_region, x='Region', y='Total Sales')
plt.title('Total Sales by Region')
plt.xticks(rotation=45)
plt.show()


# In[11]:


#Sales by Product (Bar Plot)
plt.figure(figsize=(10, 6))
sns.barplot(data=sales_by_product.head(10), x='Product', y='Total Sales')
plt.title('Top 10 Products by Total Sales')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




