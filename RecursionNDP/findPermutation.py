def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

print perms('hello')


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


#print permutation('hello')