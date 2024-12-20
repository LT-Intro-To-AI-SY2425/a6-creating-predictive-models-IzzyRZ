import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#imports the data
data = pd.read_csv("part5-unsupervised-learning/customer_data.csv")
x = data[["Annual Income", "Spending Score"]]
#standardize the data
x_std = StandardScaler().fit_transform(data)
#the value of k has been defined for you
k = 5
#apply the kmeans algorithm
kMeans = KMeans(n_clusters=k).fit(x_std)
#get the centroid and label values
centroids = kMeans.cluster_centers_
labels = kMeans.labels_
#sets the size of the graph
plt.figure(figsize=(5,5))
#use a for loop to plot the data points in each cluster
for i in range(k):
    cluster = x_std[labels == i]
    plt.scatter(cluster[:,0], cluster[:,1], cluster[:,2], cluster[:,3], cluster[:,4])
#plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], centroids[:,2], centroids[:,3], centroids[:,4], marker='X', s=100, c='r', label='centroid')           
#shows the graph
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()