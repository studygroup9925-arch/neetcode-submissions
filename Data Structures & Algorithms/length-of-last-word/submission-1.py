class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_idx=len(s)-1
        while last_idx>=0 and s[last_idx]==' ':
            last_idx-=1
        first_idx=last_idx
        while last_idx>=0 and s[last_idx]!=' ':
            last_idx-=1
        return first_idx-last_idx