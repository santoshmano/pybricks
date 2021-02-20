class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.is_word = True

    def lookup(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True if cur.is_word else False

    def delete(self, word):
        return


if __name__ == "__main__":

    trie = Trie()

    trie.insert("hello")
    trie.insert("hello world")
    trie.insert("hell")
    trie.insert("yellow")
    trie.insert("world")

    assert(trie.lookup("world") == True)
    assert(trie.lookup("worl") == False)
    assert(trie.lookup("hell") == True)
    assert(trie.lookup("hello") == True)
    assert(trie.lookup("cat") == False)

    assert(trie.lookup("hello world") == True)
    trie.delete("hello world")
    assert(trie.lookup("hello world") == False)
