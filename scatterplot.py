import matplotlib.pyplot as plt
import numpy as np 
from sklearn.datasets import load_iris



plt.style.use('seaborn-v0_8-pastel')

#generate data points 
rng = np.random.default_rng(0)
x = rng.normal(size=4)
y = rng.normal(size=4)
colors = rng.random(4)
sizes = 1000 * rng.random(4)

plt.scatter(x, y, c=colors, 
            s=sizes, alpha=0.3)
plt.colorbar();

plt.savefig('scatterplot.pdf')

plt.close()

#scatterplot from Iris data 
iris = load_iris()
features = iris.data.T #transposes the data (switch)
plt.scatter(features[0], features[1], alpha=0.4, s=100*features[3], c=iris.target, cmap = 'viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('iris scatter.pdf')