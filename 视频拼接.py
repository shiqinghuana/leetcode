from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [0] * (T+1)

        for a,b in clips:
            if a<=T:
                dp[a] = max(b,dp[a])

        def dfs(start = 0,end = dp[0],n=1):
            if end>=T:
                return n
            if n>len(dp) or end<=start:
                return -1
            m = max(dp[start+1:end+1])
            n+=1
            return dfs(end,m,n)

        return dfs()