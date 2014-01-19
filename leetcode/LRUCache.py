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


    def get(self):
        return self.items.pop(0)

    def __repr__(self):
        return str(len(self.items))

        
r =[1,2,3,4,5,6,6,1,1,1,1,1,1,1,5,5,5,5,5,5]
print r
test = LRUCache(10,r)

print test

print test.get()
print test.get()
