"""
Given a  32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example:

Input: 123
Output: 321
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x = str(abs(x))
        x = x[::-1]
        rev = int(''.join(x))
        return sign * rev if rev < 0x7fffffff else 0

if __name__ == "__main__":
    print(Solution().reverse(1234))    
