import random
class Point:
    x=0
    y=0
    def __init__(self,x=0,y=0):
        self.x =x
        self.y =y

def solution(arr):
    slopes={}
    for p1 in arr:
        for p2 in arr[1:-1]:
            try : 
                slope = (p2.y - p1.y) / float(p2.x - p1.x)
            except:
                slope = -999
            try:
                slopes[slope]+=1
            except:
                slopes[slope] =1
    return slopes
    #return sorted(slopes,key=slopes.get,reverse=True)[0:1]

res = []
for x in xrange(1,100):

    res.append(Point(random.randint(1,10),random.randint(1,10)))

print solution(res)

