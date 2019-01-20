"""
Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].
Given s = "abc", return [].
"""
import collections


class Solution():
    def backtrack(self, tmp):
        if len(tmp) == self.size:
            string = ''.join(tmp)
            self.res.append(string + self.mid + string[::-1])
        for i in range(self.size):
            if self.visit[i]:
                continue
            # half[i-1] and half[i] are the same, so it does not require to add half[i] to tmp again
            if i > 0 and self.half[i] == self.half[i - 1] and not self.visit[i - 1]:
                continue
            self.visit[i] = True    # half[i] is added to tmp list
            tmp.append(self.half[i])
            self.backtrack(tmp)
            tmp.pop()
            self.visit[i] = False

    def generatePalidromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        self.mid = [char for char, n in cnt.items() if n % 2]
        if len(self.mid) > 1:
            return []
        self.mid = '' if self.mid == [] else self.mid[0]
        self.half = ''.join(char * (n // 2)
                            for char, n in cnt.items())  # left half string
        self.half = [char for char in self.half]  # convert to list
        self.size = len(self.half)
        self.visit = [False for i in range(self.size)]
        self.res = []
        self.backtrack([])
        return self.res


if __name__ == "__main__":
    s = 'abbc'
    print(Solution().generatePalidromes(s))
