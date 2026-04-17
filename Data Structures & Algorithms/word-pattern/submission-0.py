class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        if len(pattern)!=len(s):
            return False
        mapp_p={}
        mapp_s={}
        for ch1,w in zip(pattern,s):
            if ch1 not in mapp_p and w not in mapp_s:
                mapp_p[ch1]=w
                mapp_s[w]=ch1
            elif mapp_p.get(ch1,"")!=w or mapp_s.get(w,"")!=ch1:
                return False
        return True