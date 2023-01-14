from sklean.cluster import KMeans

model = KMeans(n_cluster3)

samples = iris.data

model.fit(samples)

print(labels)