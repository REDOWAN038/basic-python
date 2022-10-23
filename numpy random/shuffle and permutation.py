import numpy as np
from numpy import random

#shuffle
# change the original array

arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

#permutation 
# create another array (original remains unchange)

newArr = random.permutation(arr)
print(newArr)