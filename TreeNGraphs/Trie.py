
import re
#method cleans up the input and replace uppper cases and special char
def getWords(txt):
    return re.sub(r'[^a-z0-9]',' ',txt.lower()).split()
def createIndex1(txt):
    index = {}
    words = getWords(txt)
    for pos,words in enumerate(words):
        index[word].append(pos)
    return index

def query1(index,word):
    if word in index:
        return index[word]
    else:
        return None
class Node(object):
    def __init__(self,letter):
        self.letter = letter
        self.isTerminate = False
        self.children = {}
        self.position = []
class Trie(object):
    def __init__(self):
        self.root= Node('')
    def __contains__(self,word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current= current.children[letter]
        return current.isTerminate
    def __getitem__(self,word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminate =True
        return current.position

    def __str__(self): 
        self.output([self.root]) 
        return ''   
    def output(self,currentPath,indent = ''):
        #DFS
        currentNode = currentPath[-1]
        if currentNode.isTerminate:
            word = ''.join([node.letter for node in currentPath])
            print indent +word + ' ' +str(currentNode.position)
            indent+=' '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:]+[node],indent)
def createIndex2(text):
    trie = Trie()
    for pos, word in enumerate(text):
        trie[word].append(pos)
    return trie
def query2(index,word):
    if word in index:
        return index[word]
    else:
        return []


print createIndex2(['cat', 'cats', 'catsdogcats', 'catxdogcatsrat', 'dog', 'dogcatsdog', 'hippopotamuses', 'rat', 'ratcat', 'ratcatdog', 'ratcatdogcat'])