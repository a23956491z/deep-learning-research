import numpy as np
arr = [ [1,2], [2,3], [3,4], [4,5], [5,6], [6,7]]
arr = np.array(arr)
print([arr[:3], arr[4:]])
print(np.concatenate([arr[:3], arr[4:]], axis=0))
