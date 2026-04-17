class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum=0
        cur_sum=0
        for i in range(len(nums)):
            if i==0:
                cur_sum=nums[i]
            elif nums[i-1]<nums[i]:
                cur_sum+=nums[i]
            else:
                cur_sum=nums[i]
            max_sum=max(max_sum,cur_sum)
        return max_sum