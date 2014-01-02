'''
midified binaray search
'''
from __future__ import division
import random
from math import fabs
DIFF = 10**-10


#binary search
def sqrt(x):

    if x == 0: return 0
    elif x < 0: return None
    elif x == 1: return 1
    elif x > 1:
        low = 1; high = x
    else: # x < 1
        low = 0; high = 1
    
    while low < high:
        mid = (low+high)/2
        if fabs(mid*mid-x) < DIFF: return mid
        elif x > mid*mid: low = mid
        else: high = mid
    return low

print sqrt(12341)

#linear search
def sqrt1(num):
    if num ==0:
        return 0
    if num <1:
        return 'not yet support'
    for i in xrange(num):
        if fabs(i**2 - num)< DIFF:
            return i
        elif i**2 > num:
            return i -1
print sqrt1(12341)
