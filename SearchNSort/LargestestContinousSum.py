
def largestSum(arr):
    if len(arr)==0:
        return 0
    maxSum = currentSum = arr[0]
    result  =[]
    for num in arr[1:]:
        currentSum = max(currentSum+num,num)
        maxSum = max(currentSum,maxSum)

    print result
    return maxSum


print largestSum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
