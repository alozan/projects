import time 
import numpy as np

start = time.time()
# vectorized sum - using numpy for vectorization
# np.arange create the sequence of numbers from 0 to 1499999
print(np.sum(np.arange(100000000)))
end = time.time()
print(end - start)

