"""
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:
    1. Capitalization: If the query matches a word in the wordlist (case-insensitive), 
       then the query word is returned with the same case as the case in the wordlist.
    2. Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, 
       it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.

In addition, the spell checker operates under the following precedence rules:    
    1. When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    2. When the query matches a word up to capitlization, you should return the first such match in the wordlist.
    3. When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    4. If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].    

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
"""
import re
import collections


class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        time complexity: O(N)
        """
        wordset = set(wordlist)
        wordset_l = set(word.lower() for word in wordlist)
        vowelset = set(re.sub("[aeiou]", '#', word.lower())
                       for word in wordlist)  # substitute vowels to #
        wordmap = collections.defaultdict(list)
        vowelmap = collections.defaultdict(list)
        res = []

        # build maps
        for i, word in enumerate(wordlist):
            word = word.lower()
            wordmap[word].append(i)
            vowelmap[re.sub("[aeiou]", '#', word)].append(i)

        for query in queries:
            query_l = query.lower()
            query_vw = re.sub("[aeiou]", '#', query_l)
            # search element in set is O(1)
            if query in wordset:  # exactly match
                res.append(query)
            elif query_l in wordset_l:  # match in lower case of word
                res.append(wordlist[wordmap[query_l][0]])
            elif query_vw in vowelset:  # vowel errors
                res.append(wordlist[vowelmap[query_vw][0]])
            else:
                res.append('')
        return res


if __name__ == "__main__":
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE",
               "Hear", "hear", "keti", "keet", "keto"]
    print(Solution().spellchecker(wordlist, queries))
