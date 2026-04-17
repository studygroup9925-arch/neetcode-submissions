class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=0
        for i in range(n):
            idx=abs(nums[i])-1
            if 0<=idx<n:
                if nums[idx]==0:
                    nums[idx]=float('inf')
                elif 0<nums[idx]<=n:
                    nums[idx]=-nums[idx]
        result=[]
        for i in range(n):
            if nums[i]>0:
                result.append(i+1)
        return result


# [4,3,2,7,8,2,3,1]
# 1-8 
# if n<=0 or nums[i]>n:
#     nums[i]=0

# result=[]
# for i in range(n):
#     idx=abs(nums[i])-1
#     if 0<=idx<n:
#         if nums[idx]==0:
#             nums[idx]='inf'
#         elif nums[idx]>0:
#             nums[idx]=-nums[idx]
# [4,3,2,7,8,2,3,1]
#    -3-2-7   -3-1
# [0,1,2,3,4,5,6,7]
