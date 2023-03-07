# here p = 0.7 , q = 0.3
import matplotlib.pyplot as plt
import numpy as np

x_1_points = np.array([0, 1])
y_1_points = np.array([0.3, 0.3])
plt.xticks([0,1,])
# plt.yticks([0,0.6,1,])

x_2_points = np.array([1, 3])
y_2_points = np.array([1, 1])

x_0_points = np.array([-3, 0])
y_0_points = np.array([0.001, 0.001])

# Add a title (specify font parameters with fontdict)
plt.title('Plot of F(x)', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# plt.text(-3.1, 0.29, '1-p', fontsize = 10)

y = [0, 0.3, 0.6, 1]
labels = ['0', '1-p', '0.6', '1']
plt.yticks(y, labels, rotation ='horizontal')


plt.plot(x_1_points, y_1_points, label='F(x) = 1  , 0 <= x < 1')
plt.plot(x_2_points, y_2_points, label='F(x) = 1-p  , x >= 1')
plt.plot(x_0_points, y_0_points, label='F(x) = 0  , x < 0')
plt.vlines(x=1, ymin=0.3, ymax=1, colors='blue', ls=':', lw=1)
plt.vlines(x=0, ymin=0, ymax=0.3, colors='blue', ls=':', lw=1)
plt.legend()

plt.savefig('mygraph.png', dpi=100)

plt.show()
