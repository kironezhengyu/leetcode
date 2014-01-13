'''
minimal transformation from one word to another
from cat, bat, bet, bed, at, ad, ed
'''

import collections
from collections import deque,defaultdict
words = ["hot","dot","dog","leg","dig","die","lie","doe","lot","log","cog","hit"]

def genGraph(arr):
    graph=collections.defaultdict(list)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for word in arr:
        for i in range(len(word)):
            #remove a char
            removed  = word[:i]+word[i+1:]
            if removed in arr:
                graph[word].append(removed)
            #change a letter
            for char in letters:
                changed = word[:i]+char+word[i+1:]
                if changed in arr and changed!=word:
                    graph[word].append(changed)
        #add char
        for i in range(len(word)+1):
            for char in letters:
                added = word[:i]+char+word[i:]
                if added in arr:
                    graph[word].append(changed)
    return graph


graph=  genGraph(words)

def getWordTransformation(graph,word1,word2):
    #bfs
    print graph
    visited = {word1:None}
    q = deque([word1])
    while q:
        node = q.popleft()
        if node == word2:
            path =[]
            print visited
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                q.append(neighbour)

    return []



print getWordTransformation(graph,'lot','dig')



'''
subproblems ,
1. on x[i:] and y[j:] O(n)
2. guess:  x[0] to y[0]: replace/delete/insert
3. recurrence: min(three options)
    1. cost of replace:
    2. insert y[j]
    3. delete x[i]
4. for i = [x..0]
    for j in [x..0]

0..........y
|
|         insert
|     (x)y+1
|      x+1 x+1,y+1
|
|
x



'''

    #word_ladder("hit", "lot", words)
#word_ladder_II2("hit", "cog", words)
# word_ladder_II2("dot", "log", words)
# word_ladder_II2("die", "cog", words)
# word_ladder_II2("die", "leg", words)
# word_ladder_II2("lot", "dig", words)







