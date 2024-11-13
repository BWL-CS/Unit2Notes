import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 

sns.set_theme(style='ticks', palette='pastel') #othehr pallets are deep, muted, bright, dark, colorblind
#style are dark, white, darkgrid, whitegrid, ticks


#matplotlib histogram 
#histogram shoes distribution of values
data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=1000)
data = pd.DataFrame(data, columns=['x','y'])
for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.56)
plt.savefig('hist.pdf', bbox_inches='tight')
plt.close()

#KDE (Kernal desnity estimaation) gives a smooth estimeite of distrobution of values
sns.kdeplot(data=data, fill=True)
plt.savefig('sns-kdeplot.pdf', bbox_inches='tight')
plt.close()

#load a built in dataset 
iris = sns.load_dataset("iris")
print(iris.head())
sns.pairplot(iris, hue='species', height=2.5)
plt.savefig('sns-pairplot.png', bbox_inches='tight')
plt.close()
