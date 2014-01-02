import random
class LRUCache():
    capacity =0
    items = []
    zoo = {}
    def __init__(self,capacity=0,arr=None):
        self.capacity = capacity
        if arr != None:
            for item in arr:
                self.set(item)
    def set(self,key,value=1):
        try:
            self.zoo[key] +=1
        except:
            self.zoo[key] = 1
        self.items = sorted(self.zoo,key=self.zoo.get,reverse=True)[:self.capacity-1]


    def get(self,key):
        if key in self.items:
            return self.zoo[key]
        else:
            return -1

    def __repr__(self):
        return ','.join([str(i) for i in self.items])

r =[random.randrange(0,9) for n in range(100)]
print r
test = LRUCache(10,r)

print test

print test.get(2)
print test.get(11)
