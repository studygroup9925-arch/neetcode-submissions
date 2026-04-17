class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*(2*n)
        low,high=0,n
        while low<n and high<2*n:
            result[low]=nums[low]
            result[high]=nums[low]
            low+=1
            high+=1
        return result