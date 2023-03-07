# ICSE 2019 CLASS 12
# Question 1(vi)
""" Problem Statement
Prove that the function f(x) = x^3 - 6x^2 + 12x + 5 is increasing on R
"""

import matplotlib.pyplot as plt
import numpy as np

# input parameters 
x = np.linspace(-10, 12, 100)

# The function y = x^3 - 6x^2 + 12x + 5
y = x*x*x - 6*x*x + 12*x + 5

# Plotting the function 
plt.plot(x, y, color="black", linestyle="-", linewidth=2, label='$y=f(x)$')

# Preparing to plot the inflection point:
x2 = 2
y2 = x2*x2*x2 - 6*x2*x2 + 12*x2 + 5

# Displaying the inflection point
plt.plot(x2, y2, color="none", marker='o', markersize=6, markerfacecolor='r', label='Inflection point')
plt.annotate("(2,13)", [1, 126])


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of f(x)', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.grid()
plt.legend(loc='best')
# plt.savefig('mygraphss.png', dpi=200)
plt.show()
