"""
Approach: use two maps to see if the elements map to the same element
t.c.-> O(k) where k = len(pattern) = len(s)
s.c.-> O(k)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        pTos = collections.defaultdict(str)
        sTop = collections.defaultdict(str)
        
        for i in range(len(pattern)):
            if pattern[i] not in pTos:
                pTos[pattern[i]] = words[i]
            if pattern[i] in pTos and pTos[pattern[i]] != words[i]:
                return False

        for i in range(len(words)):
            if words[i] not in sTop:
                sTop[words[i]] = pattern[i]
            if words[i] in sTop and sTop[words[i]] != pattern[i]:
                return False
        return True