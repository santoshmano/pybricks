class TrieNode():
    def __init__(self, letter=''):
        self.children = {}
        self.is_word = False

    def lookup_letter(self, c):
        if c in self.children:
             return True, self.children[c].is_word
        else:
             return False, False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.is_word = True

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

def build_prefix(dictionary):
    trie = Trie()
    for word in dictionary:
        trie.add(word)
    return trie


def find_words(dictionary, board):
    result = []
    prefix = build_prefix(dictionary)
    boggle(board, prefix, result)
    return result


def boggle(board, prefix, result):
    #print(board, len(board[0]), len(board))
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for r in range(0, len(board)):
       for c in range(0, len(board[0])):
          str = []
          _boggle(board, visited, prefix.root, result, r, c, str)

def _is_valid(visited, i, j):
    if (i < 0) or (i >= len(visited)) or \
       (j < 0) or (j >= len(visited[0])) or \
       visited[i][j] == True:
           return False
    return True


def _boggle(board, visited, node, result, row, col, str):
    print(node.children)
    print(visited)
    c = board[row][col]
    present, is_word = node.lookup_letter(c)

    if present == False:
        return

    str.append(c)
    if is_word == True :
        result.append("".join(str))
        print(result)

    visited[row][col] = True
    for i in row-1, row, row+1:
        for j in col-1, col, col+1:
            if _is_valid(visited, i, j):
                _boggle(board, visited, node.children[c], result, i, j, str)
    str.pop()
    visited[row][col] = False


dictionary = ["geek", "geeks", "boy"]

board = [["g", "b", "o"],
         ["e", "y", "s"],
         ["s", "e", "k"]]

res = find_words(dictionary, board)
