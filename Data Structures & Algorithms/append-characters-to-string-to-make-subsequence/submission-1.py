class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx_s,idx_t=0,0
        while idx_s<len(s) and idx_t<len(t):
            if s[idx_s]==t[idx_t]:
                idx_s+=1
                idx_t+=1
            else:
                idx_s+=1
                
        return len(t)-idx_t


        # rows,cols=len(s),len(t)
        # dp=[[0]*(cols+1) for _ in range(rows+1)]
        # for i in range(rows+1):
        #     for j in range(cols+1):
        #         if i==0:
        #             dp[i][j]=j
        #         elif j==0:
        #             dp[i][j]=i
        #         elif s[i-1]==t[j-1]:
        #             dp[i][j]=dp[i-1][j-1]+1
        #         else:
        #             dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        # return len(s)-dp[rows][cols]

