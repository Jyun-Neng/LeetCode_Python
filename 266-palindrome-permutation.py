"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""
import collections


class Solution():
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool 
        """
        cnt = collections.Counter(s)
        mid = [char for char, n in cnt.items() if n % 2]
        if len(mid) > 1:
            return False
        return True


if __name__ == "__main__":
    s = 'addad'
    print(Solution().canPermutePalindrome(s))
