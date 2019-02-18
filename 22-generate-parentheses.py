"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def backtrack(self, left, right, valid):
        if not left and not right:
            self.ans.append("".join(valid))
        else:
            if len(left) == len(right):
                valid += left.pop()
                self.backtrack(left, right, valid)
                valid.pop()
                left.append('(')
            else:
                for c in "()":

                    if c == '(' and left:
                        left.pop()
                    elif c == ')' and right:
                        right.pop()
                    else:
                        continue
                    valid += c
                    self.backtrack(left, right, valid)
                    valid.pop()
                    if c == '(':
                        left.append(c)
                    else:
                        right.append(c)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        left = ['('] * n
        right = [')'] * n
        valid = []
        self.backtrack(left, right, valid)
        return self.ans


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
