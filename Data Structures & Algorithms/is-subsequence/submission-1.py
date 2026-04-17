class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True
        subseq=0
        for i in range(len(t)):
            if t[i]==s[subseq]:
                subseq+=1
            if subseq==len(s):
                return True
        return subseq==len(s)