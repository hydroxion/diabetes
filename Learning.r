
library(cluster)

library(clValid)

library(dbscan)

library(fpc)


data <- read.csv(file='Dataset.csv', sep=",", header=TRUE)


km <- kmeans(data, center=6)

dnk <- dunn(dist(data), km$cluster)

cat("\nDunn, K-means \033[31m:\033[37m ", dnk, "\n\n")

plotcluster(data, km$cluster)


db <- dbscan(data, 60, minPts=6)

dnb <- dunn(dist(data), db$cluster)

cat("\nDunn, Db-scan \033[31m:\033[37m ", dnb, "\n\n")

plot(data, col=db$cluster)

# plot(hclust(dist(recorte), method = "complete"))
