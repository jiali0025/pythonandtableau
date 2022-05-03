#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:45:05 2022

@author: jiali
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read.csv
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# summary of the data
data.info()

# working with calculations

# defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# mathematical operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

# CostPerTransaction = CostPerItem * NumberofItemsPurchases

# variables = dataframe['column_name']
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

# adding a new column to a dataframe
data['CostPerTransaction'] = CostPerTransaction

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# profit calculation = sales - cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# markup = (sales - cost) / cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']


# rounding marking 
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# combing data fields

my_name = 'Jia' + ' Li'
my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

# my_date = data['Day'] + '-' 

# checking columns data type
print(data['Day'].dtype)

# change columns type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

# using iloc to view specific columns/rows

data.iloc[0] # views the row with .index=0 (first row)
data.iloc[0:3] # first 3 rows
data.iloc[-5:] # last 5 rows

data.head(5) # first 5 rows

data.iloc[:,2] # first 3 columns

data.iloc[4,2] # 4th row, 2nd column

# using split to split the client keyword field
# new_var = column.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand=True)

# creating new columns for the split columns in Client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

# using the lower function to change to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# how to merge files
# bring in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merge files: merge_df = pd.merge(df_old, df_new, on = 'key)
data = pd.merge(data, seasons, on = 'Month')

# drop columns
# df = df.drop('columnname", axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1) # drop multiple columns

# export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)
