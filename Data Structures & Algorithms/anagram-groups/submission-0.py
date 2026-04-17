class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp={}
        for s in strs:
            sorted_s=tuple(sorted(s))
            if sorted_s in mapp:
                mapp[sorted_s].append(s)
            else:
                mapp[sorted_s]=[s]
        return [v for k,v in mapp.items()]