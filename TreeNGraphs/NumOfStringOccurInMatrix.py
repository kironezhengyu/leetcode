def DFS(M, x, y, s, MatchSoFar):
    if x >= len(M) or y >= len(M[0]) or M[x][y] != s[0]:
        return 0

    ## s[0] matched; if this is the only character in string
    ## then there is a word match
    if len(s) == 1:
        print MatchSoFar+[(x,y)]
        return 1

    ## search in child nodes for rest of string match
    num_matches = 0
    for (X, Y) in [(x, y+1), (x+1, y), (x+1, y+1)]:
        num_matches += DFS(M, X, Y, s[1:], MatchSoFar+[(x,y)])

    return num_matches

## MAIN
M = [
['w' , 's' , 'r' , 't' , 'g' , 'g' ],
['a' , 'a' , 'c' , 'h' , 'i' , 'n' ], 
['k' , 'c' , 'h' , 'u' , 'j' , 'j' ],
['o' , 'h' , 'i' , 'n' , 'y' , 'q' ],
]


num_matches = 0
for x in range(len(M)):
    for y in range(len(M[0])):
        num_matches += DFS(M, x, y, "sachin", [])

print num_matches
