# code by Donal
# april 22, 2022
# Probability CBSE class 9 - Example 10

import numpy as np

if __name__ == "__main__":

    """ Randomly selecting 5 numbers in the range [0,50] where each number has an equal
        probability of getting picked.  """
    freq = np.random.uniform(low=0.0, high=50.0, size=5)

    # class1 = number of bags in which number of seeds germinated was >40
    class1 = 0
    # class 2 = number of bags in which number of seeds germinated was exactly 49
    class2 = 0
    # class 3 = number of bags in which number of seeds germinated was >35
    class3 = 0

    # Counting the number of bags in each class
    for i in freq:
        if i > 40:
            class1 += 1
        if i == 49:
            class2 += 1
        if i > 35:
            class3 += 1

    # Displaying the categories and the number of bags in the corresponding categories side by side         
    print(
        "Seeds germinated   No. of Bags\n > 40                  %.0f\n = 49                  %.0f\n > 35 "
        "%.0f\n     " % (class1, class2, class3))
