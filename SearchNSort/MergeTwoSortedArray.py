'''
two sorted array,
A is bigger than b
merge them
'''

#O(n+m) space
def mergeAB(a,b):
    res = []
    i=j=0
    while i < len(a) and j <len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
            i+=1
    #leftovers
    while i < len(a):
        res.append(a[i])
        i+=1
    while j < len(b):
        res.append(b[j])
        j+=1
    return res


#print mergeAB([1,2,3,4,5,6,7,8,9],[-1,-2,3,8,123])


def mergeAB2(a,b):
    #merge from back of the a array
    lastA = len(a)-1
    lastB = len(b)-1
    a.extend(b)
    mergeIndex = len(a) - 1
    while lastB >= 0 and lastA >= 0:
        if a[lastA] > b[lastB]:
            a[mergeIndex] = a[lastA]
            mergeIndex-=1
            lastA-=1
            
        else:
            a[mergeIndex]  = b[lastB]
            mergeIndex-=1
            lastB-=1
    while lastB>=0:
        a[mergeIndex] = b[lastB]
        mergeIndex-=1
        lastB-=1
    return a

print mergeAB2([1,2,3,4,5,6,7,8,9],[-1,-2,3,8,123])
