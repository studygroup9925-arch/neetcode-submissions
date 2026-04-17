class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i, num in enumerate(nums):
            if target-num in mapp:
                return [mapp[target-num],i]
            mapp[num]=i
        return [-1,-1]