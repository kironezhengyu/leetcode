def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return (a,b)
print swap(3,6)


def trailingZero(num):
    zeros = num/5
    return zeros+1

print trailingZero(1000)