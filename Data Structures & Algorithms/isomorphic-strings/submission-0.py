class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        mapp_s={}
        mapp_t={}
        for ch1,ch2 in zip(s,t):
            if ch1 not in mapp_s and ch2 not in mapp_t:
                mapp_s[ch1]=ch2
                mapp_t[ch2]=ch1
            elif mapp_s.get(ch1,"")!=ch2 or mapp_t.get(ch2,"")!=ch1:
                return False
        return True