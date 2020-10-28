from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        m = min(A)
        res = []
        for char in m:
            if all(char in i for i in A):
               res.append(char)
               A = [i.replace(char,"",1) for i in A]

        return res