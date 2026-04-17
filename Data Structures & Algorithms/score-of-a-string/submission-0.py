class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        prev=s[0]
        for ch in s[1:]:
            ans+=abs(ord(prev)-ord(ch))
            prev=ch
        return ans