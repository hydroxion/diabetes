
# Rscript Learning.r

library(cluster)

library(fpc) # install.packages('fpc')

library(dbscan)


dat <- read.csv(file='Dataset.csv', sep=",", header=TRUE)

km <- kmeans(dat, center=6)

db <- dbscan(dat, 5, minPts=5)


cat("\n[ Km ] \033[31mClusters\033[37m\n\n", km$cluster, "\n\n\033[31mCenters\033[37m\n\n", km$centers, "\n\n")

cat("\n[ Db ] \033[31mEmpty\033[37m\n\n\n")


plotcluster(dat, km$cluster, xlab=NULL, ylab=NULL)

# plotcluster(dat, db$cluster, xlab=NULL, ylab=NULL)
