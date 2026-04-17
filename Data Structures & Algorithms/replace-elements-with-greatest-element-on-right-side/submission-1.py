class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        maxm=-1
        for i in range(n-1,-1,-1):
            cur=arr[i]
            arr[i]=maxm
            if cur>maxm:
                maxm=cur
        return arr
        # for i in range(n):
        #     right_max=-1
        #     for j in range(i+1,n):
        #         right_max=max(right_max,arr[j])
        #     result[i]=right_max
        # return result