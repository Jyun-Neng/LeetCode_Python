"""
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).  For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happens before addition and subtraction.
It's not allowed to use the unary negation operator (-).  For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target.  Return the least number of expressions used.

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
"""


class Solution:
    def leastOpsExpressTarget(self, x, q):
        """
        :type x: int
        :type target: int
        :rtype: int
        time complexity: O(log(q))
        """
        n = 0
        while q:
            q, r = divmod(q, x)
            # case1: q*x + r, case2: (q+1)*x - (x-r)
            if n == 0:
                add, sub = r * 2, (x - r) * 2
            else:
                add, sub = min(r * n + add, (r + 1) * n +
                               sub), min((x - r) * n + add, (x - r - 1) * n + sub)
            n += 1
        # case2: x*x^n - (x-r)*x^n, because it requires to add x*x^n , it requires add n ops
        return min(add, n + sub) - 1


if __name__ == "__main__":
    obj = Solution()
    print(obj.leastOpsExpressTarget(3, 19))
