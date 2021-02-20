import re

def get_words_py(text):
    return re.sub(r'[^a-z0-9]',' ',text.lower()).split()

def read_file(filename):
    try:
        file = open(filename, "r")
        text = file.read()
    except Exception as e:
        print("unable to open file: {} due to: {}"
                .format(filename, str(e)))
        return None
    return text

# hash index implementation of reverse index
def build_hash_index(words):
    index = {}
    for i, word in enumerate(words):
        if word not in index:
            index[word] = []
        index[word].append(i)
    return index

def get_pos_from_hash_index(index, word):
    pos = []
    if word in index:
        pos = index[word]
    return pos

class TrieNode():
    def __init__(self, letter=''):
        self.letter = letter
        self.children = {}
        self.is_word = False
        self.index = []

# trie implementation of reverse index
class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, pos):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            cur = cur.children[letter]
        cur.is_word = True
        cur.index.append(pos)

    def lookup(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return []
            cur = cur.children[letter]
        if cur.is_word:
            return cur.index
        else:
            return []

# trie implementation
def build_trie_index(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.add(word, i)
    return trie

if __name__ == "__main__":
    text = read_file("text.txt")
    words = get_words_py(text)

    hash_index = build_hash_index(words)
    trie_index = build_trie_index(words)

    lookup_words = ["a", "juliet", "ran", "and"]

    print(hash_index)

    for word in lookup_words:
        pos = get_pos_from_hash_index(hash_index, word)
        print(word, "postions in hash index", pos)
        pos = trie_index.lookup(word)
        print(word, "postions in hash index", pos)
