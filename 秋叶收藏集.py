class Solution:
    def  minimumOperations(self, leaves: str) -> int:


        def dfs(n=1,a1=int(leaves[0] == "y"),a2=float('inf'),a3=float('inf')):

            if n==len(leaves)-1:
                return min(a2,a3)+int(leaves[n]=='y')

            b1,b2,b3 = a1+int(leaves[n]=="y"),min(a1,a2)+int(leaves[n]=="r"),min(a2,a3)+int(leaves[n]=='y')


            return dfs(n+1,b1,b2,b3)
        return dfs()