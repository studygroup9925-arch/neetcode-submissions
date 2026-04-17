class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mapp=Counter(arr)
        res=-1
        for k,v in mapp.items():
            if k==v:
                res=max(res, k)
        return res