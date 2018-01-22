
# coding: utf-8

from os import path

from pandas import read_csv, DataFrame


std = str(path.dirname(path.abspath(__file__))) + '/'

data = read_csv(std + 'Diabetes.csv', sep=',', usecols=[0,1,2,3,4,5,6,7])

data = DataFrame(data)

data.columns = ['Preg','Plas','Pres','Skin','Insu','Mass','Pedi','Age']

for col in data.columns:
    data = data[~data[col].isnull()] # If some instance is null, doesn't enter ~


print(data)

data.to_csv(std +'Dataset.csv')
