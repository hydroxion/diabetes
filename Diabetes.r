
data <- read.csv(file='Dataset.csv', sep=",", header=TRUE)

# data = data[-(0:1)]

model <- kmeans(data, 3)

print(model)