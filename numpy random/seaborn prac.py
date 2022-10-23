import matplotlib.pyplot as plt
import seaborn as sns

#sns.distplot([0,1,2,3,4,5])
#sns.distplot([0,1,2,3,4,5], hist=False)
sns.kdeplot([0,1,2,3,4,5])
plt.show()