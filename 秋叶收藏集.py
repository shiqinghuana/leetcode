class Solution:
    def  minimumOperations(self, leaves: str) -> int:

        a1,a2,a3 = int(leaves[0] =="y"),len(leaves),len(leaves)

        def dfs(n,a1,a2,a3,leaves: str):
            if n == len(leaves)-1:
                return min(a3,a2)+int(leaves[n]=="y")
            b1 = a1 + int(leaves[n]=="y")
            b2 = min(a2,a1) + int(leaves[n]=="r")
            b3 = min(a3,a2) + int(leaves[n]=="y")
            return dfs(n+1,b1,b2,b3,leaves)
        return dfs(1,a1,a2,a3,leaves)


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0, 0, 0] for _ in leaves]
        # 初始化路径
        dp[0][0] = int(leaves[0] == "y")  # 第一个字符只能在 第一个框
        dp[0][1] = dp[0][2] = dp[1][2] = n

        for i in range(1, n):
            isRed = int(leaves[i] == "r")
            isYellow = int(leaves[i] == "y")
            dp[i][0] = dp[i - 1][0] + isYellow
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + isRed
            if i >= 2:
                dp[i][2] = min(dp[i - 1][1], dp[i - 1][2]) + isYellow
        return dp[n - 1][2]