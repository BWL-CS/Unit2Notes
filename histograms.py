import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('ggplot')

rng = np.random.default_rng(1701)
data = rng.normal(size=1000)

#histogram shows frequanecy 
plt.hist(data)
plt.savefig('histogram.png')
plt.close()

# Example of a more customized hist
plt.hist(data, bins=30, density=True, alpha=0.5, histtype='stepfilled', color = 'yellow', edgecolor='none')
plt.savefig('histcustom-.png')
plt.close()

#hexgonal binnings
mean = [0, 0]
cov = [[1,1], [1,2]]
x, y = rng.multivariate_normal(mean, cov, 100000).T
plt.hexbin(x,y, gridsize = 10000)
cb = plt.colorbar(label='count in bin')

plt.savefig('hexbin.png')