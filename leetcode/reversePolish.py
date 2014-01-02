def solution(arr):
    operands = ['+','-','*','/']
    stack = []
    for token in arr:
        # print token
        try:
            int(token)
            stack.append(token)
            continue
        except:
            if token in operands:
                temp =0
                num2 = stack.pop()
                num1 = stack.pop()
                temp = eval(str(num1)+token+str(num2))
                stack.append(temp)
                continue
            else:
                raise Exception('Invalid Token')
    return stack.pop()

print solution(["2", "1", "+", "3", "*"])
