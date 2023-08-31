notas=[10,8.5,9.75,6.25,3.75,2.75,4.75,7,8]

print("Count = {}".format(len(notas)))
print("Max = {}".format(max(notas)))
print("Min = {}".format(min(notas)))

import numpy as np
print("Round = {}".format(list(np.round(notas,1))))