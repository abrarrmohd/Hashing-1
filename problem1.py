"""
Approach: group according to the word count and hash the word-count in a a tuple 
t.c. = O(n*k) (where n = len(s) and k is the max size of each string in s)
s.c. = O(n)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_word_count(s):
            count = [0 for i in range(26)]
            for char in s:
                count[ord(char) - ord('a')] += 1
            return count
        groups = collections.defaultdict(list)
        for s in strs:
            count = get_word_count(s)
            groups[tuple(count)].append(s)
        return list(groups.values())