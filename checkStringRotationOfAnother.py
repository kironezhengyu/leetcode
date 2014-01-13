'''
f s1 = "stackoverflow" then the following are some of its rotated versions:

"tackoverflows"
"ackoverflowst"
"overflowstack"
'''

#concatanate string1 should contain combination of rotation
def solution(s1,s2):
    if s2 not in s1+s1:
        return False
    return True

print solution('stackoverflow','stackoverflwo')