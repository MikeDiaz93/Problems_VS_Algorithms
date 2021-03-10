# Represents a single node in the Trie
from ipywidgets import interact
from IPython.display import display
from ipywidgets import widgets


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = {}
        self.is_complete = False

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        r = self.suffixes_aux(suffix)
        ans = []
        for item in r:
            ans.append(item[len(suffix):])

        return ans

    def suffixes_aux(self, suffix):

        results = []
        if self.is_complete:
            results.append(suffix)

        for (value, child) in self.children.items():
            results.extend(child.suffixes_aux(suffix + value))

        return results


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        aux = self.root

        for char in word:
            if char not in aux.children:
                aux.insert(char)

            aux = aux.children[char]

        aux.is_complete = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix

        aux = self.root
        for char in prefix:
            if char not in aux.children:
                return None

            aux = aux.children[char]

        return aux


# original test
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='');


# test 2
MyTrie2 = Trie()
wordList2 = [
    "hello", "hi", "height",
    "kilogram", "king", "kurzgesagt", "kodak", "kurdistan",
    "deutsche", "deuces", "deus","deuteronomy"
]

for word in wordList2:
    MyTrie2.insert(word)

    
prefix_node = MyTrie2.find("")
print(prefix_node.suffixes())
#expected output: ["hello", "hi", "height", "kilogram", "king", "kurzgesagt", "kodak", "kurdistan","deutsche", "deuces", "deus","deuteronomy"]

prefix_node = MyTrie2.find("h")
print(prefix_node.suffixes())
#expected output: ["ello", "i", "eight"]

prefix_node = MyTrie2.find("deu")
print(prefix_node.suffixes())
#expected output: ["tsche", "ces", "s", "teronomy"]

prefix_node = MyTrie2.find("deuteronomy")
print(prefix_node.suffixes())
#expected output: []
