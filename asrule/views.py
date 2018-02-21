from django.shortcuts import render

# Create your views here.
'''
import pandas as pd
import glob
import os
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# set wd
os.chdir("S:/B&M/Analytics & Store Segmentation/Ad Hoc Analyses/Association Rule - 2017 Halloween/")
# get all the .csv from wd
allfiles = glob.glob("*.csv")
# prepare empty data frame
raw_data = pd.DataFrame()
# read and merge all csv in a for loop
raw_data = pd.concat((pd.read_csv(f, header=None) for f in allfiles))

# changing column names
raw_data.columns = ['TransID', 'Quantity', 'ItemClass']


raw_data = raw_data[~raw_data['ItemClass'].str.startswith("4-")]

# one hot encoding
df_list = []
j=0
for i in range(0, raw_data.shape[0]-5000000, 100000):
    df = (raw_data.iloc[0+i:i+100000, :]
          .groupby(['TransID', 'ItemClass'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('TransID'))
    df_list.append(df)



def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


basket_set = basket.applymap(encode_units)

# generate frequent item sets
frequent_itemset = apriori(basket_set, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemset, metric="lift")

print(rules)

'''