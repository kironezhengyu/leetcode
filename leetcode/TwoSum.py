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

def twoSum( numbers, target):
    hash ={}
    counter = 1
    for num in numbers:
        if num in hash.keys():
            hash[num] = [counter,hash[num]]
        else:
            hash[num] = counter
        counter+=1
    for num in numbers:
        difference = target - num
        if difference in hash.keys() and hash[num]!=hash[difference]:
            return hash[difference],hash[num]
        elif difference == num and isinstance(hash[num],list):
            return hash[num][1],hash[num][0]

def twoSum3(numbers,target):
    map = {}
    counter = 0
    while numbers[counter] not in map.keys():
        difference = target - numbers[counter]
        map[difference] = counter
        counter+=1
    return map[numbers[counter]]+1, counter+1

print twoSum3([3,2,4],6)
print twoSum3([0,4,3,0],0)
print twoSum3([448,74,41,680,719,173,774,492,636,199,362,792,74,647,587,678,261,874,467,462,735,582,999,479,34,294,702,834,239,853,349,142,690,81,324,188,813,931,502,707,967,895,445,878,426,430,93,255,304,928,960,192,452,211,495,787,328,568,313,194,608,990,944,256,204,616,44,991,461,59,854,348,611,535,459,724,213,683,777,885,460,751,450,918,806,395,454,603,57,655,110,542,24,82,777,395,877,229,550,685,142,845,139,804,353,111,599,114,679,728,82,137,274,490,340,244,880,982,281,852,568,428,474,348,487,432,749,586,983,402,386,210,300,864,29,980,715,911,738,375,688,515,374,945,513,392,999,214,658,920,695,391,880,600,916,235,384,763,943,399,958,826,663,844,733,461,226,616,536,246,155,83,732,940,392,176,806,925,377,824,465,175,342,291,113,186,410,490,170,32,701,162,471,742,297,791,541,243,885,603,292,933,948,326,894,686,316,341,119,610,276,463,883,849,854,682,304,737,99,760,411,426,445,682,794,541,147,520,576,644,727,499,369,222,226,836,354,53,996,868,37,42,293,271,452,181,219,125,943,149,591,599,972,961,351,545,928,922,376,917,621,777,844,655,151,881,125,877,258,291,566,76,58,18,692,815,448,224,286,191,110,655], 74)

