
# coding: utf-8

from os import path

from sklearn import cluster

from pandas import read_csv

import matplotlib.pyplot as plt


std = str(path.dirname(path.abspath(__file__))) + '/'

data = read_csv(std + 'Dataset.csv')

kmeans = cluster.KMeans(n_clusters=6).fit(data)

centers = kmeans.cluster_centers_

labels = kmeans.labels_


print('\n{2}Centroids{3}\n\n{0}\n\n{2}Labels{3}\n\n{1}\n'.format(centers, labels, '\033[31m', '\033[37m'))
