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

tips = sns.load_dataset('tips')
print(tips.head())
tips['tipsPercent'] = 100 * tips['tip'] / tips['total_bill']

#facet grid: compare muliple dimentions
grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tipsPercent", bins=np.linspace(0, 40, 15))
#smooth line of best fit/KDE 
plt.savefig('sns-facetgrid.png', bbox_inches='tight')
plt.close()

#catigorical plot (spelling is not my strong suit)
sns.catplot(x="day", y="total_bill", hue='sex', data=tips, kind='box')
#sns.set_axis_labels('day', 'total bill')
plt.savefig('sns-catplot.png', bbox_inches='tight')
plt.close()

sns.jointplot(x='total_bill', y="tip", data=tips, kind='reg')
plt.savefig('sns-jointplot.png', bbox_inches='tight')
plt.close()