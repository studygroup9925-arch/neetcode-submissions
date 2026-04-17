class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        cand=None
        for num in nums:
            if num==cand or count==0:
                cand=num
                count+=1
            else:
                count-=1
        return cand