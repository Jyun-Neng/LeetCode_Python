"""
Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once.

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
"""
import math

class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        pow_ints = []
        if bound == 0:
            return pow_ints
        
        max_num = max(x, y)
        min_num = min(x, y)
        
        if max_num == 1:
            if bound > max_num:
                pow_ints.append(2)
            return pow_ints
            
        pow_i = int(math.log(bound) // math.log(max_num)) + 1
        
        for i in range(pow_i + 1):
            if min_num == 1:
                pow_int = pow(max_num, i) + 1
                if bound >= pow_int:
                    pow_ints.append(pow_int)
            else:
                bound_y = bound - pow(max_num, i)
                if bound_y <= 0:
                    continue
                pow_j = int(math.log(bound_y) // math.log(min_num)) + 1
                for j in range(pow_j + 1):
                    pow_int = pow(max_num, i) + pow(min_num, j)
                    if pow_int not in pow_ints and pow_int <= bound:
                        pow_ints.append(pow_int)
        pow_ints.sort()
        return pow_ints

if __name__ == "__main__":
    x, y, bound = 2, 3, 10
    print(Solution().powerfulIntegers(x, y, bound))
