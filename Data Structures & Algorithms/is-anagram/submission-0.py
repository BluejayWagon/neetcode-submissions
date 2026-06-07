class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #build hash of s
        sHash= {}
        for char in s:
            sHash[char] = sHash.get(char, 0) + 1
        #build hash of t
        tHash = {}
        for char in t:
            tHash[char] = tHash.get(char, 0) + 1
        #compare hash tables
        for key in sHash:
            if key not in tHash or key not in sHash or tHash[key] != sHash[key]:
                return False
        return True