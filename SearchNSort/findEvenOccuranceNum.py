''''For example, let’s say we’re given the following array: 
[2, 1, 3, 1]. First we get all the unique elements [1, 2, 3].
 Then we construct a new array from the original array and the 
 unique elements by appending them together [2, 1, 3, 1, 1, 2, 3]. 
 We XOR all the elements in this new array. The result is 2^1^3^1^1^2^3 = 1. 
 Because the numbers 2 and 3 occur in the new array even number of times (2 times), 
 so they’ll be XORed with themselves odd times (1 time), which results in 0. 
 The number 1 occurs odd number of times (3 times), so it’ll be XORed with 
 itself even times (2 times), and the result is the number 1 itself. 
 Which is the even occurring element in the original array. Here’s the code of this approach: 
'''
def getEven2(arr):
    allNum = set(arr)
    arr.extend(allNum)
    result = 0
    for num in arr:
        result^=num
    return result


print getEven2([2,3,4,1,4])