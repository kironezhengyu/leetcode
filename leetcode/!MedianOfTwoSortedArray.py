'''
There are two sorted arrays A and B of size m 
and n respectively. Find the median of the two 
sorted arrays. The overall run time complexity 
should be O(log (m+n)).
'''

'''
find the kth smallest number, and we are done
where k is the m+n / 2 
if m+n is even return m+n /2  +1 th as well
'''
def findMedian(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    median =  (m + n) /2
    i =0
    j =0
    current = 0
    while median >0 :
        
        if arr1[i] < arr2[j]:
            current = arr1[i]
            i+=1
            median-=1
        if arr2[j] < arr1[i]:
            current = arr2[j]
            j+=1
            median-=1
        if arr2[j] == arr1[i]:
            current = arr2[j]
            i+=1
            j+=1
            median-=2
    return current

print findMedian([0,1,3,4],[5,6,7,8,9])

