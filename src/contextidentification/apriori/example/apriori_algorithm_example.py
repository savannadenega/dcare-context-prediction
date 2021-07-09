

import numpy as np
import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from pathlib import Path

"""Apriori Algorithm is a Machine Learning algorithm which is used to gain insight
 into the structured relationships between different items involved."""
"""https://www.geeksforgeeks.org/implementing-apriori-algorithm-in-python/"""
"""http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/"""


dirname = Path(__file__).parent.parent
filepath = os.path.join(dirname, 'example/Online Retail - Less Data.xlsx')

""" Step 1: Importing the required libraries """
# Loading the Data
data = pd.read_excel(filepath)
data.head()

# data = pd.read_csv(filepath)


""" Step 2: Loading and exploring the data """
# Exploring the columns of the data
data.columns
# Exploring the different regions of transactions
data.Country.unique()


""" Step 3: Cleaning the Data """
# Stripping extra spaces in the description
data['Description'] = data['Description'].str.strip()

# Dropping the rows without any invoice number
data.dropna(axis = 0, subset =['InvoiceNo'], inplace = True)
data['InvoiceNo'] = data['InvoiceNo'].astype('str')

# Dropping all transactions which were done on credit
data = data[~data['InvoiceNo'].str.contains('C')]


""" Step 4: Splitting the data according to the region of transaction """
# Transactions done in France
basket_France = (data[data['Country'] =="France"]
		.groupby(['InvoiceNo', 'Description'])['Quantity']
		.sum().unstack().reset_index().fillna(0)
		.set_index('InvoiceNo'))

# Transactions done in the United Kingdom
basket_UK = (data[data['Country'] =="United Kingdom"]
		.groupby(['InvoiceNo', 'Description'])['Quantity']
		.sum().unstack().reset_index().fillna(0)
		.set_index('InvoiceNo'))

# Transactions done in Portugal
basket_Por = (data[data['Country'] =="Portugal"]
		.groupby(['InvoiceNo', 'Description'])['Quantity']
		.sum().unstack().reset_index().fillna(0)
		.set_index('InvoiceNo'))

basket_Sweden = (data[data['Country'] =="Sweden"]
		.groupby(['InvoiceNo', 'Description'])['Quantity']
		.sum().unstack().reset_index().fillna(0)
		.set_index('InvoiceNo'))


""" Step 5: Hot encoding the Data """
# Defining the hot encoding function to make the data suitable
# for the concerned libraries
def hot_encode(x):
	if(x<= 0):
		return 0
	if(x>= 1):
		return 1


# Encoding the datasets
basket_encoded = basket_France.applymap(hot_encode)
basket_France = basket_encoded

basket_encoded = basket_UK.applymap(hot_encode)
basket_UK = basket_encoded

basket_encoded = basket_Por.applymap(hot_encode)
basket_Por = basket_encoded

basket_encoded = basket_Sweden.applymap(hot_encode)
basket_Sweden = basket_encoded


""" Step 6: Buliding the models and analyzing the results """

### France
# Building the model
frq_items = apriori(basket_France, min_support = 0.05, use_colnames = True)

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
print(rules.head())
