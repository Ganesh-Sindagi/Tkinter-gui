from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import streamlit as st
import random

st.write("""
# k-means Clustering
by [@arielcedola](https://twitter.com/arielcedola)
This simple [streamlit](https://www.streamlit.io/) app has been developed with the aim of supporting the teaching of [clustering](https://en.wikipedia.org/wiki/K-means_clustering), a basic machine learning concept, using [k-means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) algorithm.
Easy to use! Reset points, spread them, select the number of clusters, and play!
""")

# Cached function that returns a mutable object with a random number in the range 0-100
@st.cache(allow_output_mutation=True)
def seed():
    return {'seed': random.randint(0, 100)} # Mutable (dict)

# Random state for points generation randomly selected by calling the cached function seed()
# In this way the points distribution generated by make_blobs is conserved when app is rerun
random_state = seed()

# Button to reset points by mutating the cached dict value
if st.sidebar.button('Reset points', key='123'):
    random_state['seed'] = random.randint(0, 100) # Mutated cached value

# Showing the current random_state
st.sidebar.write('Seed = ', random_state['seed'])

# Slider to select the standard deviation of clusters generated by make_blobs generator
cluster_std = st.sidebar.slider('Dispersion', 0.2, 3.0, 0.2, 0.2)

# Points generator
x, _ = make_blobs(n_samples=200, n_features=2, centers=5, cluster_std=cluster_std, shuffle=True, random_state=random_state['seed'])

# Dropdown list to select number of clusters
n_clusters = st.sidebar.selectbox('Number of clusters', range(1, 10))

# k-means algorithm
kmeans = KMeans(n_clusters=n_clusters, init='random', n_init=10, max_iter=300, random_state=111)
y_kmeans = kmeans.fit_predict(x)

# Plotting colored clusters
fig, ax = plt.subplots(figsize=(12,8))
plt.scatter(x[:, 0], x[:, 1], s=100, c=kmeans.labels_, cmap='Set1')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=400, marker='*', color='k')
st.pyplot(fig)

st.write("""
**NOTES**:
- The number of point centers generated is set to 5 by default
- The clusters found by the k-means algorithm are identified by colors
- The stars indicate the centroids of the clusters
- Code available in this github [repo](https://github.com/arielcedola/kmeans)
""")