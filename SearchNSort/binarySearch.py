'''
'''

def binarySearch(arr,x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high)/2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            return mid
    return 'lol'

arr = [-1,0,2,3,4,5,6,1321231]
print binarySearch(arr,1321231)
