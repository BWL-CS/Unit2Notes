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
ax.plot(x_vals, 3*(x_vals), color='#47c92a')
ax.plot(x_vals, 4*(x_vals), linestyle='dashed')
ax.plot(x_vals, 5*(x_vals), linestyle='dashdot')
ax.plot(x_vals, 6*(x_vals), linestyle='dotted')
ax.plot(x_vals, 7*(x_vals), linestyle='dotted')

ax.plot(x_vals, 1.5*(x_vals)*(x_vals), ':m')
fig.savefig('lineplot2.png')

#demo on cusotmaztion 
fig3 = plt.figure()


plt.plot(x_vals, np.sin(x_vals))
plt.xlim(-1, 11)
plt.ylim(-3.14, np.pi)
plt.axis('tight')
#other options; 'equal',image 
plt.title("a sign wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
fig3.savefig('lineplot3.pdf')