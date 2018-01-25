
# coding: utf-8

from os import path

from pandas import read_csv, DataFrame


std = str(path.dirname(path.abspath(__file__))) + '/'

data = read_csv(std + 'Diabetes.csv', sep=',', usecols=list(range(8)))

data = DataFrame(data)

data.columns = ['Preg','Plas','Pres','Skin','Insu','Mass','Pedi','Age']

for col in data.columns:
    data = data[~data[col].isnull()]


print('\n{}\n'.format(data.head()))

data.to_csv(std[:-5] +'Dataset.csv')
