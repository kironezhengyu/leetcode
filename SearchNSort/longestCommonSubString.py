'''
[[0,0,0,0]
 [0,0,1,0]
 [0,1,0,2]
 [0,0,2,0]]
'''

'''
leetleetcode
bunnybunbunny
'''

herp = ""
 
def isPalindrome(s):
    if s == s[::-1] :
        return True
 
s = 'abaccddccefe'
 
for idy, _ in enumerate(s):
    for idx, _ in enumerate(s):
        derp = s[idy:idx+1]
        if isPalindrome(derp) and (len(derp) > len(herp)):
            herp = derp
 
print(herp)



