"""
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) 
subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
Return the minimum number of K-bit flips required so that there is no 0 in the array.  
If it is not possible, return -1.

Note:

    1. 1 <= A.length <= 30000
    2. 1 <= K <= A.length

Example:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
"""


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        cnt = flip = 0
        table = [0] * length
        for i in range(length):
            flip ^= table[i]
            if A[i] ^ flip == 0:
                if i + K > length:
                    return -1
                cnt += 1
                flip ^= 1
                if i + K < length:
                    table[i + K] ^= 1
        return cnt


if __name__ == "__main__":
    A, K = [0, 1, 0], 1
    print(Solution().minKBitFlips(A, K))
