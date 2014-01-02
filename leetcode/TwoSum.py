'''
Given an array of integers, find two numbers such
 that they add up to a specific target number.

The function twoSum should return indices of the 
two numbers such that they add up to the target, 
where index1 must be less than index2. Please note
 that your returned answers (both index1 and index2) 
 are not zero-based.

You may assume that each input would have exactly 
one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''



def hashMapSol(arr, target):
    table = {}
    result = []
    for number in arr:
        counter = 0
        table[number] = counter
        counter+=1
    for number in arr:
        remainder = target - number
        if remainder in table.keys():
            result.append((number,remainder))
    return result
# hashSet sol
def twoSum2(arr,target):
    if len(arr)<2:
        return
    seen = set()
    output= []
    for num in arr:
        temp = target - num
        if temp not in seen:
            seen.add(num)
        else:
            output.append((num,temp))
    return output


print twoSum2([2,2,11,1,3],4)

