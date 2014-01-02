'''
Given an array of integers, every element appears twice 
except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
'''

def singleNumber1(arr):
    res = 0

    for i in xrange(len(arr)):
        res ^= arr[i]
    return res

print singleNumber1([1,2,3,4,1,2,3])

'''

Given an array of integers, every element 
appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime 
complexity. Could you implement it without using extra memory?
'''


