'''
find the maximum k number in an array
'''

import Queue

def solution(arr,k):
    pq = Queue.PriorityQueue()
    for item in arr:
        pq.put(-item)
    result = []
    help(pq)
    for i in range(k):
        result.append(-pq.get_nowait())
    return result

print solution([312,3,43,2141,5,3654,432412,5,5342,543,53],5)