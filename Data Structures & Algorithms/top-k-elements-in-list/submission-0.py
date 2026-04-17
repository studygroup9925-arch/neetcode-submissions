class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp=Counter(nums)
        sorted_items=sorted(mapp.items(),key=lambda x:x[1],reverse=True)
        return [items[0] for items in sorted_items[:k]]