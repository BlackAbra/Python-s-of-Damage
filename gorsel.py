import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0,6,3,6])
# ypoints = np.array([0,10,4,7])

# plt.plot(xpoints,ypoints)
# plt.show()


# print(matplotlib.__version__)

ypoints = np.array([0,10,4,7]) 
plt.plot(ypoints)
plt.bar(ypoints,xpoints)
plt.show()
