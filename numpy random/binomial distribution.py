from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.binomial(n=10, p=0.5, size=20)
sns.histplot(x)
plt.show()