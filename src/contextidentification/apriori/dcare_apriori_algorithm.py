import numpy as np
import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from pathlib import Path

"""Apriori Algorithm is a Machine Learning algorithm which is used to gain insight
 into the structured relationships between different items involved."""


""" Step 1: Importing the dataset """
dirname = Path(__file__).parent
filepath = os.path.join(dirname, 'dataset-less-data.xls')
data = pd.read_excel(filepath)
print(data.head())


""" Step 2: Setting Data """
basket_data = (data.set_index('id_pacient'))
print(basket_data.head())


""" Step 3: Hot encoding the Data to make the data suitable for the concerned libraries """
def hot_encode(x):
    if x == 5 or x == 6:
        return 0
    else:
        return 1


basket_encoded = basket_data.applymap(hot_encode)
basket_data = basket_encoded
print(basket_data.head())


""" Step 4: Buliding the models and analyzing the results """
# Building the model
frq_items = apriori(basket_data, min_support=0.05, use_colnames=True)

# Collecting the inferred rules in a dataframe
rules = association_rules(frq_items, metric="lift", min_threshold=1)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])

print(rules.head())
