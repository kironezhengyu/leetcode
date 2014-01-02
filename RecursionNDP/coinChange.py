#coins = [1,5,10,25]

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


coinsOptions = [1, 2, 3]
def numberOfWays(target):
    if (target < 0):
        return 0
    elif(target == 0):
        return 1
    else:
        return sum([numberOfWays(target - coin) for coin in coinsOptions])
print numberOfWays(5)


target = 5
coins = [1,2,3]
ways = [1]+[0]*target
for coin in coins:
    for i in range(coin, target+1):
        ways[i]+=ways[i-coin]
print ways[target]

#print min_change(coins,13)