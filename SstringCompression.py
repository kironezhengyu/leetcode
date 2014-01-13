'''
ng aabcccccaaa would become  a2blc5a3. If the "compressed" string would not
'''

def solution(string):
    counter = 1
    previous = string[0]
    res= ''
    for s in string[1:]:
        if s==previous:
            counter+=1
            previous=s
        else:
            res+=previous+str(counter)
            previous=s
            counter=1
    res+=previous+str(counter)    

    return res

print solution('aabcccccaaab')
