
# coding: utf-8

# python3 Learning.py

from os import path

from sklearn import cluster

from pandas import read_csv


std = str(path.dirname(path.abspath(__file__))) + '/'

data = read_csv(std + 'Dataset.csv')

kmmeans = cluster.KMeans(n_clusters=6).fit(data)

centroids = kmmeans.cluster_centers_

labels = kmmeans.labels_


print('\n{2}Centroids{3}\n\n{0}\n\n{2}Labels{3}\n\n{1}\n'.format(centroids, labels, '\033[31m', '\033[37m'))
