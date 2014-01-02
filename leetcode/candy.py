def candy(scores):
    print scores
    n = len(scores)
    candies = [1]*n
    # left --> right
    # add one if score > child on the right
    for i in range(1,n):
        if scores[i] > scores[i-1]:
            candies[i] = max(candies[i], candies[i-1]+1)
        elif scores[i] == scores[i-1]:
            candies[i] = max(candies[i], candies[i-1])
    print candies
    # right --> left
    # add one if score > child on the left
    for i in reversed(range(n-1)):
        if scores[i] > scores[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)
        elif scores[i] == scores[i+1]:
            candies[i] = max(candies[i], candies[i+1])
    print candies
    return candies

if __name__ == '__main__':
    candy([1,2,3,7,2,0,0,3,2,10])





def solution(arr):
    

