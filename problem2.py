"""
Approach: Try to see if eacdh character in s maps to same char in t using a hashmap. Since we need to check if the reverse is true
i.e. t -> s we can use a set which logs whether a char in t was used for the first time by s (can also mean char in s was used by t)
when a new char in s maps to a char present in the tSet means that char was already mapped to a different char in s.
t.c.-> O(k) where k = len(s) = len(t)
s.c.-> O(k)
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        
        sMap = collections.defaultdict(str)
        tSet = set()
        for i in range(n):
            if s[i] not in sMap:
                if t[i] in tSet:
                    return False
                sMap[s[i]] = t[i]
                tSet.add(t[i])
            else:
                if sMap[s[i]] != t[i]:
                    return False
        return True
                