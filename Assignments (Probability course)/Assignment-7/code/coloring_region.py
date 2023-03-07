import matplotlib.pyplot as plt
import numpy as np

# Coloring the region A = BLUE , B = GREEN , AB = BLUE+GREEN = teal color
fig, ax = plt.subplots()
ax.axvspan(2, 5, alpha=0.5, color='blue')
ax.axvspan(3, 6, alpha=0.5, color='green')

plt.savefig('coloring_region.png', dpi=300)


plt.show(
