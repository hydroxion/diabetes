
# coding: utf-8

from os import path

from sklearn import cluster

from pandas import read_csv


std = str(path.dirname(path.abspath(__file__))) + '/'


data = read_csv(std + 'Dataset.csv')


kmmeans = cluster.KMeans(n_clusters=3).fit(data)

centroids = kmmeans.cluster_centers_

labels = kmmeans.labels_


print('\nCentroids\n\n{}\nLabels\n\n{}\n'.format(centroids, labels))
