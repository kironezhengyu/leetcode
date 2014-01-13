from collections import deque

actor_info = { "act1" : ["movieC", "movieA"], "act2" : ["movieA", "movieB"], 
     "act3" :["movieA", "movieB"], "act4" : ["movieC", "movieD"], 
     "act5" : ["movieD", "movieB"], "act6" : ["movieE"], 
     "act7" : ["movieG", "movieE"], "act8" : ["movieD", "movieF"], 
     "KevinBacon" : ["movieF"], "act10" : ["movieG"], "act11" : ["movieG"] }

movie_info = {'movieB': ['act2', 'act3', 'act5'], 'movieC': ['act1', 'act4'], 
      'movieA': ['act1', 'act2', 'act3'], 'movieF': ['KevinBacon', 'act8'], 
      'movieG': ['act7', 'act10', 'act11'], 'movieD': ['act8', 'act4', 'act5'], 
      'movieE': ['act6', 'act7']}
for i in movie_info:
    actor_info[i] = movie_info[i]
print actor_info
def shortest_dictance(actor1,actor2,actor_info,movie_info):
    visited = {actor1: None}
    queue = deque([actor1])
    while queue:
        print visited
        node = queue.popleft()
        if node == actor2:
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for neighbour in actor_info[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                queue.append(neighbour)
    raise NotFound('No path from {} to {}'.format(actor1, actor2))
                    


for i in movie_info:
    actor_info[i] = movie_info[i]




#print shortest_dictance("act1", "KevinBacon", actor_info, movie_info)