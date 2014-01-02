def isBalanced(string):
    openings = ['(','{','[']
    combinations = [('(',')'), ('[',']'), ('{','}')]
    stack = []
    if len(string)%2 !=0:

        return False
    for cha in string:
        if cha in openings:
            stack.append(cha)
        else:
            if len(stack)==0:
                return False
            else:
                match = stack.pop()
                if (match,cha) in combinations:
                    return True
    if len(stack)==0:
        return True


print isBalanced('()(){}[')
