import random
# print(dir(random))

r = random.random() # b/w 0 - 1 
print(r)

r = random.randint(100001,999999)
print(r)

r = random.randrange(1,8,2)
print(r)

r = random.uniform(10.2,14.3)
print(r)

import random as r
ls = [1,2,3,4,5,6]
ra = r.shuffle(ls)
print(ls)

from random import choice, sample
ls = []
for i in range(10,4536):
    ls.append(i)
print(sample(ls,3))

from random import choices as ch
ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
winner = ch(ls,k=3)
print(winner)

from random import *

'''
import pandas
import pandas as pd
from random import *
from random import randint
from random import randrange as ra
from random import random, shuffle, uniform



package: collection of multiple modules for a specific task.

package have a default file __init__.py
Empty file (__init__.py)
'''
