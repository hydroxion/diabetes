
# Rscript Learning.r

library(cluster)

library(fpc) # install.packages('fpc')


dat <- read.csv(file='Dataset.csv', sep=",", header=TRUE)

km <- kmeans(dat, center=6)

cat("\n\033[31mClusters\033[37m\n\n", km$cluster, "\n\n\033[31mCenters\033[37m\n\n", km$centers, "\n\n")

plotcluster(dat, km$cluster)
