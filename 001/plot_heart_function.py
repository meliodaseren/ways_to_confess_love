#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

y, x = np.ogrid[-2:2:100j, -2:2:100j]
plt.contour(x.ravel(), y.ravel(), (x**2+y**2-1)**3 - x**2*y**3, [0])
plt.savefig('./001/001_heart.png')
plt.show()

