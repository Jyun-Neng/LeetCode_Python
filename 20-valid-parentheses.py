"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example:

Input: "([)]"
Output: false
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {'}': '{', ']': '[', ')': '('}
        for char in s:
            if char in table:
                if not stack:
                    return False
                if table[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True


if __name__ == "__main__":
    print(Solution().isValid("([)]"))
