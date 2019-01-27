"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example:

Input: dividend = 10, divisor = 3
Output: 3
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        time complexity: O(log N)
        """
        # the only case may cause overflow
        if dividend == -2147483648 and divisor == -1:
            return 0x7fffffff
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res, bits = 0, divisor.bit_length()
        # for special case 0xffffffff, it should consider 32-bit division
        # this method may cause overflow in other languages because of the shift right operation
        # long division method
        for bit in range(33 - bits)[::-1]:
            tmp = divisor << bit
            if dividend >= tmp:
                dividend -= tmp
                res += (1 << bit)
        return res if positive else -res


if __name__ == "__main__":
    a, b = 10, 3
    print(Solution().divide(a, b))
