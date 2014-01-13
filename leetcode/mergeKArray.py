'''
PQ
'''
import heapq

def addtoheap(h, i, it):
    try:
        heapq.heappush(h, (next(it), i))
    except StopIteration:
        pass

def mergek(*lists):
    its = map(iter, lists)
    h = []
    for i, it in enumerate(its):
        addtoheap(h, i, it)
    while h:
        v, i = heapq.heappop(h)
        addtoheap(h, i, its[i])
        yield v
def magic(arr):
    heap = [(l[0],i,0) for i,l in enumerate(arr) if len(l) > 0]
    print heap
    heapq.heapify(heap)
    print heap
    lst = []
    while heap:
        item,lst_index,item_index = heapq.heappop(heap)
        lst.append(item)
        if item_index + 1 < len(arr[lst_index]):
            heapq.heappush(heap,(arr[lst_index][item_index+1],lst_index,item_index+1))
    return lst

res = magic([[1, 3, 5], [2, 4, 6], [7, 8, 9], [10]])
print res