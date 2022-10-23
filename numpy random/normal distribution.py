
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# loc ------> (Mean) where the peak of the bell exists.

# scale ------> (Standard Deviation) how flat the graph distribution should be.

# size ------> The shape of the returned array.


#  x = random.normal(loc=1, scale=2, size=(2,3))
sns.kdeplot(random.normal(loc=3, scale=3, size=1000))
plt.show()