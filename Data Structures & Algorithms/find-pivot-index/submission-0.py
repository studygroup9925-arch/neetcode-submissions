class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        cur_sum=0
        for i,num in enumerate(nums):
            if total_sum-num==cur_sum:
                return i
            cur_sum+=num
            total_sum-=num
        return -1