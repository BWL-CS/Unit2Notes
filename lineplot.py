import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-pastel')
#rember that x is the independent variable 
x_vals = np.linspace(0, 10, 100)
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

#plt.show()
plt.savefig('lineplots.png')

#alternativly set up a fig object for the plot 
fig = plt.figure()
ax = plt.axes()

ax.plot(x_vals, 2*(x_vals)+3)
fig.savefig('lineplot2.png')