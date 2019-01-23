"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
Return an empty list if there is no such transformation sequence.
    1. All words have the same length.
    2. All words contain only lowercase alphabetic characters.
    3. You may assume no duplicates in the word list.
    4. You may assume beginWord and endWord are non-empty and are not the same.

Example:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
"""
import collections


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        table = {}
        # build a table
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i + 1:]   # replace a letter with _
                table[s] = table.get(s, []) + [word]

        visited = set()
        # the keys of layer represent the words being visited
        # the items of layer represent the path from beginWord to the word being visited
        layer = {}
        layer[beginWord] = [[beginWord]]
        # BFS
        while layer:
            next_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    res.extend(path for path in layer[word])
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    words = table.get(s, [])
                    for neighbor in words:
                        if neighbor not in visited:
                            # record the path from beginWord to neighbor
                            next_layer[neighbor] += [parents + [neighbor]
                                                     for parents in layer[word]]
            # set visited words simultaneously
            visited |= set(next_layer.keys())
            layer = next_layer

        return res


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
