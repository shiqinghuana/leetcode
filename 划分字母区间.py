from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        n = 0
        k = 0
        l = []

        while n<len(S):
            unio = set(S[n:k+1]) & set(S[k+1:])
            if unio:
                for i in unio:
                    k = max(k,S.rindex(i))
            else:
                l.append(k-n+1)
                k+=1
                n=k

        return l
