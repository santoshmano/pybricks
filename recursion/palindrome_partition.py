# Time:  O(2^n)
# Space: O(n)
# recursive solution
class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        self.partitionRecu(result, [], s, 0)
        return result

    def partitionRecu(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur))
        else:
            for j in range(i, len(s)):
                if self.isPalindrome(s[i: j + 1]):
                    cur.append(s[i: j + 1])
                    self.partitionRecu(result, cur, s, j + 1)
                    cur.pop()

    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True


if __name__ == "__main__":
    result = Solution2().partition("abaa")
    for i in result: print(i)