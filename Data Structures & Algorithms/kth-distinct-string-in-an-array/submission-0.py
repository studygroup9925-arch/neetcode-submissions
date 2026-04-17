class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=Counter(arr)
        res=""
        for key,v in count.items():
            if k==1 and v==1:
                res=key
                break
            elif v==1:
                k-=1
        return "" if len(count)<k else res