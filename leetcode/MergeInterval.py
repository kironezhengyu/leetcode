''''
given a array of intervals
return merged 
'''
class interval(object):
    def __init__(self,start=0,end=0,interval=()):
        if interval != ():
            print interval
            self.start = interval[0]
            self.end = interval[1]
        else:
            self.start = start
            self.end = end
    def __repr__(self):
        return 'start: %d, end: %d' % (self.start,self.end)
def addAll(arr):
    result = []
    for i in range(len(arr)):
        r =  interval(arr[i])
        result.append(r)
    return result
print addAll([(1,2),(3,5),(6,7),(8,10),(12,16),(4,9)])



def mergeInterval(arr):
    previous = arr[0]
    print previous
    result = []
    for inter in arr[1:]:
        print inter
        if inter.end < previous.start:
            print inter.end < previous.start
            result.append(inter)
        elif inter.start >previous.end:
            result.append(previous)
            previous = inter
        #merge into new interval
        else:
            previous = interval(min(previous.start,inter.start),
                max(previous.end,inter.end))

    result.append(previous)
    return result
oneThree = interval(1,3)
sixNine= interval(6,9)
twoFive = interval(2,5)

#print mergeInterval([oneThree,twoFive,sixNine])



