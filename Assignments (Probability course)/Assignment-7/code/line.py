import matplotlib.pyplot as plt
import numpy as np

# specifying the plot size
plt.figure(figsize = (8, 5), dpi = 100)

plt.axvline(x = 2, color = 'b', linestyle='--', label = 'axvline - full height')
plt.axvline(x = 5, color = 'b', linestyle='--',  label = 'axvline - full height')
plt.axvline(x = 3, color = 'g', label = 'axvline - full height')
plt.axvline(x = 6, color = 'g', label = 'axvline - full height')

plt.savefig('line.png', dpi=300)

 # Coloring the region A = BLUE , B = GREEN , AB = BLUE+GREEN = dark green color
# fig, ax = plt.subplots()
# ax.axvspan(2, 5, alpha=0.5, color='blue')
# ax.axvspan(3, 6, alpha=0.5, color='green')


plt.show()
