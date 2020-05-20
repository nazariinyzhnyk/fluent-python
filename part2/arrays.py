import array
import random
from collections import deque

import numpy as np

a = [random.random() for _ in range(100000)]
print(a)
a = array.array('d', (random.random() for _ in range(100000)))
print(a)

a = np.arange(12)
print(a)
print(a.shape)

a.shape = 3, 4
print(a)

a = a.transpose()
print(a)

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 12, 12])
print(dq)

dq.extendleft([11, 23, 45])
print(dq)
