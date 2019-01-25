"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
Input:
    X X X X
    X O O X
    X X O X
    X O X X
Output:    
    X X X X
    X X X X
    X X X X
    X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.    
"""
import collections


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        h = len(board)
        w = len(board[0])
        # surrounded regions will not exist
        # finish this function directly
        if h < 2 or w < 2:
            return
        queue = collections.deque([])
        # find all 'O's on the border
        # change them to '-' and put their coordinate into queue
        for x in range(w):
            if board[0][x] == 'O':
                queue.append([x, 0])
                board[0][x] = '-'
            if board[h - 1][x] == 'O':
                queue.append([x, h - 1])
                board[h - 1][x] = '-'
        for y in range(h):
            if board[y][0] == 'O':
                queue.append([0, y])
                board[y][0] = '-'
            if board[y][w - 1] == 'O':
                queue.append([w - 1, y])
                board[y][w - 1] = '-'
        # BFS
        while queue:
            x, y = queue.popleft()
            if x > 0 and board[y][x - 1] == 'O':
                board[y][x - 1] = '-'
                queue.append([x - 1, y])
            if x < w - 1 and board[y][x + 1] == 'O':
                board[y][x + 1] = '-'
                queue.append([x - 1, y])
            if y > 0 and board[y - 1][x] == 'O':
                board[y - 1][x] = '-'
                queue.append([x, y - 1])
            if y < h - 1 and board[y + 1][x] == 'O':
                board[y + 1][x] = '-'
                queue.append([x, y + 1])
        # change '-' back to 'O', it means that the region is not a surrounded region
        for x in range(w):
            for y in range(h):
                board[y][x] = 'O' if board[y][x] == '-' else 'X'


if __name__ == "__main__":
    board = [['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X'], [
        'X', 'X', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'O', 'X']]
    Solution().solve(board)
    print(board)
