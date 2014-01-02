def findKth(arr,k):
    counterMap = {}
    for item in arr:
        print counterMap
        if len(counterMap.keys()) != k:
            try: 
                counterMap[item]+=1
            except:
                counterMap[item]= 1
        else:
            while len(counterMap.keys()) !=k:
                for k in counterMap.keys():
                    counterMap[k]-=1
                    if counterMap[k] ==0:
                        counterMap.pop(k)
    return counterMap

print findKth([2,2,3,3,3],2)            
