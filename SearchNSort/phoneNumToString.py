digit_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}



def num_to_word(input):
  input = str(input)
  result = ['']
  for char in input:
    if char not in digit_map:
      raise Exception('invalid Input')
    letters = digit_map[char]
    result = [prefix+letter for prefix in result for letter in letters]
  return result


def permut(s,l):
    print("Entering function permut()")
    print("Parameters:\ns: {}\nl: {}".format(s,l))
    if l == []: 
        print("End of recursion reached, returning {}".format([[s]]))
        return [[s]]
    result = []
    for e in permut(s, l[1:]):
        result.append(e + [l[0]])
    result += [l + [s]]
    print("Returning {}".format(result))
    return result

print all_perms('a','bc')








