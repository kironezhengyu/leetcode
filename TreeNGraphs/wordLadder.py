'''
minimal transformation from one word to another
from cat, bat, bet, bed, at, ad, ed
'''

import collections
from collections import deque
def genGraph(arr):
    graph=collections.defaultdict(list)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for word in arr:
        for i in range(len(word)-1):
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


graph=  genGraph(['cat', 'bat', 'bet', 'bed', 'at', 'ad', 'ed'])

def getWordTransformation(graph,word1,word2):
    #bfs
    print graph
    visited = {word1:None}
    q = deque([word1])
    while q:
        print visited
        node = q.popleft()
        if node == word2:
            path =[]
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[-1]
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                q.append(neighbour)
    return []



print getWordTransformation(graph,'cat','bed')


