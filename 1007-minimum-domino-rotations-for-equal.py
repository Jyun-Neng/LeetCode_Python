class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        counts_A = collections.Counter(A)
        counts_B = collections.Counter(B)

        counts_same = collections.Counter()
        for x1, x2 in zip(A, B):
            if x1 == x2:
                counts_same[x1] += 1

        N = len(A)
        ans = N + 1
        for x in range(1, 6 + 1):
            if counts_A[x] + counts_B[x] - counts_same[x] == N:
                ans = min(ans, N - counts_A[x], N - counts_B[x])
                break
        return ans if ans <= N else -1

if __name__ == '__main__':
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]
    print(Solution().minDominoRotations(A, B))
