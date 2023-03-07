import matplotlib.pyplot as plt
import numpy as np
plt.axhline(0,color='black') # x = 0
plt.axvline(0,color='black') # y = 0


plt.vlines(x = 2, ymin = 0, ymax = 3, colors = 'black', linestyle = 'dotted')
plt.hlines(y = 3, xmin = 0, xmax = 2, colors = 'black', linestyle = 'dotted')


plt.text(-0.2, 3, '$y$', fontsize = 12)
plt.text(1.5, 5, '$a > 0$', fontsize = 14)
plt.text(-1.5, -2, '$x < (y - b)/a$', fontsize = 12)
plt.text(-1, 1.7, '$Y < y$ ', fontsize = 12)
plt.text(-0.15, -0.8, '0 ', fontsize = 12)
plt.text(1.5, -1, 'x = (y - b)/a', fontsize = 12)

plt.arrow(-1, -1, -0.1, 0.8, width = 0.03)
plt.arrow(-0.5, 1.8, 0.3, 0.01, width = 0.04)
plt.grid()
xpoints = [-2, -1, 0, 1, 2, 3]
ypoints = np.array([-9, -6, -3, 0, 3, 6])
plt.plot(xpoints, ypoints, linestyle = 'solid', label = 'y = ax + b')
plt.legend()


plt.title('Plot of y = ax + b ,  a > 0', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})

plt.show()
