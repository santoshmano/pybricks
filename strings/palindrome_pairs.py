# Palindrome Pairs
# 	Given a list of words, find pairs that when concatenated
# 	will form a palindrome

# Add the list of words into a trie in the reverse order
# For every word find if in Trie,
#	- if found, check if the remainder of string is a palindrome

class TrieNode():
    def __init__(self):
        self.array_index = -1
	self.is_word = False
	self.children = {}

def add_word(root, word, index):
	cur = root
	for i in range(len(word)-1, -1, -1):
		if word[i] not in cur.children:
			cur.children[letter] = TrieNode()
		cur = cur.children[letter]

	cur.is_word = True
	cur.array_index = index

def find_pairs(root, words, word, index, result):
	cur = root
	for i in range(0, len(word)):
            if (i == (len(word)-1)):
                return

def palindrome_pairs(words):
	root = TrieNode()
	result = []

	for i, word in enumerate(words):
		add_word(root, word, i)

	for i, word in enumerate(words):
		find_pairs(root, words, word, i, result)

	return result

if __name__ == "__main__":
	trie = Trie()
	words = ["aaa", "aa", "ba"]

	for i, word in enumerate(words):
		trie.add(word, i)

	print(trie.find("aa"))
	print(trie.find("aab"))
	print(trie.find("ba"))
	print(trie.find("aa"))
	print(trie.find("311"))