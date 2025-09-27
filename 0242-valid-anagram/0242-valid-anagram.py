class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s = {}
        set_t = {}
        for i in s:
            set_s[i] = set_s.get(i, 0) +1
        for i in t:
            set_t[i] = set_t.get(i, 0) +1
        
        for i in s:
            if set_s.get(i) != set_t.get(i):
                return False
        return True
        

            
        