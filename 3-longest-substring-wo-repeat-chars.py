'''
Given a string, find the length of the longest substring without repeating characters.
Input: "pwwkew"
Output: 3 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:

    def __init__(self):
        """docstring for init"""
        self.substr = []
        self.length = 0

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        for char in s:
            new_substr = []
            if char in self.substr:
                if len(self.substr) > self.length:
                    self.length = len(self.substr)
                for rev in self.substr[::-1]:   # backward trace
                    if rev == char:
                        break
                    new_substr.append(rev)
                self.substr = []
                self.substr = new_substr[::-1]  # reverse list
            self.substr.append(char)            # add last character
        if len(self.substr) > self.length:
            self.length = len(self.substr)
        return self.length


sol = Solution()
string = "pwwkew"
length = sol.lengthOfLongestSubstring(string)
print(length)
