def perm1(prefix, string):
    n = len(string)
    if n==0 :
        print prefix
    else:
        for i in range(n):
            perm1(prefix + string[i],  string[0:i] + string[i+1:n])


def perm(string):
    perm1('',string)


def permutation(string):
    if len(string) <=1:
        return [string]
    perms = permutation(string[1:])
    result = []
    for perm in perms :
        print 'single perm ',perm
        for i in range(len(perms)+1):
            result.append(perm[:i] + string[0] + perm[i:])
    return result


print permutation('')