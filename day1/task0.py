# An one line comment starts with '#'

#---------
# This is just a hello world program

print("Hello world!")

#---------

## A multiline comment starts and ends with """
"""
This is a comment
written in
more than just one line
"""

#---------

# checking python version
import sys
print(sys.version)

#---------
#Using numpy and matplotlib in google collaboratory

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
