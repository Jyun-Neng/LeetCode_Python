"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
    1. Return 0 if there is no such transformation sequence.
    2. All words have the same length.
    3. All words contain only lowercase alphabetic characters.
    4. You may assume no duplicates in the word list.
    5. You may assume beginWord and endWord are non-empty and are not the same.

Example:

Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.    
"""
import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        table = {}
        # build a table
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]   # replace a letter with _
                table[s] = table.get(s, []) + [word]

        queue = collections.deque([(beginWord, 1)])
        visited = set()
        # BFS
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
            if word == endWord:
                return steps
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]
                words = table.get(s, [])
                for neighbor in words:
                    if neighbor not in visited:
                        queue.append((neighbor, steps + 1))
        return 0


if __name__ == "__main__":
    beginWord, endWord = "hit", "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
