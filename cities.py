import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np

#load our CSV into a dataframe 
cities = pd.read_csv('california_cities.csv')
print(cities.info())

lat = cities['latd'] #y values cos 
lon = cities['longd'] #x values syn
pop = cities['population_total']
area = cities['area_total_sq_mi']

#scatterplot 
plt.scatter(lon, lat, label=None, c=np.log10(pop), cmap='RdPu', s=area, linewidth=0, alpha=0.5)
plt.axis('equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)
plt.title('CA Cities: Area and population')
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area,
                label=str(area) + ' km$^2$')
coeffs = np.polyfit(lon, lat, 2)
x_fit = np.linspace(min(lon), max(lon), 5)
y_fit = np.polyval(coeffs, x_fit)
plt.plot(x_fit, y_fit, label='2nd degree fit')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')
plt.savefig('cities.png')
plt.close()