#coins = [1,5,10,25]
coins=[4,10,25]

# def min_change(V, C):
#     m, n = len(V)+1, C+1
#     table = [[0] * n for x in xrange(m)]
#     for j in xrange(1, n):
#         table[0][j] = float('inf')
#     for i in xrange(1, m):
#         for j in xrange(1, n):
#             aC = table[i][j - V[i-1]] if j - V[i-1] >= 0 else float('inf')
#             table[i][j] = min(table[i-1][j], 1 + aC)
#     return table[m-1][n-1]

import time                                                

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))

        print(endTime - startTime,'ms')
        return result

    return wrapper


#DP Optimal
import sys
@timeme
def get_best_coins(coins, target):
    costs = [0]
    coins_used = [None]
    for i in range(1,target + 1):
        bestCost = sys.maxint
        bestCoin = -1
        for coin in coins:
            if coin <= i:
                cost = 1 + costs[i - coin]
                if cost < bestCost:
                    bestCost = cost
                    bestCoin = coin
        costs.append(bestCost)
        coins_used.append(bestCoin)
    ret = []    
    while target > 0:
        ret.append(coins_used[target])
        target -= coins_used[target]
    return ret

target = 36
print get_best_coins(coins, target)


def allSubSet(arr):
    result = [[]]
    current = []
    for num in arr:
        current = []
        for lists in result:
            current.append(lists+[num])
        result+=current
        #result += [ x+[num] for x in result]
    return result

def greedyChange(arr,target):
    original = target
    if arr== []:
        return []
    sol = []
    for i in arr[::-1]:
        if target - i <0:
            continue
        else:
            while target >0:
                target-=i
                sol.append(i)
                if target <0:
                    sol.pop()
                    target+=i
                    break
    print sol
    print sum(sol)
    if sum(sol)!=original:
        return []
    else:
        return sol
@timeme
def findBest(coins,target):
    lists = allSubSet(coins)
    cost = 99999
    currentBestSolution = []
    for l in lists:
        greedy = greedyChange(l,target)
        if len(greedy)!=0:
            if len(greedy) < cost:
                cost = len(greedy)
                currentBestSolution = greedy
    return currentBestSolution

#


#print greedyChange(coins,2569)







