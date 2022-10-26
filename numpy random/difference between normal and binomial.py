from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(loc=50, scale=5, size=1000)
y = random.binomial(n=100, p=0.5, size=1000)

sns.kdeplot(x, label='normal')
sns.kdeplot(y, label='binomial')

plt.show()